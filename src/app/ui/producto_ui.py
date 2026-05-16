from app.utils.tools import *
from app.service.producto_service import ProductoService
from app.service.proveedor_service import ProveedorService
from app.ui.proveedor_ui import proveedor_ui

class producto_ui:
    
    def __init__(self, producto_service: ProductoService, proveedor_service: ProveedorService, proveedor_ui:proveedor_ui):
        self.producto_service  = producto_service
        self.proveedor_service = proveedor_service
        self.proveedor_ui      = proveedor_ui

    def menu_producto(self):
        while True:
            while True:
                limpiar_pantalla()
                print("\n== GESTIÓN DE PRODUCTOS ==")
                print("1- Registrar producto")
                print("2- Mostrar productos")
                print("3- Eliminar producto")
                print("4- Actualizar producto")
                print("5- Mostrar stock actual")
                print("6- Actualizar precio de un producto")
                print("7- Actualizar stock de un producto")
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
                    self._registrar_producto()
                case 2:
                    self._mostrar_productos()
                case 3:
                    self._eliminar_productos()
                case 4:
                    self._actualizar_producto()
                case 5:
                    self._mostrar_stock()
                case 6:
                    self._actualizar_precio_producto()
                case 7:
                    self._actualizar_stock_producto()
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
    
    # =========================
    # REGISTRAR PRODUCTOS
    # =========================
    def _registrar_producto(self):
        limpiar_pantalla()
        print("\n── Registrar producto ──")
        nombre      = self._pedir_nombre()
        stock       = self._pedir_stock()
        precio      = self._pedir_precio()
        descripcion = self._pedir_descripcion()
        proveedor   = self._pedir_proveedor()
        
        if proveedor == "cancelar":
            print("\nRegistro cancelado.")
            pausa()
            return

        self.producto_service.registrar_producto(nombre, stock, proveedor, precio, descripcion)
        print("\nProducto registrado exitosamente.")
        pausa()
    
    # =========================
    # ACTUALIZAR PRODUCTOS
    # =========================
    def _actualizar_producto(self):
        limpiar_pantalla()
        print("\n── Actualizar producto ──")
        producto = self._seleccionar_producto("Selecciona el número a actualizar (0 para cancelar): ")
        if producto is None:
            return
        print(f"\nEditando: {producto.nombre} | Deja en blanco para conservar el valor actual.\n")
        producto.nombre      = self._pedir_nombre(producto.nombre)
        producto.stock       = self._pedir_stock(producto.stock)
        producto.precio      = self._pedir_precio(producto.precio)
        producto.descripcion = self._pedir_descripcion(producto.descripcion)
        producto.proveedor   = self._pedir_proveedor(producto.proveedor)
        print("\nProducto actualizado correctamente.")
        pausa()

    # =========================
    # ACTUALIZAR PRECIO DE PRODUCTOS
    # =========================
    def _actualizar_precio_producto(self):
        limpiar_pantalla()
        print("\n── Actualizar precio de producto ──")
        producto = self._seleccionar_producto("Selecciona el número a actualizar (0 para cancelar): ")
        if producto is None:
            return
        print(f"\nEditando: {producto.nombre} | Deja en blanco para conservar el valor actual.\n")        
        producto.precio      = self._pedir_precio(producto.precio)        
        print("\nProducto actualizado correctamente.")
        pausa()

    # =========================
    # ACTUALIZAR PRECIO DE PRODUCTOS
    # =========================
    def _actualizar_stock_producto(self):
        limpiar_pantalla()
        print("\n── Actualizar precio de producto ──")
        producto = self._seleccionar_producto("Selecciona el número a actualizar (0 para cancelar): ")
        if producto is None:
            return
        print(f"\nEditando: {producto.nombre} | Deja en blanco para conservar el valor actual.\n")        
        producto.stock       = self._pedir_stock(producto.stock)   
        print("\nProducto actualizado correctamente.")
        pausa()

    # =========================
    # ELIMINAR PRODUCTOS
    # =========================
    def _eliminar_productos(self):
        limpiar_pantalla()
        print("\n── Eliminar producto ──")

        producto = self._seleccionar_producto("Selecciona el número a actualizar (0 para cancelar): ")
        if producto is None:
            return
        
        self.producto_service.eliminar_producto(producto.nombre)
        
        print("\nProducto eliminado correctamente.")
        pausa()

    # =========================
    # MOSTRAR STOCKS DE PRODUCTOS
    # =========================
    def _mostrar_stock(self):
        salir = False
        while not salir:
            limpiar_pantalla()
            print("\n── Stock actual ──")
            productos = self.producto_service.get_productos()
            
            if not productos:
                print("\nNo hay productos registrados.")
                pausa()
                salir = True
            else:
                print(f"\n{'#':<4} {'Nombre':<25} {'Stock':>8}")
                print("─" * 40)
                for i, p in enumerate(productos, 1):
                    alerta = "(Stock bajo)" if p.stock < 5 else ""
                    print(f"{i:<4} {p.nombre:<25} {p.stock:>8} {alerta}")
                
                print("\n0- Volver al menú")
                if input("Elige una opción: ").strip() == "0":
                    salir = True    
    
    def _seleccionar_producto(self, mensaje="Selecciona el número del producto (0 para cancelar): "):
        productos = self._listar_productos()
        if productos is None:
            pausa()
            return None
        
        while True:
            try:
                idx = int(input(f"\n{mensaje}")) - 1
                if idx == -1:
                    return None
                if 0 <= idx < len(productos):
                    return productos[idx]
                print("Número fuera de rango. Intenta nuevamente.")
            except ValueError:
                print("Ingresa un número válido.")
    
    def _pedir_nombre(self, actual=""):
        while True:
            nombre = input(f"Nombre      [{actual}]: ").strip() if actual else input("Nombre      : ")
            if actual and not nombre:
                return actual
            try:
                return self.producto_service.validar_nombre(nombre)
            except ValueError as e:
                print(f"{e}. Intenta nuevamente.\n")
    
    def _pedir_stock(self, actual=""):
        while True:
            stock = input(f"Stock       [{actual}]: ").strip() if actual else input("Stock       : ")
            if actual and not stock:
                return actual
            try:
                return self.producto_service.validar_stock(stock)
            except ValueError as e:
                print(f"{e}. Intenta nuevamente.\n")
    
    def _pedir_precio(self, actual=""):
        while True:
            precio = input(f"Precio      [{actual}]: ").strip() if actual else input("Precio      : ")
            if actual and not precio:
                return actual
            try:
                return self.producto_service.validar_precio(precio)
            except ValueError as e:
                print(f"{e}. Intenta nuevamente.\n")
                
    def _pedir_descripcion(self, actual=""):
        while True:
            descripcion = input(f"Descripción [{actual}]: ").strip() if actual else input("Descripción : ")
            if actual and not descripcion:
                return actual
            try:
                return self.producto_service.validar_descripcion(descripcion)
            except ValueError as e:
                print(f"{e}. Intenta nuevamente.\n")
    
    def _pedir_proveedor(self, actual=None):
        while True:
            proveedores = self.proveedor_service.get_proveedores()
            if not proveedores:
                print("\n No hay proveedores registrados. Debes registrar uno para continuar.")
                opcion = input("¿Deseas registrar uno ahora? (s/n): ").strip().lower()
                if opcion == "s":
                    self.proveedor_ui._registrar_proveedor()
                    return self.proveedor_service.get_proveedores()[-1]
                else:
                    return "cancelar"
            print(f"\n{'#':<4} Escoja proveedor")
            print("─" * 30)
            for i, p in enumerate(proveedores, 1):
                print(f"{i:<4} {p.nombre}")
                print(f"{len(proveedores) + 1:<4} Registrar nuevo proveedor")
                if actual:
                    print(f"\nProveedor actual: {actual.nombre} | 0 para conservar")
                        

            while True:
                try:
                    idx = int(input("\nSelecciona una opción: "))
                    if idx == 0:
                        if actual:
                            return actual
                        print("Debes seleccionar un proveedor.")
                    elif  idx == len(proveedores) + 1:
                        self.proveedor_ui._registrar_proveedor()
                        break
                    elif  1 <= idx <= len(proveedores):
                        return proveedores[idx - 1]
                    print("Número fuera de rango. Intenta nuevamente.")
                except ValueError:
                    print("Ingresa un número válido.")