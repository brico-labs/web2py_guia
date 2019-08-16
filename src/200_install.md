# Instalación

## Empezar rápido

Vamos a ver el proceso de instalación de una instancia de web2py en
modo _standalone_. Normalmente uso web2py instalado de esta forma para
entornos de desarrollo.


Bajamos el programa de la web de Web2py y descomprimimos el framework:

~~~~{bash}
# creamos un directorio (cambia el path a tu gusto)
mkdir web2py
cd web2py

# bajamos el programa de la web y descomprimimos
wget https://mdipierro.pythonanywhere.com/examples/static/web2py_src.zip


~~~~

Descomprimimos el framework,

Preparamos los certificados

openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr

Country Name (2 letter code) [AU]:ES
State or Province Name (full name) [Some-State]:CORUNA
Locality Name (eg, city) []:CORUNA
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Vodafone
Organizational Unit Name (eg, section) []:TNO
Common Name (e.g. server FQDN or YOUR name) []:txfinder
Email Address []:sergio.alvarino@vodafone.com

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:secret1t05
An optional company name []:Vodafone Spain

Ejecutamos:

openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

Ahora deberíamos tener los ficheros server.key, server.csr y server.crt en el directorio raiz de web2py, una vez generados estos ficheros tenemos que arrancar el servidor con los siguientes parámetros:

python web2py.py -a 'admin_password' -c server.crt -k server.key -i 0.0.0.0 -p 8000

Y ya podemos acceder nuestro server en la dirección https://localhost:8000
Preparando nuestra aplicación

    Crea una aplicación desde el interfaz de administración, en nuestro caso la llamaremos pyfinder

    Para usar MySQL como motor de base de datos: Editamos el fichero applications/pyfinder/private/appconfig.ini, tenemos que poner el uri que apunta a nuestra base de datos, sustituyendo dbUser, dbPass y dbName por valores reales.

<!-- end list -->

    ; App configuration
    [app]
    name        = PyFinder
    author      = Sergio Alvariño <sergio.alvarino@vodafone.com>
    description = TxFinder en Web2Py
    keywords    = Thope, TxFinder, web2py, python, framework
    generator   = Web2py Web Framework

    ; Host configuration
    [host]
    names = localhost:*, 127.0.0.1:*, *:*, *

    ; db configuration
    [db]
    ; uri       = sqlite://storage.sqlite
    uri         = mysql://dbUser:dbPass@localhost/dbName

    migrate   = true
    pool_size = 10 ; ignored for sqlite

    ; smtp address and credentials
    [smtp]
    server = smtp.gmail.com:587
    sender = salvari@gmail.com
    login  = username:password
    tls    = true
    ssl    = true

    ; form styling
    [forms]
    formstyle = bootstrap3_inline
    separator =

    Editamos el fichero applications/pyfinder/models/db.py Tenemos que asegurarnos de editar esta sección para que no nos de problemas con palabras reservadas:

<!-- end list -->

    db = DAL(myconf.get('db.uri'),
             pool_size=myconf.get('db.pool_size'),
             migrate_enabled=myconf.get('db.migrate'),
             check_reserved=['mysql'])
    #         check_reserved=['all'])

    Creamos un fichero db_custom.py en el directorio: applications/pyfinder/models El fichero tiene que ser parecido al que figura a continuación.

    IMPORTANTE: en cada tabla crear el campo id de tipo integer, es para uso interno de web2py

    IMPORTANTE: especificar migrate FALSE al final en todas las tablas externas

Ejemplo de contenido del fichero db_custom.py

db.define_table('afoxtfo',
    Field('id', 'integer'),
    Field('opti_of_connection_id' , 'string'),
    Field('afo' , 'string'),
    Field('afo_fiber' , 'string'),
    Field('opti_cable_id' , 'string'),
    Field('tfo' , 'string'),
    Field('tfo_fiber' , 'string'),
    Field('cable_endpoint' , 'string'),
    Field('side' , 'string'),
    Field('state' , 'string'),
    Field('loaddate' , 'string'),
    migrate = False);

