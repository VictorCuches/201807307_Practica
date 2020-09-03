import json
import webbrowser
resultadoSuma = 0
print("----------------------------------BIENVENIDO A SimpleQL--------------------------------")

print("                              M E N U   P R I N C I P A L ")
print("Comandos que puedes utilizar: ")
print("- CARGAR")
print("- SALIR")


print("Escribe el nombre de los archivos que deseas cargar: ") 

opc_menu = input()
word_word = opc_menu.split() #separo la 'frase' en palabra por palabra en un arreglo 
#aqui debe ir el ciclo while 

        


print("..........................................................")
#print(word_word) #print de prueba para saber lo que estoy guardando con comas para comparar luego 
#print(opc_menu.split()[2]) Con este [2] puedo jalar la palabra que este en esa posicion 

#este for elimina las comas (,) del nombre del archivo para poder usarlo bien bien 
for i in range(len(word_word)):
    word_word[i] = word_word[i].replace(",", "")

#Metodo para cargar el archivo json
def cargar_json(ruta, dato_num, atributo, x, word_opc2): 
    with open(ruta) as contenido:
        archivi = json.load(contenido)            
        for element in archivi:
            if (atributo == "nombre"):
                encontrado = element.get('nombre')
                if (encontrado==dato_num ):#encuentra el registro que quiero buscar 
                    print("Busqueda finalizada, los datos son") 
                    for i in range(1, x): 
                        if (word_opc2[i]=="nombre"):
                            print("nombre: "+element.get('nombre'))
                        elif (word_opc2[i]=="edad" ):
                            print("edad: ",element.get('edad'))
                        elif (word_opc2[i]=="activo" ):
                            print("activo: ",element.get('activo'))
                        elif (word_opc2[i]=="promedio" ):
                            print("promedio: ",element.get('promedio'))         
            elif (atributo == "edad"):
                encontrado = element.get('edad')
                

                if (encontrado==dato_num):#encuentra el registro que quiero buscar 
                    print("Busqueda finalizada, los datos son") 
                    for i in range(1, x):
                         
                        if (word_opc2[i]=="nombre"):
                            print("nombre: "+element.get('nombre'))

                        elif (word_opc2[i]=="edad" ):
                            print("edad: ",element.get('edad'))
                        elif (word_opc2[i]=="activo" ):
                            print("activo: ",element.get('activo'))

                        elif (word_opc2[i]=="promedio" ):
                            print("promedio: ",element.get('promedio'))        

                
            elif (atributo == "promedio"):
                encontrado = element.get('promedio')
                

                if (encontrado==dato_num):#encuentra el registro que quiero buscar 
                    print("Busqueda finalizada, los datos son") 
                    for i in range(1, x):
                         
                        if (word_opc2[i]=="nombre"):
                            print("nombre: "+element.get('nombre'))

                        elif (word_opc2[i]=="edad" ):
                            print("edad: ",element.get('edad'))
                        elif (word_opc2[i]=="activo" ):
                            print("activo: ",element.get('activo'))

                        elif (word_opc2[i]=="promedio" ):
                            print("promedio: ",element.get('promedio'))            

                

            elif (atributo == "activo"):
                encontrado = element.get('activo')
                print(encontrado)

                if (encontrado==dato_num):#encuentra el registro que quiero buscar 
                    print("Busqueda finalizada, los datos son") 
                    for i in range(1, x):
                         
                        if (word_opc2[i]=="nombre"):
                            print("nombre: "+element.get('nombre'))

                        elif (word_opc2[i]=="edad" ):
                                print("edad: ",element.get('edad'))
                        elif (word_opc2[i]=="activo" ):
                                print("activo: ",element.get('activo'))

                        elif (word_opc2[i]=="promedio" ):
                                print("promedio: ",element.get('promedio'))             

                
            else:
                ("atrbuto invalido")
                

def suma_json(ruta, word_opc2):
    resultado = 0    
    with open(ruta) as contenido:
        archivi = json.load(contenido)
        if(word_opc2[1]=="edad"):
            for element in archivi:
                suma = int(element.get('edad'))
                resultado = resultado + suma            
            return resultado           
        elif (word_opc2[1]=="promedio"):
            for element in archivi:
                suma_prom = float(element.get('promedio'))
                resultado = resultado + suma_prom            
            return resultado 
        else: 
            print("Has seleccionado un atributo invalido")
            
def max_json(ruta, word_opc2):
    maxi= 0   
    with open(ruta) as contenido:
        archivi = json.load(contenido)
        if(word_opc2[1]=="edad"):
            for element in archivi:
                age = int(element.get('edad'))
                if (age>maxi):
                    maxi = age 
                else: 
                    maxi = maxi           
            return maxi           
        elif (word_opc2[1]=="promedio"):
            for element in archivi:
                prome = float(element.get('promedio'))
                if (prome>maxi):
                    maxi = prome 
                else: 
                    maxi = maxi           
            return maxi 
        else: 
            print("Has seleccionado un atributo invalido")

