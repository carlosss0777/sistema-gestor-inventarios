# Menu principal del sistema

from app.repository.movimiento_repository import movimiento_repository
from app.repository.proveedor_repository import proveedor_repository
from app.repository.producto_repository import producto_repository
from app.service.movimiento_service import movimiento_service
from app.service.proveedor_service import ProveedorService
from app.service.producto_service import ProductoService
from app.ui.movimiento_ui import movimiento_ui
from app.ui.proveedor_ui import proveedor_ui
from app.ui.producto_ui import producto_ui
from app.utils.tools import *

class menu_principal:
    def __init__(self):
        self.movimiento_repository = movimiento_repository()
        self.producto_repository = producto_repository()
        self.proveedor_repository = proveedor_repository()
        self.proveedor_service  = ProveedorService(self.proveedor_repository)
        self.producto_service  = ProductoService(self.producto_repository, self.proveedor_service.get_all())
        self.movimiento_service = movimiento_service(self.movimiento_repository)

        self.proveedorUI = proveedor_ui(self.proveedor_service, self.producto_service)
        self.productoUI = producto_ui(self.producto_service, self.proveedor_service,self.proveedorUI)
        self.movimientoUI = movimiento_ui(self.movimiento_service, self.producto_service, self.productoUI)
        
    def execute(self):
        while True:
            while True:
                limpiar_pantalla()
            
                print("\n-----------------------------------")
                print("== SISTEMA GESTOR DE INVENTARIOS ==")
                print("-----------------------------------")
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
            