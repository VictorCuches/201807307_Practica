# MANUAL DE USUARIO SimpleQL
## Descripción
SimpleQL es un lenguaje de consultas que funciona únicamente a nivel de consola, su propósito es facilitar al usuario la búsqueda de registros completos en archivos json, en los que buscar registro por registro podría ser muy tedioso y cansado. SimpleQL permite al usuario cargar información a memoria por medio de comandos y obtener algunos datos generales acerca de esta, como el número de registros, el valor máximo de un atributo o incluso un reporte de en html de un conjunto de registros. 

## Caracteristicas de SimpleQL
- Todos los comandos y campos son *case insensitive* esto quiere decir que si el usuario introduce el comando "caRGar" el programa identificara que trata del comando "CARGAR".
- La extensión de archivos que maneja SimpleQL es .json, la estructura de como deben ser los archivos se mostrara al final de este manual. 

## Comandos
##### CARGAR 
Al iniciar el programa Este comando permitirá la carga de diferentes archivos a memoria, el único parámetro que lo conforma es una lista de direcciones a los archivos que cargará a memoria.
###### Ejemplo: CARGAR archivo1, archivo2, archivo3, …… archivoN


![](image/cargar.jpg)