def min_json(ruta, word_opc2):
    mini= 0   
    with open(ruta) as contenido:
        archivi = json.load(contenido)
        if(word_opc2[1]=="edad"):
            for element in archivi:
                age = int(element.get('edad'))
                if (mini==0):
                    mini = age
                elif (age>mini):
                    mini = mini 
                else: 
                    mini = age          
            return mini           
        elif (word_opc2[1]=="promedio"):
            for element in archivi:
                prome = float(element.get('promedio'))
                if (mini==0):
                    mini = prome
                elif (prome>mini):
                    mini = mini 
                else: 
                    mini = prome           
            return mini 
        else: 
            print("Has seleccionado un atributo invalido")
       
def cargar_alljson(ruta):
    with open(ruta) as contenido:
        archivi = json.load(contenido)
        for element in archivi:
            print(element)

def select_json(ruta, dato_num,atribute):
    with open(ruta) as contenido:
        archivi = json.load(contenido)
        for element in archivi:
            if (atribute == "nombre"):
                encontrado = element.get('nombre')
                if (encontrado==dato_num):#encuentra el registro que quiero buscar 
                    print("Busqueda finalizada, los datos son") 
                    print("nombre: "+element.get('nombre'))
                    print("edad: ",element.get('edad'))
                    print("activo: ",element.get('activo'))
                    print("promedio: ",element.get('promedio'))        
 
            elif (atribute == "edad"):
                encontrado = element.get('edad')
                if (encontrado==dato_num):#encuentra el registro que quiero buscar 
                    print("Busqueda finalizada, los datos son") 
                    print("nombre: "+element.get('nombre'))
                    print("edad: ",element.get('edad'))
                    print("activo: ",element.get('activo'))
                    print("promedio: ",element.get('promedio'))

            elif (atribute == "activo"):
                encontrado = element.get('activo')
                if (encontrado==dato_num):#encuentra el registro que quiero buscar 
                    print("Busqueda finalizada, los datos son") 
                    print("nombre: "+element.get('nombre'))
                    print("edad: ",element.get('edad'))
                    print("activo: ",element.get('activo'))
                    print("promedio: ",element.get('promedio'))
            
            elif (atribute == "promedio"):
                encontrado = element.get('promedio')
                if (encontrado==dato_num):#encuentra el registro que quiero buscar 
                    print("Busqueda finalizada, los datos son") 
                    print("nombre: "+element.get('nombre'))
                    print("edad: ",element.get('edad'))
                    print("activo: ",element.get('activo'))
                    print("promedio: ",element.get('promedio'))

            else: 
                print("Atributo invalido")

    #Validacion de opcion y creacion de switch para saber cual usar, de aqui en adelante se viene lo chido 
