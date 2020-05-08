#1
#E: Lista
#S: Cada uno de los valores de la lista, junto a su posición
#R: Solo listas, no se permiten listas vacías

def print_values(lista):
    if (isinstance (lista,list)):
        if (lista!=[]):
            return print_aux(lista,0)
        else:
            print ("La lista está vacía")
    else:
        print ("Por favor introduzca una lista")

def print_aux(lista,cont):
    if (lista==[]):
        return
    else:
        print ("El valor en la posición",cont,"es",lista[0])
        return print_aux(lista[1:],cont+1)


#2
#E: La acción que quiere hacer el usuario con la lista a crear
#S: La lista creada según el usuario especifica
#R: Solo se pueden agregar números a la lista

def formar_lista():
    return lista_aux([])

def lista_aux(lista):
    accion=(input("introduzca el elemento: "))
    if (accion=="actual"):
        if (lista!=[]):
            print ("Su lista actual es:",lista)
            return lista_aux(lista)
        else:
            print ("Aún no hay elementos en la lista")
            return lista_aux(lista)
    elif(accion=="fin"):
        print ("La lista final es:",lista)
    else:
        try:
            a=int(accion)
            lista=lista+[a]
            return lista_aux(lista)
        except:
            print ("Valor inválido, por favor intente de nuevo")
            return lista_aux(lista)
            
#3
#E: Dos listas
#S: Nueva lista formada por la suma de los dígitos de los indices de las listas
#R: Solo listas del mismo tamaño, los elementos de la lista deben de ser números

def sum_lists(l1,l2):
    if (isinstance(l1 and l2,list)):
        if (validar(l1) and validar(l2)):
            if (largo(l1) == largo(l2)):
                return sum_aux(l1,l2,[])
            else:
                print ("Las listas deben de tener el mismo tamaño")
        else:
            print ("Los valores de las listas deben de ser int o float")
    else:
        print ("Uno o más de los elementos ingresados no son listas")

def validar(l):
    if (l==[]):
        return True
    else:
        if(isinstance(l[0],int) or isinstance(l[0],float)):
            return validar(l[1:])
        else:
            return False

def largo(lista):
    if (lista==[]):
        return 0
    else:
        return 1+largo(lista[1:])

def sum_aux(l1,l2,new):
    if (l1==[]):
        return new
    else:
        return sum_aux(l1[1:],l2[1:],new+[(l1[0]+l2[0])])

#4
#E: Lista
#S: Promedio de los números de la lista
#R: Solo números en la lista

def average(lista):
    if (isinstance(lista,list)):
        if (validar(lista)):
            return aver_aux(lista,largo(lista),0)
        else:
            print ("error en los elementos de la lista")
    else:
        print ("No se ha ingresado una lista")

def aver_aux(lista,lar,cont):
    if (lista==[]):
        return cont/lar
    else:
        return aver_aux(lista[1:],lar,cont+lista[0])

#5
#E: Lista, número de veces que se desea que un elemento se repita en la misma
#S: Lista con los elementos repetidos
#R: Solo enteros en el numero de repeticiones, listas en la lista a analizar, y solo valores que existan en la lista

def repetir (numero, elemento, lista):
    if (isinstance(numero,int) and numero>0):
        if (isinstance(lista,list)):
            apa=apariciones(elemento,lista,0)
            if (isinstance (apa,int)):
                return rep_aux(numero,lista,apa,lista[0:apa])
            else:
                print ("El elemento",elemento,"no está en la lista")
        else:
            print ("El elemento",lista,"no es una lista")
    else:
        print("La cantidad de repeticiones debe ser un número entero mayor a 0")

def apariciones(x,lista,cont):
    if (lista==[]):
        return "Inválido"
    else:
        if (lista[0]==x):
            return cont
        else:
            return apariciones(x,lista[1:],cont+1)

def rep_aux(cant,lista,pos,new):
    if (cant==1):
        return new+lista[pos:]
    else:
        return rep_aux(cant-1,lista,pos,new+[lista[pos]])
    
    
#6
#E: Lista, y operación a realizar
#S: El valor resultante de la operación indicada
#R: Solo se admiten listas y las operaciones: suma, multiplicacion y promedio

def calculadora(lista,operacion):
    if (isinstance(lista,list)):
        if (operacion=="suma"):
            return suma (lista)
        elif (operacion=="promedio"):
            return average(lista)
        elif (operacion=="multiplicación" or operacion=="multiplicacion"):
            return multiplicar(lista)
        else:
            print ("Operación inválida")
    else:
        print ("El valor ingresado debe de ser una lista")

def suma(lista):
    if (validar(lista)):
        return suma_aux(lista)
    else:
        print ("Error al sumar: al menos uno de los valores de la lista no es un número")

def suma_aux(lista):
    if (lista==[]):
        return 0
    else:
        return lista[0]+suma_aux(lista[1:])
def multiplicar(lista):
    if (validar(lista)):
        return multip_aux(lista)
    else:
        print ("Error al multiplicar: al menos uno de los valores de la lista no es un número")

def multip_aux(lista):
    if (lista==[]):
        return 1
    else:
        return lista[0]*multip_aux(lista[1:])

#7
#E: Dos listas
#S: La segunda lista eliminando lo anterior a la aparición de la primera lista (si es que aparece)
#R: Solo listas, la primera lista debe estar contenida en la segunda, las listas no pueden estar vacías

def subsecuencia(lista1,lista2):
    if (isinstance(lista1 and lista2,list)):
        if (lista1!=[] and lista2!=[]):
            return sub_aux(lista1,lista2)
        else:
            print ("Las listas no pueden estar vacías")
    else:
        print ("Al menos una de las entradas ingresadas no es una lista")

