# Empezar rápido

## Instalación

Vamos a ver el proceso de instalación de una instancia de web2py en
modo _standalone_. Normalmente uso web2py instalado de esta forma para
entornos de desarrollo. Para un entorno de producción lo normal es
instalar web2py tras un servidor web como
[_Apache_](https://www.apache.org/) o [Nginx](https://www.nginx.com/),
aunque dependiendo de la carga de trabajo y de como administres tus
sistemas no tiene por que ser imprescindible y lo puedes poner en
producción en modo _standalone_.

1. Creamos un entorno virtual

   Como ya hemos comentado ___web2py___ funciona ya en Python 3. Además
   con Python nunca está de mas encapsular nuestras pruebas y desarrollos
   en un entorno virtual.^[Los siguientes comandos asumen que tienes
   instalado _virtualenvwrapper_ como recomendamos en la guía de
   postinstalación de Linux Mint, si no lo tienes tendrás que crear un
   virtualenv con los comandos tradicionales] Así que creamos el
   virtualenv que llamaremos _web2py_:

   ~~~~
   mkvirtualenv -p `which python3` web2py
   ~~~~

#. Bajamos el programa de la web de Web2py y descomprimimos el framework:

   ~~~~{bash}
   # creamos un directorio (cambia el path a tu gusto)
   mkdir web2py_test
   cd web2py_test

   # bajamos el programa de la web y descomprimimos
   wget https://mdipierro.pythonanywhere.com/examples/static/web2py_src.zip

   # opcionalmente borramos el zip, sería mejor guardarlo
   # por si queremos hacer nuevas instalaciones
   rm web2py_src.zip
   ~~~~

#. Generamos certificados para el protocolo _ssl_:

   Para usar con comodidad web2py conviene que nos generemos unos
   certificados para gestionar el ssl:

   ~~~~{bash}
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
   ~~~~

   Y ahora ejecutamos:

   ~~~~
   openssl x509 -req -days 365 -in server.csr \
   -signkey server.key -out server.crt
   ~~~~

#. Arrancamos el servidor:

   Ahora deberíamos tener los ficheros `server.key`, `server.csr` y
   `server.crt` en el directorio raiz de web2py, una vez generados
   estos ficheros podemos arrancar el servidor con los siguientes
   parámetros (recuerda activar el entorno virtual si no lo tienes
   activo):

   ~~~~{bash}
   python web2py.py -a 'admin_password' -c server.crt -k server.key \
   -i 0.0.0.0 -p 8000
   ~~~~

   Y ya podemos acceder nuestro server en la dirección <https://localhost:8000>
   
#. Servidor de base de datos.
   
   Para usar ___web2py___ es imprescindible tener acceso a un servidor
   de base de datos. Podemos usar MySQL o MariaDB por ejemplo. Pero
   para empezar rápidamente vamos a tirar de
   [SQLite](https://www.sqlite.org/version3.html), un servidor fácil
   de instalar potente y versátil. Es importante usar la versión 3 que
   introduce grandes mejoras sobre el antiguo _SQLite_
   
   ~~~~{bash}
   sudo apt install sqlite3
   ~~~~

Y ahora si que ya tenemos todo listo para empezar a usar ___web2py___.
Podemos crear nuestra primera aplicación.

### Los detalles tenebrosos

Si tienes mucha prisa por aprender web2py puedes saltarte esta
sección e ir directamente a la sección [siguiente](#nuestra-primera-aplicación)

Si por el contrario quieres entender exactamente que hemos hecho para
poder arrancar el ___web2py___ este puede ser el primer paso.

¿Qué es un _virtualenv_?

: Python nos permite definir _virtualenv_. Un _virtualenv_ es un
  entorno python aislado. Todos los _virtualenvs_ están aislados entre
  si y mejor todavía son independientes del python del sistema. Esto
  te permite tener multiples entornos de desarrollo (o producción)
  cada uno con distintas versiones de python y diferentes librerias
  python instaladas en cada uno de ellos, o quizás diferentes
  versiones de las mismas librerias.

¿Que es _virtualenvwrapper_?

: Es un frontend para usar _virtualenv_, la herramienta nativa de
  python para gestionar _virtualenvs_. Es completamente opcional,
  aunque a mi me parece muy cómoda.

¿Qué es todo eso de los certificados?

: ___web2py___ viene preparado para usar _https_ (estas siglas tienen
  varias interpretaciones: _HTTP over TLS_, _HTTP over SSL_ o _HTTP Secure_).
  _https_ usa comunicaciones cifradas entre tu navegador y el servidor
  web para garantizar dos cosas: que estás accediendo al auténtico
  servidor y que nadie este interceptando la comunicación entre
  navegador y servidor.

: Para usar _https_ hay que hacer varias cosas:

    * Generar un CSR (Certificate Signing Request)
    * Obtener con ese CSR un certificado SSL de una autoridad certificadora (CA)
    * O alternativamente generar nosotros un certificado a partir del CSR

: Lo que hemos hecho con los comandos _openssl_ ha sido:

    * Generar un par de claves (privada y pública) para nuestro
      servidor (`server.key`)
    * Generar con esa clave un CSR (el CSR lleva la información que le
      hemos metido de nuestro servidor y la clave pública)
    * Generar un certificado firmándolo nosotros mismos con esa misma
      clave como si fueramos la autoridad certificadora.
      
: Esto nos vale para arrancar ___web2py___ aunque nuestro navegador
  nos dará una alerta de riesgo de seguridad por que no reconoce a la
  CA.
  
[Más info de _openssl_](https://www.digitalocean.com/community/tutorials/openssl-essentials-working-with-ssl-certificates-private-keys-and-csrs)


## Nuestra primera aplicación

Vamos a crear nuestra primera aplicación en web2py.

Si has seguido los pasos de la [sección anterior](#instalación) ya
tienes el ___web2py___ funcionando y puedes seguir cualquiera de los
tutoriales que hay en la red para aprender.

En esta guía vamos a ver la creación de una aplicación paso a paso.
Crearemos una aplicación de inventario para el material de la
Asociación BricoLabs, empezando por una funcionalidad sencilla y
añadiendo cosas según se nos ocurran.

Crea una aplicación desde el interfaz de administración, en nuestro
caso la llamaremos ___cornucopia___.

Nuestro ___web2py___ nace con algunas aplicaciones de ejemplo creadas,
de hecho la pantalla inicial es una de ellas la aplicación "Welcome" o
"Bienvenido" (dependerá del lenguaje por defecto de tu navegador).

Para crear nuestra aplicación ___cornucopia___:

* Vamos al botón __admin__ en la pantalla principal.
* Metemos la password con la que hemos arrancado el ___web2py___ en la
  linea de comandos.
* Desde la ventana de administración creamos nuestra nueva aplicación

Inmediatamente nos encontraremos en la ventana de diseño de nuestra
nueva aplicación. ___web2py___ nos permite diseñar completamente
nuestra aplicación desde aquí, ni siquiera necesitaremos un editor de
texto (aunque nada impide usar uno, desde luego).

### `private/appconfig.ini`

El primer fichero que vamos a examinar es `private/appconfig.ini` La
sección `private` debería estar abajo de todo en la ventana de diseño.

En la sección `[app]` del fichero podemos configurar el nombre de la
aplicación y los datos del desarrollador.

En la sección `[db]` fichero configuramos el motor de base de datos
que vamos a usar en nuestra aplicación. Por defecto viene configurado
_sqlite_ así que no vamos a tener que cambiar nada en este sentido.

En la seccion `[smtp]` podemos configurar el gateway de correo que
usará la aplicación para enviar correos a los usuarios. Por defecto
viene viene la configuración para usar una cuenta de gmail como
gateway, solo tenemos que cubrir los valores de usuario y password y
la dirección de correo.


### El Modelo

En la parte superior de la ventana de diseño (o edición) de nuestra
aplicación tenemos la sección `Models`

![Menú Modelos](src/img/models_menu.jpg)

___web2py___ se encarga de crear las tablas necesarias en la base de
datos que le hayamos indicado que use. 

Al crear la aplicación ___web2py__ ha creado en la base de datos todas
las tablas relacionadas con la gestión de usuarios y sus privilegios.

Si echamos un ojo al modelo gráfico (_Graphs Models_) veremos las
tablas que ___web2py___ ha creado por defecto y las relaciones entre
ellas.

Si vemos el log de comandos de sql (_sql.log_) veremos los comandos
que ___web2py___ ha ejecutado en el motor de base de datos.

Y por último si vemos _database administration_ podremos ver las
tablas creadas en la base de datos, e incluso crear nuevos registros
en esas tablas.

También podemos echar un ojo al contenido del fichero `db.py` o
`menu.py` pero por el momento __no__ vamos a modificar nada en esos
ficheros.





# Secciones en el futuro

## web2py y git

## Instalación con nginx

## Certificados let's encrypt


