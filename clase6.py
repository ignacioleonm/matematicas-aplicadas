#verificando tipo de sucesión


a=[900,810,729]

print(f'a(3)-a(2)={a[2]-a[1]}')
print(f'a(2)-a(1)={a[1]-a[0]}')
print()
print(f'a(3)/a(2)={a[2]/a[1]}')
print(f'a(2)/a(1)={a[1]/a[0]}') # es geométrica


#parte c)
suma1 = 0
for i in range(1,31):
    termino = 900*0.9**(i-1)
    suma1 = suma1 + termino
print(suma1)

#parte d)
#FORMA 1
suma1 = 0
for i in range(1,31):
    termino = 900*0.9**(i-1)
    suma1 = suma1 + termino
print(suma1)

suma2 = 0
for i in range(1,25):
    termino = 900*0.9**(i-1)
    suma2 = suma2 + termino
print(suma2)

print(suma1 - suma2)

#FORMA 2
suma = 0
for i in range(25,31):
    termino = 900*0.9**(i-1)
    suma = suma + termino
print(round(suma,2))


#parte e)
suma = 0
for i in range(13,25):
    termino = 900*0.9**(i-1)
    suma = suma + termino
print(round(suma,2))    

suma = 0
for i in range(1,31):
    termino = 900*0.9**(i-1)
    suma = suma + termino
print(round(suma,2)) 




