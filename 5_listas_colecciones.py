#Albert Frand Nina Quispe
#Listas
lista = ["Albert","Nina",25,True]
print(lista[0])
#Crear lista de frutas 
frutas = ["Mango","Manzana","Sandia","Mandarina","Maracuya"]
print(frutas[3])

frutas[1] = "Granada"
print(frutas)

for i in frutas:
    print(i)

#Matriz 
matriz = [
    [1,2,3],
    [4,5,6],
    [0,1,0]
]
print(matriz[2][0])

#Lista de Numeros
numeros =[1,2,3,4,5,6,7,8,9,0]
print(numeros[8])
print(numeros[:3])
print(numeros[1:5])
print(numeros[::2])
print(numeros[::-1])
print(numeros[::-2])

#Ciclo For en las listas
for i in numeros:
    print(i*10)

#Metodos en las listas 
print("------------------------------------Metodos")
frutas = ["Mango","Manzana","Sandia","Mandarina","Maracuya"]

#append para agregar un nuevo dato
frutas.append("Ciruela")        
print(frutas)

#insert un dato en un lugar requerido
frutas.insert(2,"Pera")
print(frutas)

#remove borrar dato
frutas.remove("Sandia")
print(frutas)

#pop para obtener o eliminar el ultimo dato 
frutas.pop()
print(frutas)

#sort para ordenar una lista
frutas.sort()
print(frutas)

#reverse para revertir el orden
frutas.reverse()
print(frutas)

#lent para contar los datos
cantidad = len(frutas)
print(cantidad)

#index para encontrar el indice 
indice = frutas.index("Manzana")
print(indice)