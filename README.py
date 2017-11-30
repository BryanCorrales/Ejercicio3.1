# Ejercicio3.1
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
