#Sucesión aritmética
#Clase 3
#código parte a)
print(f'd= {28.14-26.93}')
print(f'd= {26.93-25.72}')

#calcular el término lugar 50 con dos códigos de python diferentes
#sucesión aritmética: 25.72, 26.93, 28.14, ...
n = 1
termino = 25.72
d = 1.21
while n < 50: #mientras n sea menor que 50 hacer lo siguiente
    n = n + 1
    termino = termino + d 
    print(f'a{n} = {round(termino,6)}') #round redondea el numero a 6 decimales

#parte c)
#calculando directamente el término 50
#sucesión aritmética: 25.72, 26.93, 28.14, ...
n = 50
an = 25.72 + (n-1)*1.21
print (f'a{n} = {round(an,6)}') 

n = 1
termino = 25.72
#d) ¿qué lugar ocupa en esta sucesión el término 411.71?
while (round(termino,2) < 411.71):
    n = n + 1
    termino = termino + d
print(f'a{n} = {round(termino,6)}')

