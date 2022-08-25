#sucesiones
list(range(3,8,2)) #es una lista con los numeros de 3 a 8 de 2 en 2

list(range(3,8)) #es una lista con los numeros de 3 a 8 de 1 en 1

list(range(8)) #es una lista con los numeros de 0 a 7 de 1 en 1


#Uso de ciclos FOR
#for i in range(valor_inicial, valor_final, incremento):
#    b.append(expresion_a_agregar)


#Guía de ejemplo
#--Problema 1--
#parte a)
for n in range(1,6):
    terminoA = 3*n**2+7
    print(f'a({n}) = {terminoA}')
#parte b)
for n in range(16,20):
    terminoB = 3*n**2+7
    print(f'b({n}) = {terminoB}')

#--Problema 2--

#parte a)
for n in range(1,5):
    terminoC = 5*n**3
    print(f'c({n}) = {terminoC}')

#parte b)
for n in range(9,13): #en el valor final se debe dejar uno menos que el valor esperado.
    terminoD = 5*n**3
    print(f'd({n}) = {terminoD}')

#parte c) Indicar si el término 40.000 pertenece a la sucesión (An = 40000)

resultado = round(8000**(1/3),6) #round redondea el numero a 6 decimales
print(resultado)
#resultado = 20.0

termino = 5*n**3 # inicializa el término en n = 1
n = 1 #inicializa el valor de n a 1

while(termino < 40000): #mientras el valor de termino sea menor que 40000 hacer lo siguiente
    n = n + 1 #incrementa el valor de n en 1
    termino = 5*n**3
    print(f'c({n}) = {termino}') 

#se corta el ciclo cuando el valor de termino es mayor que 40000

#Problema 3
#parte a)

for n in range (1,21):
    termino = (-1)**n
    print(f'a({n}) = {termino}') #termino es el resultado de la expresion
#¿Qué se puede afirmar acerca de los términos de esta sucesión?
#El valor absoluto de los términos es 1