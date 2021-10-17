# WebScraping_News

# econoamigos

Ejecución de los scripts para la implementacion de Scraping mediande AWS a diferentes paginas web 

1. Creacion de un ambiente virutal

    ```cmd
    C:\Equipo> virtualenv env
    ```

2. Activar el ambiete virtual

    ```cmd
    C:\Equipo> env/bin/activate
    ```

3. Intalar todos los paquetes de python

    ```cmd
    (env) C:\Equipo> pip install -r requirements.txt
    ```
    
4. Desplegue de las funciones lambda: El procedimiento se relaiza para desplegar la función lambda que descarga los archivos y los sube a S3, tambein se debe desarrollara para el folder lambda_Update_partitions


    ```cmd
    (env) C:\Equipo> cd lambda_Get_CSV
    ```


    ```cmd
    (env) C:\Equipo> zappa init
    ```
    

    ```cmd
    (env) C:\Equipo> zappa deploy dev
    ```   
    

      
5. Ejecución en Athena
En el servicio de AWS Athena, se ejecutan los comandos escritos en el archivo AthenaCode

