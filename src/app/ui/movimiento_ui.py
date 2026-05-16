# Modulo de movimientos de stock

from app.service.movimiento_service import movimiento_service
from app.ui.entradas_salidas_ui import entradas_salidas_ui
from app.service.producto_service import ProductoService
from app.ui.producto_ui import producto_ui
from app.utils.tablas import *
from app.utils.tools import *

class movimiento_ui:
    def __init__(self, movimiento_service: movimiento_service, producto_service: ProductoService, producto_ui: producto_ui):
        self.movimiento_service = movimiento_service
        self.producto_service = producto_service
        self.producto_ui = producto_ui
        self.esUI = entradas_salidas_ui(self.movimiento_service, self.producto_service, self.producto_ui)
    
    def menu_movimiento(self):
        while True:
            while True:
                limpiar_pantalla()
                print("\n----------------------------")
                print("== GESTIÓN DE MOVIMIENTOS ==")
                print("----------------------------")
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
                
                case 2:
                    limpiar_pantalla()
                    self._mostrar_historial()
                
                case 0:
                    print("\nVolviendo al menú principal...\n")
                    pausa()
                    break
                
                case _:
                    print("\nOpción no válida. Intenta nuevamente...")
                    pausa()
                    
    def _mostrar_historial(self):
        movimientos = self.movimiento_service.get_movimientos()
        
        if not movimientos:
            print("\n------------------------------------------------------------")
            print("         No hay movimientos registrados.")
            print("------------------------------------------------------------")
            
            detener()
            return
        
        else:
            limpiar_pantalla
            
            print("\n------------------------------------------------------------")
            print("             -- MOVIMIENTOS REGISTRADOS --")
            print("------------------------------------------------------------")
            tabla = tabla_movimientos(movimientos)
            print(tabla)
            
            detener()