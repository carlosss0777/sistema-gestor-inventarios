# Modulo de registro movimientos de stock

from app.utils.tools import *

class entradas_salidas_ui:
    
    def menu_es(self):
        while True:
            while True:
                limpiar_pantalla()
                print("\n== REGISTRO DE ENTRADAS/SALIDAS ==")
                print("1- Registrar entrada de stock")
                print("2- Registrar salida de stock")
                print("0- Cancelar registro")
            
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
                    continue
                
                case 2:
                    limpiar_pantalla()
                    continue
                
                case 0:
                    print("\nCancelando registro...\n")
                    pausa()
                    break
                
                case _:
                    print("\nOpción no válida. Intenta nuevamente...")
                    pausa()