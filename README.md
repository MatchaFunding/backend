# 🐍 BackEnd y Base de Datos

## Requisitos

Se necesita usar la misma versionde python que el proyecto base.
Se debe tener instalado _django_, _djangorestframework_ y _mysql_.

## Instalacion

Usando [Python 3.12.10](https://www.python.org/downloads/release/python-31210/), instalar las dependencias por medio de _pip_.

```
pip install django
pip install djangorestframework
pip install mysqlclient
pip install django-cors-headers
```

Para la Base de Datos, descargar [MariaDB 12.0.1](https://mariadb.org/download/?t=mariadb&p=mariadb&r=12.0.1&os=windows&cpu=x86_64&pkg=msi&mirror=insacom).

## Configuracion

Una vez esten satisfechos todos los requisitos hay que crear la Base de Datos
correspondiente.
Por motivos de consistencia, todos debiesen usar las mismas credenciales y configuraciones.

Al usar _MariaDB_ / _MySQL_ por primera vez debemos crear un user y password
```
mysql_secure_installation.exe
```

Tras configurar _MariaDB_ / _MySQL_ hay que crear la Base de Datos vacia que luego
sera poblada con las tablas correspondientes por Django.

```
mysql -u {USER} -p{PASSWORD}
CREATE DATABASE MatchaFundingDB;
```

La salida completa debiese verse algo asi.

```
C:\Users\ElMaikina\Code\matcha-funding\databases> mysql -u {USER} -p{PASSWORD}
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 89
Server version: 9.2.0 MySQL Community Server - GPL

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [(none)]> CREATE DATABASE MatchaFundingDB;
MySQL [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| matchafundingdb    |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.002 sec)
```

Descargar el archivo _matchafunding.conf_ y guardarlo en *_C:/_*, este sera
usado por Django para conectarse a la Base de Datos creada.

Finalmente, estando en la carpeta _/backend_ (raíz), ejecutar los
comandos a continuacion para crear las Tablas en la Base de Datos.

```
C:\Python312\python.exe manage.py makemigrations backend
C:\Python312\python.exe manage.py migrate backend
```

## Ejecucion

Para correr el backend hay que ejecutar el siguiente commando desde la terminal:

```
C:\Python312\python.exe manage.py runserver
```

## Testing

Para agregar datos hay que levantar el sistema con el paso anterior e ir a la
siguiente direccion: [http://127.0.0.1:8000](http://127.0.0.1:8000). Ahi
apareceran todas las vistas implementadas, las cuales son accesibles agregando
el nombre de dicho metodo al _URL_ 
(por ejemplo: [http://127.0.0.1:8000/enviarnuevopostulante/](http://127.0.0.1:8000/enviarnuevopostulante/))

Para implemtar la _API_ las llamadas deben estar en formato _JSON_.

```json
{
    "Nombre":"A Darle Atomos",
    "Creacion":"2024-10-10",
    "Tipo":"Individual",
    "Perfil":"Educacion",
    "Razon":"Incentivar la educacion mediante experiencias interactivas",
    "RUT":"12.345.678-9"
}
```

**Importante**: Los _ID_ de las clases son auto-incrementales, no se deben pasar
por medio de la llamda.
