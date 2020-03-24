import re

print("UNIDAD DOS AUTOMATAS")
print("GENERACION DE CODIGO INTERMEDIO")
print("SOLO TRABAJA CON UN VALOR O CARACTER")
print("LA EXPRESION DEBE EMPEZAR CON : X= ")
print("SOLO EXPRESIONES VALIDAS COMO X = 2 + 4 * Y")
print("CASO 1: EJEMPLO  X = 2 + 5 * y") 
print("CASO 2: EJEMPLO  X = a / a + b * b") 
print("CASO 3: EJEMPLO  X= (a+ 2) / 3 + b")
print("CASO 4: EJEMPLO  X = (a+ 2) / (3 - b)")
x=int(input("Seleccione una opcion: "))

# LOS CASOS SON SIN REGEX SOLO CON LISTAS, POR ESO, SE TRABAJA SOLO CON UN DIGITO O UN SOLO
#CARACTER

if x==1:
    #CASO UNO SIN USO DE REGEX, CON LISTAS.
    p = []
    vs = []
    valor =str(input("ingrese la expresion \n"))
    suma = -1
    for i in valor:
        if i != " ":
            p.append(i)
    temporalCero = ""
    for i in p: # MULTIPLICACION O DIVISION
        suma +=1
        if i =="*" or i=="/":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            temporalCero = "_t0 = " + p[suma-1] + " " +  p[suma] + " " + p[suma+1]  #LA LISTA P VAN DESGLOZANDO LA EXPRESION EN PARTES
            p.remove(p[suma]) # SE ELIMINA "*"
            p.remove(p[suma-1]) #SE ELIMINA EL "5"
            p.remove(p[suma-1]) #SE ELIMINA EL "Y"


    temporalUno = ""
    for i in p:
        if i == "+" or i == "-": # SUMA O RESTA 
            if p[-1] == "+" or p[-1]=="-":
                temporalUno = "_t1 ="+ p[2] + " "+ p[3] + " " +"_t0"
                
            else:
                temporalUno = "_t1 = "+ p[3] + " "+ p[2] + " " +"_t0"
    print(temporalCero)
    print(temporalUno)

elif x==2:
    p = []
    vs = []
    valor =str(input("ingrese la expresion \n"))
    suma = -1
    for i in valor:
        if i != " ":
            p.append(i)
    temporalCero = ""
    for i in p: # MULTIPLICACION O DIVISION
        suma +=1
        if i =="*" or i == "/":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            temporalCero = "_t0 = " + p[suma-1] + " " +  p[suma] + " " + p[suma+1] 
        
   
    temporalUno = ""
    for i in p:
        
        if p[7] == "+" or p[7] == "-" : 
            temporalUno = "_t1 ="+ p[6] + " "+ p[7] + " " + p[8]    
        else:    
            temporalUno = "_t1 = "+ p[2] + " "+ p[3] + " " + p[4]

    print(temporalCero)
    print(temporalUno)    
    print("_t2=",temporalCero[0:3],p[5],temporalUno[0:3])
    
elif x==3:
    p = []
    vs = []
    valor =str(input("ingrese la expresion \n"))
    suma = -1
    for i in valor:
        if i != " ":
            p.append(i)
    temporalCero = ""
    for i in p: 
        suma +=1
        if i =="(" or i == ")":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            temporalCero = "_t0 = " + p[suma-4] + " " +  p[suma-3] + " " + p[suma-2] + " " + p[suma-1] + " " + p[suma]
    temporalUno = ""
    for i in p:
        if i == "*" or i == "/":
            if p[2] == "(" :
                temporalUno = "_t1 ="+ " _t0 " + p[suma-3] + " " +  p[suma-2] + " " 
            else:
                temporalUno = "_t1 = " + p[suma-6] + " " +  p[suma-5] + " " +  "_t0"
    temporalDos = ""
    for i in p:
        if i == "+" or i == "-": 
            if p[2] == "(" :
                temporalDos = "_t2="+ " _t1 " + p[suma-1] + " " +  p[suma] + " " 
            else:
                temporalDos = "_t2 = " + p[suma-8] + " " +  p[suma-7] + " " +  "_t1"
    print(temporalCero)
    print(temporalUno)
    print(temporalDos)
   
   



