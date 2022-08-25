#Clase 4
#20-08-2022
#Sucesiones geometricas
#son de la forma: a_n = a_1 * r^(n-1)

#a)
a = [4,6,9]
print(f'a(3)-a(2)= {round(a[2]/a[1],6)}')
print(f'a(1)-a(0)= {round(a[1]/a[0],6)}')

#c)
n =1
termino = 4
r = 1.5

while n < 60:
    n = n + 1
    termino = termino * r
print(f'a{n} = {round(termino,6)}')


#d) calcular el lugar que ocupa el termino 68,343775
n = 1
termino = 4
r = 1.5
while (round(termino,6) < 68.34375):
    n = n + 1
    termino = termino * r
print(f'a{n} = {round(termino,6)}')

#Ejercicio 14
#razón geométrica = an = 1.25 * 2^(n-1)
#c) calcular el octavo término
n = 1
termino = 1.25
while n < 8:
    n = n + 1
    termino = termino * 2
print(f'a{n} = {round(termino,6)}')

#d) calcular el lugar del termino 20480
termino = 1.25
n = 1
while (round(termino,6) < 20480):
    n = n + 1
    termino = termino * 2
print(f'a{n} = {round(termino,6)}')




