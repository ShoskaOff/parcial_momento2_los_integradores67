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
                print("ANDRES")
                break
            elif opcion == 2:
                    print("YEISON")
                    break
            elif opcion == 3:
                 print("DENIS")
                 break
            else:
                print("Opcion invalida")



if __name__ == "__main__":
    menu()

