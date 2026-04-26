# Modulo de movimientos de stock

from app.ui.entradas_salidas_ui import entradas_salidas_ui

from app.utils.tools import *

class movimiento_ui:
    def __init__(self):
        self.esUI = entradas_salidas_ui()
    
    def menu_movimiento(self):
        while True:
            while True:
                limpiar_pantalla()
                print("\n== GESTIÓN DE MOVIMIENTOS ==")
                print("1- Registrar movimiento")
                print("2- Ver historial de movimientos")
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
                    self.esUI.menu_es()
                    continue
                
                case 2:
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