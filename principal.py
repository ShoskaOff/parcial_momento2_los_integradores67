#Samuel (Estructura y Menú Principal):

gastos = []                             # se crea la lista vacia de los gatos

def menu():                             #se crea el menu
        print("===BIENVENIDO=AL=HIMALAYA===")
        while (True):
            print("""
            1) Registrar
            2) Ver calculos
            3) Busqueda
            """)
            opcion = int(input("Seleccione una opcion: "))
            if opcion == 1:
                registrar_gasto()
                break
            elif opcion == 2:
                    print("YEISON")
                    break
            elif opcion == 3:
                 print("DENIS")
                 break
            else:
                print("Opcion invalida")

#Camilo Andres Hernandez (Modulo de registro)

def registrar_gasto():

    placa = input("Ingrese la placa del vehículo: ")
    concepto = input("Ingrese el concepto (Gasolina o Peaje): ")
    valor = float(input("Ingrese el valor del gasto: "))

    flujo = {
     "placa": placa,
     "concepto": concepto,
     "valor": valor
    }

    gastos.append(flujo)

    print("Gasto registrado correctamente.")
    print(gastos)

if __name__ == "__main__":
    menu()




