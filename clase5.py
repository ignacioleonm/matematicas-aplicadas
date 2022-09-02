#Clase 4
#Sumatorias
#27-08-2022

#Ejercicio 2:
#parte a) (con listas)
a = []

for i in range(1,13):
    a.append(3*i**2+7)

print(a) #imprime la lista
print(sum(a)) #imprime la sumatoria de la lista, desde el término 1 hasta el 12

#parte a) (sin listas)
suma = 0
for i in range(1,13):
    suma = suma + (3*i**2+7)
    
print(suma)

#parte b) (sin lista)
suma = 0
for i in range(13,25):
    suma = suma + (3*i**2+7)

print(suma)


#Solución Problema 4
suma = 0
for i in range(1,4):
    suma = suma + (-1.5*i**2 + 6*i)
    total = suma / 3

print(total)


#Problema 6
a= [50,66,82]
print(f'a(3)-a(2)={a[2]-a[1]}')
print(f'a(2)-a(1)={a[1]-a[0]}')
print()





