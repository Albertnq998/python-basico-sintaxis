#ALBERT FRAND NINA QUISPE
#Operadores en Python
#1. Operadores Aritmeticos
suma = 5+5
resta = 10-6
multiplicacion = 5*5
division = 10/2
modulo = 10%2
exponentes = 10**2 

print('El resultado de la suma es:' ,suma)
print('El resultado de la resta es:' ,resta)
print('El resultado de la multiplicacion es:' ,multiplicacion)
print('El resultado de la division es:' ,division)
print('El resultado del modulo:' ,modulo)
print('El resultado del exponente es:' ,exponentes)

#2. Operadores de Comparacion

print(5 == 5) #Igual a
print(5 != 5) #Diferente de
print(10 > 5) #Mayor que
print(10 < 5) #Menor que
print(10 >= 5) #Mayor igual que
print(10 <= 5) #Menor igual que

#3. Operadores Logicos
v = True
f = False
 #3.1. and (y)
print('----------------------AND')
print(v and v)
print(v and f)
print(f and v)
print(f and f)
 #3.2 or (o)
print('------------------OR')
print(v or v)
print(v or f)
print(f or v)
print(f or f)
 #3.3 not(negación)
print('------------------NOT')
print(not v)
print(not f)

#4. Operadores de asignacion
#Suma y asigna (+=)
print("---------------------------------- +=")
edad = 20
edad += 5
print(edad)

#Resta y asigna (-=)
print("----------------------------------- -=")
saldo = 100
saldo -= 50
print(saldo) 

#Multiplica y asigna (*=)
print("------------------  *=")
precio = 30
precio *= 5
print(precio)

#Divide y asigna (/=)
print("----------------------- /=")
total = 200
total /= 2 
print(total)