db.define_table('physical',
    Field('id', 'integer'),
    Field('circuit_id', 'string'),
    Field('circuit_name', 'string'),
    Field('line_type_code', 'string'),
    Field('mux_type_code', 'string'),
    Field('vendor_code', 'string'),
    Field('line_of_sight_distance', 'string'),
    Field('distance', 'string'),
    Field('carrier_circuit_name', 'string'),
    Field('circuit_activation_date', 'string'),
    Field('circuit_deactivation_date', 'string'),
    Field('circuit_desconection_date', 'string'),
    Field('origination_tributary', 'string'),
    Field('destination_tributary', 'string'),
    Field('circuit_medium_type', 'string'),
    Field('phys_conn_bandwidth', 'string'),
    Field('circuit_state_code', 'string'),
    Field('from_user_site_id', 'string'),
    Field('from_map_site_id', 'string'),
    Field('from_site_name', 'string'),
    Field('from_zone', 'string'),
    Field('from_node_id', 'string'),
    Field('from_user_node_id', 'string'),
    Field('from_node_class_code', 'string'),
    Field('from_node_technology_code', 'string'),
    Field('from_node_state_code', 'string'),
    Field('from_phys_node_id', 'string'),
    Field('from_node_type_code', 'string'),
    Field('from_shelf_no', 'string'),
    Field('from_user_shelf_id', 'string'),
    Field('from_slot_no', 'string'),
    Field('from_slot_num_text', 'string'),
    Field('from_card_id', 'string'),
    Field('from_card_type_code', 'string'),
    Field('from_user_card_id', 'string'),
    Field('from_port_no', 'string'),
    Field('from_port_id', 'string'),
    Field('to_user_site_id', 'string'),
    Field('to_map_site_id', 'string'),
    Field('to_site_name', 'string'),
    Field('to_zone', 'string'),
    Field('to_node_id', 'string'),
    Field('to_user_node_id', 'string'),
    Field('to_node_class_code', 'string'),
    Field('to_node_tech_code', 'string'),
    Field('to_node_state_code', 'string'),
    Field('to_phys_node_id', 'string'),
    Field('to_node_type_code', 'string'),
    Field('to_shelf_no', 'string'),
    Field('to_user_shelf_id', 'string'),
    Field('to_slot_no', 'string'),
    Field('to_slot_num_text', 'string'),
    Field('to_card_id', 'string'),
    Field('to_card_type_code', 'string'),
    Field('to_user_card_id', 'string'),
    Field('to_port_no', 'string'),
    Field('to_port_id', 'string'),
    Field('loaddate', 'string'),
    Field('create_user_id', 'string'),
    Field('create_date', 'string'),
    Field('modified_user_id', 'string'),
    Field('modified_date', 'string'),
    migrate = False)
db.define_table('segment',
    Field('id', 'integer'),
    Field('virtual_link_id', 'string'),
    Field('path_name', 'string'),
    Field('origination_route_path', 'string'),
    Field('destination_route_path', 'string'),
    Field('path_type', 'string'),
    Field('protection_type', 'string'),
    Field('hop_no', 'string'),
    Field('physical_conn', 'string'),
    Field('physical_conn_id', 'string'),
    Field('physical_conn_media', 'string'),
    Field('physical_conn_bandwidth', 'string'),
    Field('logical_conn_id', 'string'),
    Field('logical_conn', 'string'),
    Field('logical_conn_type', 'string'),
    Field('origination_node_id', 'string'),
    Field('origination_node', 'string'),
    Field('origination_node_name', 'string'),
    Field('origination_card', 'string'),
    Field('origination_site_id', 'string'),
    Field('origination_site', 'string'),
    Field('origination_site_name', 'string'),
    Field('origination_site_latitude', 'string'),
    Field('origination_site_longitude', 'string'),

Receta para instalar desde cero bajando el repo de github
Checlist

    Crear bases de datos en MySQL
        txdb
        txdbnew
        txdbold
    Dar privilegios a


## Instalación con nginx

## Certificados let's encrypt
