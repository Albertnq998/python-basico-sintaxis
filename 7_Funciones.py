#ALBERT FRAND NINA QUISPE
#Funciones

nombre = ["Juan", "Albert", "Pepito"]
for i in nombre: 
    print("Hola ",i)
    print("Bienvenido al Sistema")
    print("-------------------------")

print("=======================================")
def saludar(nombre):
    print("HOLA", nombre)
    print("Bienvenido al Sistema")
    print("---------------")
saludar("Juan")
saludar("Albert")
saludar("Pepito")

#Funciones con retorno return()
def suma(primer_numero,segundo_numero):
    resultado = primer_numero+segundo_numero
    return (resultado)     
print(suma(2,2))

#Funciones sin retorno
def suma2(primer_numero,segundo_numero):
    resultado = primer_numero + segundo_numero
    print(resultado)
suma2(2,2)
