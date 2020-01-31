

# C01
Introducción al anonimato (PoC Proxy)

**Descripción**
La prueba de concepto consiste en dos servicios, un servidor de aplicaciones web nginx y un servidor proxy

**Instrucciones**
1. Levantar servicios
    ``` bash
    $ docker-compose -f docker-compose.yml up --build
    ```
2. Obtener direcciones IP de los servicios
    ``` bash
    $ docker inspect clase01_proxy-server_1
    $ docker inspect clase01_web-server_1
    ```
3. Abrir la URL **http://< ip-web-server >/index.html**
	Esto debera de desplegarle una pagina con la leyenda "I know who u r"
4. Revisar los mensajes desplegados en la terminal en la que se ejecuto el comando `$ docker-compose -f docker-compose.yml up --build`
5. Configurar el navegador estableciendo el proxy manual con la ip del servidor proxy con el puerto 3128, una vez configurado  repetir paso 3 y 4, y comparar los resultados.
