from app.service.proveedor_service import ProveedorService
from app.service.producto_service import ProductoService
from app.ui.proveedor_ui import proveedor_ui
from app.utils.validators import *
from app.utils.tablas import *
from app.utils.tools import *

class producto_ui:
    def __init__(self, producto_service: ProductoService, proveedor_service: ProveedorService, proveedor_ui:proveedor_ui):
        self.producto_service  = producto_service
        self.proveedor_service = proveedor_service
        self.proveedor_ui      = proveedor_ui

    def menu_producto(self):
        while True:
            while True:
                limpiar_pantalla()
                print("\n----------------------------")
                print("== GESTIÓN DE PRODUCTOS ==")
                print("----------------------------")
                print("1- Registrar producto")
                print("2- Mostrar productos")
                print("3- Eliminar producto")
                print("4- Actualizar producto")
                print("5- Mostrar stock actual")
                print("6- Actualizar precio de un producto")
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
        limpiar_pantalla()
        print("\n------------------------------------------------------------")
        print("                -- LISTADO DE PRODUCTOS --")
        print("------------------------------------------------------------")
        self._listar_productos()
        detener()
    
    def _listar_productos(self):
        productos = self.producto_service.get_productos()
        if not productos:
            print("\nNo hay productos registrados.")
            return None
        
        tabla = tabla_productos(productos)
        print(tabla)

        return productos
    
    # =========================
    # REGISTRAR PRODUCTOS
    # =========================
    def _registrar_producto(self):
        limpiar_pantalla()
        print("\n------------------------------------------------------------")
        print("                 -- REGISTRAR PRODUCTO --")
        print("------------------------------------------------------------")
        nombre      = self._pedir_nombre()
        stock       = self._pedir_stock()
        precio      = self._pedir_precio()
        descripcion = self._pedir_descripcion()
        proveedor   = self._pedir_proveedor()
        
        if proveedor == "cancelar":
            print("\nRegistro cancelado.")
            pausa()
            return
        
        try:
            self.producto_service.validar_duplicado(nombre, proveedor) # validacion de duplicados
            
            self.producto_service.registrar_producto(nombre, stock, proveedor, precio, descripcion)
            print("\nProducto registrado exitosamente.")
            detener()
            
        except ValueError as e:
            mensaje_error(e)
            detener()
    
    # =========================
    # ACTUALIZAR PRODUCTOS
    # =========================
    def _actualizar_producto(self):
        limpiar_pantalla()
        print("\n------------------------------------------------------------")
        print("                 -- ACTUALIZAR PRODUCTO --")
        print("------------------------------------------------------------")
        producto = self._seleccionar_producto("Selecciona el número a actualizar (0 para cancelar): ")
        if producto is None:
            pausa()
            return
        print(f"\nEditando: {producto.nombre} | Deja en blanco para conservar el valor actual.\n")
        producto.nombre      = self._pedir_nombre(producto.nombre)
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
        print("\n------------------------------------------------------------")
        print("             -- ACTUALIZAR PRECIO DE PRODUCTO --")
        print("------------------------------------------------------------")
        producto = self._seleccionar_producto("Selecciona el número a actualizar (0 para cancelar): ")
        if producto is None:
            pausa()
            return
        print(f"\nEditando: {producto.nombre} | Deja en blanco para conservar el valor actual.\n")        
        producto.precio      = self._pedir_precio(producto.precio)        
        print("\nProducto actualizado correctamente.")
        pausa()

    # =========================
    # ELIMINAR PRODUCTOS
    # =========================
    def _eliminar_productos(self):
        limpiar_pantalla()
        print("\n------------------------------------------------------------")
        print("             -- ELIMINAR PRODUCTOS --")
        print("------------------------------------------------------------")

        producto = self._seleccionar_producto("Selecciona el número a eliminar (0 para cancelar): ")
        if producto is None:
            pausa()
            return
        
        self.producto_service.eliminar_producto(producto.nombre)
        
        print("\nProducto eliminado correctamente.")
        detener()

    # =========================
    # MOSTRAR STOCKS DE PRODUCTOS
    # =========================
    def _mostrar_stock(self):
        limpiar_pantalla()
        print("\n------------------------------------------------------------")
        print("                 -- STOCK ACTUAL --")
        print("------------------------------------------------------------")
        productos = self.producto_service.get_productos()
            
        if not productos:
            print("\nNo hay productos registrados.")
            pausa()
        else:
            tabla = tabla_stock(productos)
            print(tabla)
            detener()
    
    def _seleccionar_producto(self, mensaje="Selecciona el número del producto (0 para cancelar): "):
        productos = self._listar_productos()
        if productos is None:
            pausa()
            return None
        
        while True:
            try:
                idx = validar_indice(input(mensaje), len(productos))
                
                if idx == -1:
                    return None
                else:
                    return productos[idx]
            
            except ValueError as e:
                mensaje_error(e)
                pausa()
    
    def _pedir_nombre(self, actual=""):
        while True:
            nombre = input(f"Nombre [{actual}]: ").strip() if actual else input("Nombre: ")
            if actual and not nombre:
                return actual
            try:
                return self.producto_service.validar_nombre(nombre)
            except ValueError as e:
                mensaje_error(e)
                pausaLarga()
    
    def _pedir_stock(self, actual=""):
        while True:
            stock = input("Stock: ")
            
            try:
                return self.producto_service.validar_stock(stock)
            except ValueError as e:
                mensaje_error(e)
                pausaLarga()
    
    def _pedir_precio(self, actual=""):
        while True:
            precio = input(f"Precio [${actual}]: $").strip() if actual else input("Precio: $")
            if actual and not precio:
                return actual
            try:
                return self.producto_service.validar_precio(precio)
            except ValueError as e:
                mensaje_error(e)
                pausaLarga()
                
    def _pedir_descripcion(self, actual=""):
        while True:
            descripcion = input(f"Descripción [{actual}]: ").strip() if actual else input("Descripción: ")
            if actual and not descripcion:
                return actual
            try:
                return self.producto_service.validar_descripcion(descripcion)
            except ValueError as e:
                mensaje_error(e)
                pausaLarga()
    
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
            
            print("\n------------------------------------------------------------")
            print("             -- PROVEEDORES REGISTRADOS --")
            print("------------------------------------------------------------")
            tabla = tabla_proveedores(proveedores)
            print(tabla)
            
            if actual:
                print(f"\nProveedor actual: {actual.nombre} | 0 para conservar")
                
            while True:
                try:
                    idx = validar_indice(input("\nSelecciona el proveedor: "), len(proveedores))
                    if idx == -1:
                        if actual:
                            return actual
                        print("Debes seleccionar un proveedor")
                    
                    else:
                        return proveedores[idx]
                except ValueError as e:
                    mensaje_error(e)
                    pausaLarga()