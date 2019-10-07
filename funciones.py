import numpy as np  
a= np.zeros((3,12)) 
for i in range(len(a)): 

    for j in range(len(a[i])): 

        if(i == 0): 

            dep = "Santander" 

        elif(i == 1): 

            dep  = "Antioquia" 

        else: 

            dep = "Boyacá" 

        a[i][j] = int(input("Ingrese la temperatura del departamento "+ str(dep)+":")) 
tempSan = 0 
tempAnt = 0 
tempBoy = 0 
tempMaxSan = 0 
tempMaxAnt = 0 
tempMaxBoy = 0 
mesSan=0
mesAnt=0
mesBoy=0
def funcion_diccionario(x):
    diccionario= {0:"Enero",1:"febrero",2:"Marzo",3:"Abril",4:"mayo",5:"Junio",6:"Julio",7:"Agosto",8:"Septiembre",9:"Octubre",10:"Noviembre",11:"Diciembre"}
    mes=diccionario[x]
    return mes
for i in range(3): 

    for j in range(12): 

        if(i==0): 

            tempSan += a[i][j] 
            if a[i][j]>tempMaxSan:
                tempMaxSan=a[i][j]   
                mesSan=funcion_diccionario(j)
                
            if j ==11:
                print("la temperatura maxima de santander es: ",tempMaxSan, " en el mes de ", mesSan)
                
            
        elif(i==1): 

            tempAnt += a[i][j] 
            if a[i][j]>tempMaxAnt:
                tempMaxAnt= a[i][j] 
                mesAnt=funcion_diccionario(j)
             
            if j ==11:
                print("la temperatra mayor de la antioquia es: ", tempMaxAnt, " en el mes de ", mesAnt)
                

        else: 

            tempBoy += a[i][j] 
            if a[i][j]>tempMaxAnt:
                tempMaxBoy=a[i][j] 
                mesBoy=funcion_diccionario(j)
            
            if j == 11:
                print("la temperatura maxima de boyaca es: ", tempMaxBoy, " en el mes de ", mesBoy)
                