if (word_word[0].upper()=="CARGAR"):
    #mostrare los registros de cada archivo para que el usuario pueda ver bien las cosas y escoger segun lo que quiera
    print("Se han cargado los archivos a memoria...")
    #impresion del contenido de los archivos .json
    print("Comandos que puedes utilizar ")
    print("- SELECCIONAR")
    print("- MAXIMO")
    print("- MINIMO")
    print("- SUMA")
    print("- CUENTA")
    print("- REPORTAR") 
    print("Escriba comando que desee: ")
    
    #Aqui empieza lo que quiero hacer con los archivos que genere a memoria
    opc_submenu = input() #lectura de comando 
    word_opc2 = opc_submenu.split() #separo la frase de la linea anterior para trabajar con cada espacio
    for i in range(len(word_opc2)):
        word_opc2[i] = word_opc2[i].replace(",", "")
    #print(word_opc2) #imprimo esto nada mas para saber que hay dentro del arreglo word_opc2
    print("----------------------------------------------------------------------------------")
    if  (word_opc2[0].upper()=="SELECCIONAR" and word_opc2[1]=='*' ):
        print("Escogiste la opcion SELECCIONAR * ")

        m = len(word_opc2)
        
        if m==2:
            print("Se mostraran todo el contenido cargado a memoria")
            for i in range(len(word_word)-1): #solo quiero los nombres de los archivos por eso el -1 para eliminar el nombre del COMANDO
                print("----------------------------"+word_word[i+1]+"------------------------------")
                ruta = '201807307_Practica/'+word_word[i+1]
                cargar_alljson(ruta)
        else:
            atribute = word_opc2[3]
            if (word_opc2[3] == "nombre" or word_opc2[3] == "activo"):

                dato_num = word_opc2[5]+ " "+word_opc2[6]
                dato_num = dato_num.replace('"', "")
            
            elif (word_opc2[3] == "edad"):
                dato_num = int(word_opc2[5])
        
            else: 
                dato_num = float(word_opc2[5])
            for i in range(len(word_word)-1): #solo quiero los nombres de los archivos por eso el -1 para eliminar el nombre del COMANDO
                
                ruta = '201807307_Practica/'+word_word[i+1]
                select_json(ruta, dato_num, atribute)





    elif (word_opc2[0].upper()=="SELECCIONAR"):
        print("Escogiste la opcion SELECCIONAR")
        #guardo la posicion de la palabra DONDE para saber que es lo que quiero buscar 
        for i in range(len(word_opc2)):
            if (word_opc2[i].upper()=="DONDE"):
                x =int(i) #posicion del DONDE
        
        #Imprimo las posiciones y palabra para saber que ondix 
        #print(x)       
        #print(word_opc2[x+3]) #posicion de la palabra o numero que quiero buscar 
        atributo = word_opc2[x+1]
        if (word_opc2[x+1] == "nombre" or word_opc2[x+1] == "activo"):
            #haciendo cambiossssss-------------------------------------------------
            #cadena = word_opc2
            #word_f = word_opc2[x+3]+ " "
            #one_word = word_opc2[x+3]
            #cualquier cosa solo dejo estoooooooo kajajajajaja
            dato_num = word_opc2[x+3]+ " "+word_opc2[x+4]
            dato_num = dato_num.replace('"', "")
            
        elif (word_opc2[x+1] == "edad"):
            dato_num = int(word_opc2[x+3])
        
        else: 
            dato_num = float(word_opc2[x+3])

        
        
        for i in range(len(word_word)-1): #solo quiero los nombres de los archivos por eso el -1 para eliminar el nombre del COMANDO
            
            ruta = '201807307_Practica/'+word_word[i+1]
            cargar_json(ruta, dato_num, atributo, x, word_opc2)
            
        
        

    elif (word_opc2[0].upper()=="MAXIMO"):
        maximo = 0
        maximo2 = 0
        print("Escogiste la opcion MAXIMO")
        for i in range(len(word_word)-1): #solo quiero los nombres de los archivos por eso el -1 para eliminar el nombre del COMANDO
            
            ruta = '201807307_Practica/'+word_word[i+1]
            maximo = (max_json(ruta,word_opc2))
            if (maximo>maximo2):
                maximo2 = maximo
            else:
                maximo2 = maximo2

        print("El resultado maximo de "+word_opc2[1]+" es: ", maximo2)


           


    elif (word_opc2[0].upper()=="MINIMO"):
        minimo = 0 #12
        minimo2 = 0 #33
        print("Escogiste la opcion MINIMO")
        for i in range(len(word_word)-1): #solo quiero los nombres de los archivos por eso el -1 para eliminar el nombre del COMANDO
            
            ruta = '201807307_Practica/'+word_word[i+1]
            minimo = (min_json(ruta,word_opc2))
            if (minimo2==0):
                minimo2 = minimo
               
            elif (minimo>minimo2):
                minimo2 = minimo2
            else:
                minimo2 = minimo

        print("El resultado minimo de "+word_opc2[1]+" es: ", minimo2)

    elif (word_opc2[0].upper()=="SUMA"):
        total2 = 0
        print("Escogiste la opcion SUMA")
        for i in range(len(word_word)-1): #solo quiero los nombres de los archivos por eso el -1 para eliminar el nombre del COMANDO
            
            ruta = '201807307_Practica/'+word_word[i+1]
            total =(suma_json(ruta, word_opc2))
            total2 = total2 + total 

        print("El resultado de la suma de "+word_opc2[1]+" es: ", "{:.2f}".format(total2))
            
        


    elif (word_opc2[0].upper()=="CUENTA"):
        print("Escogiste la opcion CUENTA")
        cuenta = int(len(word_word))
        cuenta2 = (cuenta-1)*2
        print("La cantidad de registros cargados a memoria es: ",cuenta2 )

    elif (word_opc2[0].upper()=="REPORTAR"):
        name = "victor"
        print("Escogiste la opcion REPORTAR")
        f = open('practica.html','w')

        mensaje = """
        <html>
        <center>
        <head>PRACICA LENGUAJES A+ </head>
        <body><p></p>
        <table class="table table-hover">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">nombre</th>
                    <th scope="col">edad</th>
                    <th scope="col">activo</th>
                    <th scope="col">promedio</th>
                </tr>
            </thead>
            
                
            
        </table>
        </body>
        </center>



        </html>"""

        f.write(mensaje)
        f.close()

        webbrowser.open_new_tab('practica.html')

    elif (word_opc2[0].upper()=="SALIR"):
        print("Gracias por probar SimpleQL, chau")

    else: 
        print("Escogiste una opcion incorrecta...")
elif (word_word[0].upper()=="SALIR"):
    print("Gracias por probar SimpleQL, chau")

else: 
    print("Has ingresado un comando invalido")
