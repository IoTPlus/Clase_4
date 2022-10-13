#CUARTA CLASE
## Listas: Es una colección de valores de cualquier tipo, por lo general contiene elementos del mismo tipo.
# Es mutable, i.e. Se puede modificar agregando, eliminando o actualizando valores.

#1 Crear listas:
lista_1 = []
lista_2 = list()
lista_3 = [1,2,[3,4],'hola']
valores = [1,2,3,4]

#2 Agregar elementos a una lista:
valores.append(10)
valores.append(5)
valores.append(-3)

#2.1 Agregar elementos a una lista usando range:
valores = list(range(5))

list(range(3,8))

list(range(5,1,-1))

#3 Acceder a elementos de una lista:
nombres = ['Juan', 'Pedro', 'Ana', 'Martin']
nombres[0]

nombres[-1]
nombres.index('Pedro')
len(nombres)

nombres[0]='Juanito'


#4 Concatenación:
a=[1,2,3,4]
b=[5,6,7,8]

c=a+b
print(c)
d=b+a
print(d)

#5 Repetir listas:
a=[1,4,6]
b = a*3

print(b)

#6 Verificar si un elemento esta en la lista:
a= [1,2,3,4]
10 not in a

6 in a

#7 Eliminar un elemento de la lista:
nombres = ['Juan', 'Pedro', 'Ana', 'Martin']
del nombres[2]
nombres

#8 Funciones sobre edades:
edades= [10, 3, 18, 32]

len(edades)
sum(edades)
min(edades)
max(edades)

#9 Metodos en listas:
#9.1 Agregar elemento en posición especifica:
valores.insert(i,x)  # Agrega el elemento x a la lista valores en la posicion i
#9.2 Contar cantidad de veces que aparece el elemento x en la lista l:
l.count(x)
#9.3 Obtener indice del elemento x en la lista l:
l.index(x)
#9.4 Remover elemento x de la lista l:
l.remove(x)
#9.5 Invertir una lista:
l.reverse(x)
#9.6 Ordenar una lista:
l.sort()

#10.1 Recorrido de listas usando while:
nombres = ['Juan', 'Pedro', 'Ana', 'Martin']
edades= [10, 3, 18, 32]

i=0
while i < len(nombres):
    print(nombres[i])
    i+=1

i=0
while i < len(nombres):
    print(nombres[i], 'tiene', edades[i], 'años')
    i+=1

#10.2 Recorrer lista usando for:
for nombre in nombres:
    print(nombre)

for i in range(len(nombres)):
    print(nombres[i], 'tiene', edades[i], 'años')

#11 Operador slice:
lista=[1,3,5,7,9,11,13]

print(lista[3:5])
print(lista[3:])
print(lista[:3])
print(lista[::-1])

#12 Computar desviación estandar cuyo parametro sea una lista de valores entregados en argumento:
def desviacion_estandar(list):
    promedio = sum(list) / len(list)
    i=0
    diff=list
    diff_sq=list
    while i < len(list):
        diff[i] = list[i] - promedio
        diff_sq[i] = diff[i] ** 2
        i+=1
    variance = sum(diff_sq) / (len(diff_sq) - 1)
    dev_st = pow(variance, 0.5)
    return dev_st

print(desviacion_estandar([4.0,1.0,11.0,13.0,2.0,7.0]))

#13 Computar producto interno de dos listas entregadas en argumento:
a=[5,1,6]
b=[1,-2,8]

def producto_interno(a,b):
    i = 0
    sum = 0
    while i < len(a):
        sum = sum + a[i]*b[i]
        i+=1
    return sum

a=[7,1,4,9,8]
b=list(range(5))
print(producto_interno(a,b))


#14 Si el producto interno entre las dos listas es cero se dice que son ortogonales.
#Primera opción:
def son_ortogonales(a,b):
    if producto_interno(a, b) == 0:
        return True
    else:
        return False

#Segunda opción:
def son_ortogonales(a,b):
    return producto_interno(a,b) == 0


print(son_ortogonales([2,1],[3,-6]))


##TUPLAS
#Se diferencian de las listas porque son inmutables (No pueden ser modificadas luego de su creación), recomendado
#para agrupar valores que por su naturaleza deben ir juntos.

autos = [
    ('Subaru', 'Forester', 2019),
    ('Kia', 'Sportage', 2020),
    ('Hyundai', 'Santa fe', 2018),
    ('Chevrolet', 'Captiva', 2010),
    ('Renault', 'Duster', 2020)
]

#15.1 Desempaqueado de tuplas llamando a cada elemento:
for marca, modelo, año in autos:
    print(modelo + " del año: " + str(año))

#15.2 Desempaquetado de tuplas usando el largo de esta:
for i in range(len(autos)):
    print(autos[i][1] + " del año : " + str(autos[i][2]))

#16 Dos tuplas son iguales si tienen la misma cantidad de elementos y estos son identicos:
(1,2,3) == (1,2,3)
#17 Para saber si una tupla es mayor que otra se comparan elementos en la primera posición que sean distintos:
(1,2) < (1,2,4)

#18 Discutir y resolver los siguientes sin usar la pc:
a=(2,10,1991)
b=(25,12,1990)
c=("Donald", True, b)
x, y = ((27,3),9)
z, w = x
v = (x,a)

a < b
y + w
x + a
len(v)
v[1][1]
c[0]
a + b[1:5]
(a + b)[1:5]
str(a[2]) + str(b[2])
str(a[2 + b[2]])
str((a + b)[2])
str(a + b)[2][0]

#19.1 Producto mas caro:

