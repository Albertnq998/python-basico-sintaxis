#ALBERT FRAND NINA QUISPE
#Tuplas sets y Diccionarios.

#Tuplas
#Simbolo()
# por default lo ordena 
# inmutables = no se puede hacer cambios 
# te acepta duplicados

tupla = (1,2,1,2,40,10,5,11)
print(tupla)

#Indices
print(tupla[4])

#Sets
# Simbolos {}
# No ordena
#Mutable = si puedes hacer cambios 
# No te acepta duplicados
sets = {1,2,3,1,2,3}
print(sets)

sets.add(4) #agregar dato
print(sets)

sets.remove(3) #remover dato
print(sets)

# Diccionarios
# Simbolo {key:value}
# Si ordena

estudiante = {
    "Nombre":"Albert",
    "Natalidad":"Puno",
    "Edad": 21,
    "Carrera":"Ingenieria"
}
print(estudiante)

print(estudiante["Nombre"])
print(estudiante["Natalidad"])
print(estudiante["Edad"])
print(estudiante["Carrera"])

estudiante["Edad"] = 18
print(estudiante)

#Ciclo for en los diccionarios
for clave, valor in estudiante.items():
    print("Clave:", clave , "Valor:", valor)