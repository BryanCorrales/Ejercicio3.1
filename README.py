# Ejercicio3.1
def areaCuadrado():
    lado = float(input('Ingrese el lado del cuadrado en m: '))
    areas =  lado**2
    print ("El area es: " , areas)
def areatriangulo():
    altura=int(input("Ingrese la altura: "))
    base=int(input("Ingrese la base: "))
    area=(base+altura)/2
    print("La area del triangulo es: ",area)
def calculaCirculo():
    radio=float(input("Ingrese el radio del circulo: "))
    area=3.1416*radio*radio
    print("el area del circulo es: ",area)
print("Areas de Figuras")
print ("1 circulo")
print ("2 cuadrado")
print("3 triangulo")
w='x'
while w=='x':
    opcion = input("Escoja la opcion que desea calcular el area: ")
    if opcion=='1':
        calculaCirculo()
    if opcion=='2':
        areaCuadrado()
    if opcion=='3':
        areatriangulo()
    w=input("presione x para continuar cualquier tecla para salir: ")

