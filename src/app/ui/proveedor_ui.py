# Modulo de proveedores

from app.utils.tools import *
from app.service.proveedor_service import ProveedorService

class proveedor_ui:
    
    def __init__(self, proveedor_service: ProveedorService):
        self.proveedor_service = proveedor_service

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
                    self._mostrar_proveedores()
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
    
    # =========================
    # MOSTRAR PROVEEDORES
    # =========================
    def _mostrar_proveedores(self):
        salir = False
        while not salir:
            limpiar_pantalla()
            print("\n── Listado de proveedores ──")
            if self._listar_proveedores() is None:
                pausa()
                salir = True
            else:
                print("\n0- Volver al menú")
                if input("Elige una opción: ").strip() == "0":
                    salir = True

    def _listar_proveedores(self):
        proveedores = self.proveedor_service.get_proveedores()
        if not proveedores:
            print("\nNo hay proveedores registrados.")
            return None
        
        print(f"\n{'#':<4} {'Nombre':<25} {'Teléfono':<15} Email")
        print("─" * 65)
        for i, p in enumerate(proveedores, 1):
            print(f"{i:<4} {p.nombre:<25} {p.telefono:<15} {p.email}")

        return proveedores