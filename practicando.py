#Práctica para Control 1

#Ejemplo 1
#arreglo
#recorrer arreglo estático 3, 9, 12, 15, 18

n = 0
b = [3, 9, 12, 15, 18]
for i in range(len(b)):
    n = n + 1
    print(f'b({n}) = {b[i]}')

#generar los cuatro primeros términos de la sucesión 3n
a = []
n = 0
for i in range(4):
    n = n + 1
    a.append(3*n)
    print(f'a({n}) = {a[i]}')

#calcular los términos desde b10 hasta b15 de la sucesión bn = 5 * 0.92*n
b = []
termino = 0
for i in range(6): #i asume valores enteros desde 0 hasta 5.
    n = i + 10
    termino = 5*0.92*n
    print(f'b({n}) = {termino}')

#Ejercicio 6
#Considere la sucesion b_n de término general (1 + 1/n)^n.
#a) determine los términos b10, b100, b1000, b10000 y b100000.

n = 0
termino = 0
for i in range (1,6):
    n = 10**i
    termino = (1 + 1/n)**n
    print(f'b({n}) = {round(termino,6)}')




