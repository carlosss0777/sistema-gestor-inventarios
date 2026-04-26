# Modulo de productos

from app.utils.tools import *

class producto_ui:
    
    def menu_producto(self):
        while True:
            while True:
                limpiar_pantalla()
                print("\n== GESTIÓN DE PRODUCTOS ==")
                print("1- Registrar producto")
                print("2- Mostrar productos")
                print("3- Eliminar producto")
                print("4- Actualizar precio de un producto")
                print("5- Mostrar stock actual")
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
                
                case 5:
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