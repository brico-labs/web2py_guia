# Introducción

[web2py](http://www.web2py.com/) es un framework para facilitar el
desarrollo de aplicaciones web escrito en Python.

***web2py*** funciona correctamente en Python 3. Su curva de aprendizaje
no es tan empinada como la de Django y en muchos sentidos es más moderno
que Django.

**web2py** está basado (no estrictamente) en el modelo
[MVC](https://es.wikipedia.org/wiki/Modelo%E2%80%93vista%E2%80%93controlador)

**web2py** incorpora *Bootstrap 4*

## Referencias

  - [Evolución del modelo
    MVC](https://martinfowler.com/eaaDev/uiArchs.html)
  - [Fat models and thin
    controllers](https://nomadphp.com/blog/60/working-with-the-thin-controller-and-fat-model-concept-in-laravel)
  - [Crítica del
    mantra](https://nomadphp.com/blog/60/working-with-the-thin-controller-and-fat-model-concept-in-laravel)

# Empezar rápido

## Instalación

Vamos a ver el proceso de instalación de una instancia de web2py en modo
*standalone*. Normalmente uso web2py instalado de esta forma para
entornos de desarrollo. Para un entorno de producción lo normal es
instalar web2py tras un servidor web como
[*Apache*](https://www.apache.org/) o [Nginx](https://www.nginx.com/),
aunque dependiendo de la carga de trabajo y de como administres tus
sistemas no tiene por que ser imprescindible y lo puedes poner en
producción en modo *standalone*.

1.  Creamos un entorno virtual
    
    Como ya hemos comentado ***web2py*** funciona ya en Python 3. Además
    con Python nunca está de mas encapsular nuestras pruebas y
    desarrollos en un entorno virtual.\[1\] Así que creamos el
    virtualenv que llamaremos *web2py*:
    
        mkvirtualenv -p `which python3` web2py

2.  Bajamos el programa de la web de Web2py y descomprimimos el
    framework:
    
    ``` {bash}
    # creamos un directorio (cambia el path a tu gusto)
    mkdir web2py_test
    cd web2py_test
    
    # bajamos el programa de la web y descomprimimos
    wget https://mdipierro.pythonanywhere.com/examples/static/web2py_src.zip
    
    # opcionalmente borramos el zip, sería mejor guardarlo
    # por si queremos hacer nuevas instalaciones
    rm web2py_src.zip
    ```

3.  Generamos certificados para el protocolo *ssl*:
    
    Para usar con comodidad web2py conviene que nos generemos unos
    certificados para gestionar el ssl:
    
    ``` {bash}
    # nos movemos al directorio de web2py
    cd web2py
    
    openssl genrsa -out server.key 2048
    openssl req -new -key server.key -out server.csr
    
    Country Name (2 letter code) [AU]:ES
    State or Province Name (full name) [Some-State]:A Coruna
    Locality Name (eg, city) []:A Coruna
    Organization Name (eg, company) [Internet Widgits Pty Ltd]:BricoLabs
    Organizational Unit Name (eg, section) []:Division de Hackeo
    Common Name (e.g. server FQDN or YOUR name) []:testServer@bricolabs.cc
    Email Address []:contacto@bricolabs.cc
    
    Please enter the following 'extra' attributes
    to be sent with your certificate request
    A challenge password []:secret1t05
    An optional company name[]:Asociacion BricoLabs
    ```
    
    Y ahora ejecutamos:
    
        openssl x509 -req -days 365 -in server.csr \
        -signkey server.key -out server.crt

4.  Arrancamos el servidor:
    
    Ahora deberíamos tener los ficheros `server.key`, `server.csr` y
    `server.crt` en el directorio raiz de web2py, una vez generados
    estos ficheros podemos arrancar el servidor con los siguientes
    parámetros (recuerda activar el entorno virtual si no lo tienes
    activo):
    
    ``` {bash}
    python web2py.py -a 'admin_password' -c server.crt -k server.key \
    -i 0.0.0.0 -p 8000
    ```
    
    Y ya podemos acceder nuestro server en la dirección
    <https://localhost:8000>

5.  Servidor de base de datos.
    
    Para usar ***web2py*** es imprescindible tener acceso a un servidor
    de base de datos. Podemos usar MySQL o MariaDB por ejemplo. Pero
    para empezar rápidamente vamos a tirar de
    [SQLite](https://www.sqlite.org/version3.html), un servidor fácil de
    instalar potente y versátil. Es importante usar la versión 3 que
    introduce grandes mejoras sobre el antiguo *SQLite*
    
    ``` {bash}
    sudo apt install sqlite3
    ```

Y ahora si que ya tenemos todo listo para empezar a usar ***web2py***.
Podemos crear nuestra primera aplicación.

### Los detalles tenebrosos

Si tienes mucha prisa por aprender web2py puedes saltarte esta sección e
ir directamente a la sección [siguiente](#nuestra-primera-aplicación)

Si por el contrario quieres entender exactamente que hemos hecho para
poder arrancar el ***web2py*** este puede ser el primer paso.

  - ¿Qué es un *virtualenv*?  
    Python nos permite definir *virtualenv*. Un *virtualenv* es un
    entorno python aislado. Todos los *virtualenvs* están aislados entre
    si y mejor todavía son independientes del python del sistema. Esto
    te permite tener multiples entornos de desarrollo (o producción)
    cada uno con distintas versiones de python y diferentes librerias
    python instaladas en cada uno de ellos, o quizás diferentes
    versiones de las mismas librerias.

  - ¿Que es *virtualenvwrapper*?  
    Es un frontend para usar *virtualenv*, la herramienta nativa de
    python para gestionar *virtualenvs*. Es completamente opcional,
    aunque a mi me parece muy cómoda.

  - ¿Qué es todo eso de los certificados?  
    ***web2py*** viene preparado para usar *https* (estas siglas tienen
    varias interpretaciones: *HTTP over TLS*, *HTTP over SSL* o *HTTP
    Secure*). *https* usa comunicaciones cifradas entre tu navegador y
    el servidor web para garantizar dos cosas: que estás accediendo al
    auténtico servidor y que nadie este interceptando la comunicación
    entre navegador y servidor.
    
    Para usar *https* hay que hacer varias cosas:
    
      - Generar un CSR (Certificate Signing Request)
      - Obtener con ese CSR un certificado SSL de una autoridad
        certificadora (CA)
      - O alternativamente generar nosotros un certificado a partir del
        CSR
    
    Lo que hemos hecho con los comandos *openssl* ha sido:
    
      - Generar un par de claves (privada y pública) para nuestro
        servidor (`server.key`)
      - Generar con esa clave un CSR (el CSR lleva la información que le
        hemos metido de nuestro servidor y la clave pública)
      - Generar un certificado firmándolo nosotros mismos con esa misma
        clave como si fueramos la autoridad certificadora.
    
    Esto nos vale para arrancar ***web2py*** aunque nuestro navegador
    nos dará una alerta de riesgo de seguridad por que no reconoce a la
    CA.

[Más info de
*openssl*](https://www.digitalocean.com/community/tutorials/openssl-essentials-working-with-ssl-certificates-private-keys-and-csrs)

## Nuestra primera aplicación

Vamos a crear nuestra primera aplicación en web2py.

Si has seguido los pasos de la [sección anterior](#instalación) ya
tienes el ***web2py*** funcionando y puedes seguir cualquiera de los
tutoriales que hay en la red para aprender.

En esta guía vamos a ver la creación de una aplicación paso a paso.
Crearemos una aplicación de inventario para el material de la Asociación
BricoLabs, empezando por una funcionalidad sencilla y añadiendo cosas
según se nos ocurran.

Crea una aplicación desde el interfaz de administración, en nuestro caso
la llamaremos ***cornucopia***.

Nuestro ***web2py*** nace con algunas aplicaciones de ejemplo creadas,
de hecho la pantalla inicial es una de ellas la aplicación “Welcome” o
“Bienvenido” (dependerá del lenguaje por defecto de tu navegador).

Para crear nuestra aplicación ***cornucopia***:

  - Vamos al botón **admin** en la pantalla principal.
  - Metemos la password con la que hemos arrancado el ***web2py*** en la
    linea de comandos.
  - Desde la ventana de administración creamos nuestra nueva aplicación

Inmediatamente nos encontraremos en la ventana de diseño de nuestra
nueva aplicación. ***web2py*** nos permite diseñar completamente nuestra
aplicación desde aquí, ni siquiera necesitaremos un editor de texto
(aunque nada impide usar uno, desde luego).

### `private/appconfig.ini`

El primer fichero que vamos a examinar es `private/appconfig.ini` La
sección `private` debería estar abajo de todo en la ventana de diseño.

En la sección `[app]` del fichero podemos configurar el nombre de la
aplicación y los datos del desarrollador.

En la sección `[db]` fichero configuramos el motor de base de datos que
vamos a usar en nuestra aplicación. Por defecto viene configurado
*sqlite* así que no vamos a tener que cambiar nada en este sentido.

En la seccion `[smtp]` podemos configurar el gateway de correo que usará
la aplicación para enviar correos a los usuarios. Por defecto viene
viene la configuración para usar una cuenta de gmail como gateway, solo
tenemos que cubrir los valores de usuario y password y la dirección de
correo.

### El Modelo

En la parte superior de la ventana de diseño (o edición) de nuestra
aplicación tenemos la sección `Models`

![Menú Modelos](src/img/models_menu.jpg)

***web2py*** se encarga de crear las tablas necesarias en la base de
datos que le hayamos indicado que use.

Al crear la aplicación \_**web2py** ha creado en la base de datos todas
las tablas relacionadas con la gestión de usuarios y sus privilegios.

Si echamos un ojo al modelo gráfico (*Graphs Models*) veremos las tablas
que ***web2py*** ha creado por defecto y las relaciones entre ellas.

Si vemos el log de comandos de sql (*sql.log*) veremos los comandos que
***web2py*** ha ejecutado en el motor de base de datos.

Y por último si vemos *database administration* podremos ver las tablas
creadas en la base de datos, e incluso crear nuevos registros en esas
tablas.

También podemos echar un ojo al contenido del fichero `db.py` o
`menu.py` pero por el momento **no** vamos a modificar nada en esos
ficheros.

# Secciones en el futuro

## web2py y git

## Instalación con nginx

## Certificados let’s encrypt

1.  Los siguientes comandos asumen que tienes instalado
    *virtualenvwrapper* como recomendamos en la guía de postinstalación
    de Linux Mint, si no lo tienes tendrás que crear un virtualenv con
    los comandos tradicionales
