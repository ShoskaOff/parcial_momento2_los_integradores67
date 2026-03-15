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
            
            elif opcion == 2:
                calculo()
            
            elif opcion == 3:
                 buscar_por_placa()
            
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
    

#Camilo Celis Hernandez (Modulo de calculo)

def calculo():
    

    if len(gastos) == 0:
        print("No hay gastos registrados.")
        return
    
    total = 0

    for gasto in gastos:
        total = total + gasto["valor"]
        print(f"Placa: {gasto['placa']} | Concepto: {gasto['concepto']} | Valor: {gasto['valor']}")
    print("El gasto total acumulado es: $", total)

#denis camilo (busqueda)

def buscar_por_placa():

    placa_buscar = input("Ingrese la placa a buscar: ")

    encontrado = False

    for gasto in gastos:
        if gasto["placa"] == placa_buscar:
            print("Concepto:", gasto["concepto"])
            print("Valor:", gasto["valor"])
            print("------------------")
            encontrado = True

    if not encontrado:
        print("No se encontraron gastos para esa placa.")
    

 
     
if __name__ == "__main__":
    menu()




