# Ejercicio3.1
<<<<<<< HEAD
<<<<<<< HEAD


def areaCuadrado():
    lado = float(input('Ingrese el lado del cuadrado en m: '))
    areas =  lado**2
    print ("El area es: " , areas)

=======
def areatriangulo():
    altura=int(input("Ingrese la altura: "))
    base=int(input("Ingrese la base: "))
    area=(base+altura)/2
    print("La area del triangulo es: ",area)
>>>>>>> d69c985979b993a19cf0b1c23ec15fe471e4e4e9
=======
def calculaCirculo():
    radio=float(input("Ingrese el radio del circulo: "))
    area=3.1416*radio*radio
    print("el area del circulo es: ",area)

w='x'
while w=='x':
    opcion = input("Escoja la opcion que desea calcular el area: ")
    if opcion=='1':
        calculaCirculo()
    if opcion=='2':
        print("")
    if opcion=='3':
        print("")
    w=input("presione x para continuar cualquier tecla para salir: ")
>>>>>>> 3c5b5b485067ede2549f0f1e63ee6d1132832cc8
