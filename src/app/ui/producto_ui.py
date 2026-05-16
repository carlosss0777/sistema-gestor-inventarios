from app.utils.tools import *
from app.service.producto_service import ProductoService
from app.service.proveedor_service import ProveedorService

class producto_ui:
    
    def __init__(self, producto_service: ProductoService, proveedor_service: ProveedorService):
        self.producto_service = producto_service
        self.proveedor_service = proveedor_service

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
                    self._mostrar_productos()
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

    # =========================
    # MOSTRAR PRODUCTOS
    # =========================
    def _mostrar_productos(self):
        salir = False
        while not salir:
            limpiar_pantalla()
            print("\n── Listado de productos ──")
            if self._listar_productos() is None:
                pausa()
                salir = True
            else:
                print("\n0- Volver al menú")
                if input("Elige una opción: ").strip() == "0":
                    salir = True
    
    def _listar_productos(self):
        productos = self.producto_service.get_productos()
        if not productos:
            print("\nNo hay productos registrados.")
            return None
        
        print(f"\n{'#':<4} {'Nombre':<20} {'Stock':>6} {'Precio':>10} {'Proveedor':<20} Descripción")
        print("─" * 80)
        for i, p in enumerate(productos, 1):
            nombre_prov = p.proveedor.nombre if p.proveedor else "Sin proveedor"
            print(f"{i:<4} {p.nombre:<20} {p.stock:>6} {p.precio:>10.2f} {nombre_prov:<20} {p.descripcion}")

        return productos