import re

print("UNIDAD DOS AUTOMATAS")
print("GENERACION DE CODIGO INTERMEDIO")
print("CASO 1: EJEMPLO  X = 2 + 5 * y") #EXPRESIONES INVALIDAS X= 2 - 5 + Y ó X = 2 * 5 / Y
print("CASO 2: EJEMPLO  X = a / a + b * b") #EXPRESIONES INVALIDAS SERIAN LAS QUE NO SEAN DE MULTIPLICACION
print("CASO 3: EJEMPLO  X= (a+ 2) / 3 + b")
print("CASO 4: EJEMPLO  X = (a+ 2) / (3 - b)")
x=int(input("Seleccione una opcion"))

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
            #QUE P = [X,=,2,+]

    temporalUno = ""
    for i in p:
        if i == "+" or i == "-": # SUMA O RESTA 
            if p[-1] == "+" or "-":
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
            temporalCero = "_t0 = " + p[suma-1] + " " +  p[suma] + " " + p[suma+1]  #LA LISTA P VAN DESGLOZANDO LA EXPRESION EN PARTES
            #QUE P = [X,=,a,a,+,b,-,b]
        
    print(p)
   
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
    for i in p: # MULTIPLICACION O DIVISION
        suma +=1
        if i =="(" or i == ")":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            temporalCero = "_t0 = " + p[suma-4] + " " +  p[suma-3] + " " + p[suma-2] + " " + p[suma-1] + " " + p[suma]
            #LA LISTA P VAN DESGLOZANDO LA EXPRESION EN PARTES
    temporalUno = ""
    print(p[2])
    for i in p:
        if i == "*" or i == "/": # SUMA O RESTA 
            if p[2] == "(" :
                print("hola")
                temporalUno = "_t1 ="+ " _t0 " + p[suma-3] + " " +  p[suma-2] + " " 
            else:
                print("mundo")
                temporalUno = "_t1 =" + p[suma-6] + " " +  p[suma-5] + " " +  "_t0"
    print(p)
    print(temporalCero)
    print(temporalUno)
   
   



