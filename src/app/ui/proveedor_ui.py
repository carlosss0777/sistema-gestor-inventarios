# Modulo de proveedores

from app.utils.tools import *

class proveedor_ui:
    
    def menu_proveedor(self):
        while True:
            while True:
                limpiar_pantalla()
                print("\n== GESTIÓN DE PROVEEDORES ==")
                print("1- Registrar proveedor")
                print("2- Mostrar proveedores")
                print("3- Eliminar proveedor")
                print("4- Actualizar datos de un proveedor")
                print("0- Volver al menú principal")
            
                try:
                    opcion = int(input("Elige una opcion: "))
                    break
                except ValueError:
                    print("\nOpción no válida (debe ingresar un número)")
                    print("Intenta nuevamente...")
                    pausaLarga()
            
            match opcion:
                case 1:
                    limpiar_pantalla()
                    pass
                    continue
                
                case 2:
                    limpiar_pantalla()
                    pass
                    continue
                
                case 3:
                    limpiar_pantalla()
                    pass
                    continue
                
                case 4:
                    limpiar_pantalla()
                    pass
                    continue
                
                case 0:
                    print("\nVolviendo al menú principal...\n")
                    pausa()
                    break
                
                case _:
                    print("\nOpción no válida. Intenta nuevamente...")
                    pausa()