def sub_aux(l1,l2):
    if (l2==[]):
        return False
    else:
        if (l2[0]==l1[0]):
            return sub_2(l1[1:],l2[1:],l1[1:],l2[1:])
        else:
            return sub_aux(l1,l2[1:])

def sub_2(l1,l2,l1reserv,l2reserv):
    if (l2==[]):
        return sub_aux(l1reserv,l2reserv[1:])
    elif (l1==[]):
        return l2
    else:
        if (l2[0]==l1[0]):
            return sub_2(l1[1:],l2[1:],l1reserv,l2reserv)
        else:
            return sub_aux(l1,l2)



#8
#E: Una lista y un indice
#S: Lista formada por: la suma de los elementos hasta el indice, y las suma de los elementos del indice hasta el final
#R: Solo listas con números enteros

def suma_elementos(lista,indice):
    if (isinstance(lista,list) and isinstance(indice,int)):
        if (indice<largo(lista)):
            if (verifint(lista)):
                return suma_elementos_aux(lista,indice)
            else:
                print ("Al menos un elemento de la lista no es un número entero")
        else:
            print ("Indice inválido")
    else:
        print ("Valor inválido")

def largo(lista):
    if (lista==[]):
        return 0
    else:
        return 1+largo(lista[1:])

def verifint(lista):
    if (lista==[]):
        return True
    else:
        if (isinstance(lista[0],int)):
            return verifint(lista[1:])
        else:
            return False

def suma_elementos_aux(lista,indice):
    return [suma1(lista,indice-1)]+[suma2(lista[indice:])]

def suma1(lista,indice):
    if (indice<0):
        return 0
    else:
        return lista[indice]+suma1(lista,indice-1)


def suma2(lista):
    if (lista==[]):
        return 0
    else:
        return lista[0]+suma2(lista[1:])




#9
#E: Dos listas
#S: Lista formada por elementos de la primera que no están en la segunda
#R: Solo listas

def exclusion(lista1,lista2):
    if (isinstance(lista1,list) and isinstance(lista2,list)):
        return exclusion_aux(lista1,lista2,[])
    else:
        print ("Valor inválido")

def exclusion_aux(lista1,lista2,res):
    if (lista1==[]):
        return res
    else:
        if(presencia(lista1[0],lista2)):
            return exclusion_aux(lista1[1:],lista2,res)
        else:
            return exclusion_aux(lista1[1:],lista2,res+[lista1[0]])

def presencia(n,lista):
    if(lista==[]):
        return False
    else:
        if (lista[0]==n):
            return True
        else:
            return presencia(n,lista[1:])


#10
#E: Lista con números
#S: Lista con la cantidad de veces que el número de indice aparece en la lista
#R: Solo listas (su contenido es asumido)

def frecuencias(lista):
    if (isinstance(lista,list)):
        return frecuencias_aux(lista,0,[])
    else:
        print ("Valor inválido")

def frecuencias_aux(lista,cont,res):
    if (cont==largo(lista)):
        return res
    else:
        return frecuencias_aux(lista,cont+1,res+[contarapa(cont,lista)])

def contarapa(valor,lista):
    if (lista==[]):
        return 0
    else:
        if (lista[0]==valor):
            return 1+contarapa(valor,lista[1:])
        else:
            return contarapa(valor,lista[1:])


#11
#E: Lista de listas
#S: Lista de mayor profundidad, o mensaje en caso de empate
#R: Solo listas de listas

def profundidad(lista):
    if (isinstance(lista,list)):
        if (listadelista(lista)):
            return profundidad_aux(lista,[0,0],0)
        else:
            print ("La lista debe de tener listas dentro")
    else:
        print ("Valor inválido")

def listadelista(lista):
    if (lista==[]):
        return True
    else:
        if (isinstance(lista[0],list)):
            return lista[1:]
        else:
            return False

def profundidad_aux(lista,profundo,igualdad):
    if (lista==[]):
        if (igualdad==1):
            print ("Hay empate")
        else:
            return profundo[1]
    else:
        prof=(profundidad2(lista[0],0,0,lista[0]))
        if (prof[0]==profundo[0]):
            igualdad=1
        if (prof[0]>profundo[0]):
            profundo=prof
            igualdad=0
        return profundidad_aux(lista[1:],profundo,igualdad)

def profundidad2(lista,cont,mayor,uso):
    if (lista==[]):
        if (cont>mayor):
            mayor=cont
        return [mayor]+[uso]
    else:
        if(isinstance(lista[0],list)):
            return profundidad2(lista[1:],profundidad2(lista[0],cont+1,mayor,uso)[0],mayor,uso)
        else:
            cont=cont+1
            if (cont>mayor):
                mayor=cont
            return profundidad2(lista[1:],0,mayor,uso)

#12
#Aplanar
#E: Lista
#S: Lista aplanada
#R: Solo listas

def aplanar (lista):
    if (isinstance(lista,list)):
        if (lista!=[]):
            return aplanar_aux(lista,[])
        else:
            return []
    else:
        print ("Valor inválido")

def aplanar_aux(lista,res):
    if(lista==[]):
        return res
    else:
        if (isinstance(lista[0],list)):
            return agregar(lista[0],res,lista)
        else:
            return aplanar_aux(lista[1:],res+[lista[0]])
        
def agregar(n,res,lista):
    if (n==[]):
        if (lista==[]):
            return aplanar_aux(lista,res)
        else:
            return aplanar_aux(lista[1:],res)
    else:
        if(isinstance(n[0],list)):
            return agregar(n[1:],agregar(n[0],res,[]),lista)
        else:
            return agregar (n[1:],res+[n[0]],lista)


