# Menu principal del sistema

from app.ui.producto_ui import producto_ui
from app.ui.proveedor_ui import proveedor_ui
from app.ui.movimiento_ui import movimiento_ui

from app.utils.tools import *

class menu_principal:
    def __init__(self):
        self.productoUI = producto_ui()
        self.proveedorUI = proveedor_ui()
        self.movimientoUI = movimiento_ui()
        
    def execute(self):
        while True:
            while True:
                limpiar_pantalla()
            
                print("\n== SISTEMA GESTOR DE INVENTARIOS ==")
                print("1- Gestión de productos")
                print("2- Gestión de proveedores")
                print("3- Gestión de movimientos")
                print("0- Salir del sistema")
                
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
                    self.productoUI.menu_producto()
                    continue
                
                case 2:
                    limpiar_pantalla()
                    self.proveedorUI.menu_proveedor()
                    continue
                
                case 3:
                    limpiar_pantalla()
                    self.movimientoUI.menu_movimiento()
                    continue
                
                case 0:
                    print("\nSaliendo del sistema...\n")
                    pausa()
                    break
                
                case _:
                    print("\nOpción no válida. Intenta nuevamente...")
                    pausa()
            