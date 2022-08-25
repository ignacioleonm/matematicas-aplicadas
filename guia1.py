#Resolución de la guía 1 de Matamáticas Aplicadas.
#Autor: Ignacio León Morales
#Fecha: 12 de agosto de 2022

from decimal import Decimal
import math
from math import pi
from math import e


#Ejercicio 1
#. Considere la sucesion (3n^2 +7). Por medio de un codigo Python con ciclos for despliegue en pantalla
#a) Los primeros 5 términos de la sucesion.
for n in range (1,6): # desde n = 1 hasta n = 5
    termino = 3*n**2+7 #termino es el resultado de la expresion
    print(f'a({n}) = {termino}')  #imprime el resultado de la expresion

input() #pausa la ejecución del programa

#b) Los 5 términos que vienen inmediatamente después del decimoquinto término.
for n in range (16,21): # desde n = 16 hasta n = 20
    termino = 3*n**2+7 
    print(f'b({n}) = {termino}')

input()

#Ejercicio 2
#Considere la sucesion (gn) cuyo termino general es 5n^3. Implemente un codigo Python que muestre en pantalla
#a) Los primeros 4 términos de la sucesion.
for n in range (1,5): # desde n = 1 hasta n = 4
    termino = 5*n**3
    print(f'a({n}) = {termino}') 

input()

#b) Los 4 términos que vienen inmediatamente después del octavo término.
for n in range (9,13): # desde n = 9 hasta n = 12
    termino = 5*n**3
    print(f'b({n}) = {termino}')

input()

#c) Indicar si el término 40.000 pertenece a la sucesión (An = 40000)
resultado = round(8000**(1/3),6) #round redondea el numero a 6 decimales
print(resultado)
#resultado = 20.0

termino = 5*n**3 #inicializa el valor de termino a 0
n = 1 #inicializa el valor de n a 1

while(termino < 40000): #mientras el valor de termino sea menor que 40000 hacer lo siguiente
    n = n + 1 #incrementa el valor de n en 1
    termino = 5*n**3
    print(f'c({n}) = {termino}') 

#se corta el ciclo cuando el valor de termino es mayor que 40000

input()

#Ejercicio 3
#Sea la sucesion (kn) definida por su termino general (-1)^n.
#a) Determine los 20 primeros términos de la sucesión.

for n in range (1,21): # desde n = 1 hasta n = 20
    termino = (-1)**n
    print(f'a({n}) = {termino}')

input()

#b) ¿Qué se puede afirmar acerca de los términos de esta sucesión?
#El valor absoluto de los términos es 1
#Cuando n es par el valor de los términos es 1
#Cuando n es impar el valor de los términos es -1

#c) ¿Cuál es el término que se encuentra en la posición 2020?
#el 1, ya que la posición es un número par

#Ejercicio 4
#Sea la sucesion (hn) definida por su término general 6n(-1)^n.
#a) Determine los 100 primeros términos de la sucesión.
for n in range (1,101): # desde n = 1 hasta n = 100
    termino = 6*n*((-1)**n)
    print(f'a({n}) = {termino}')

input()

#b) Basandose en la experiencia con la sucesión de la pregunta anterior, ¿qué características observas en los terminos de esta sucesión?
#Tambiés se van intercalando los valores positivos y negativos
#Se trata de una sucesión no monótona

#Ejercicio 5
#Considere la sucesion An cuyo término general es 1/n.
#a) Determine los términos a10, a100, a1000, a10000 y a100000.
for i in range(1,6): # desde i = 1 hasta i = 5
    n = 10**i #n es el valor de 10 elevado a i
    termino = 1/n #termino es el resultado de la expresion
    print(f'a({n}) = {round(Decimal(termino),5)}')

#b) Sin programar, ni usar calculadora, entre a_9 y a_99, ¿Cuál es mayor?
#Entre ambos términos, a_9 es mayor porque esta sucesión es decreciente.

#Ejercicio 6
#Considere la sucesion b_n de término general (1 + 1/n)^n.
#a) determine los términos b10, b100, b1000, b10000 y b100000.
for i in range (1,6):
    n = 10**i #n es el valor de 10 elevado a i
    termino = (1+1/n)**n
    print(f'b({n}) = {round(Decimal(termino),5)}')
print(f'e = {round(Decimal(e),5)}')

input()

#b) Es creciente
#c) ¿Algún termino es mayor que el número de Euler (e)?
#No, porque "e" se logra con el límite que tiende hasta el infinito de n.
