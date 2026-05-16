# Modulo de proveedores

from app.service.proveedor_service import ProveedorService
from app.utils.validators import *
from app.utils.tablas import *
from app.utils.tools import *

class proveedor_ui:
    
    def __init__(self, proveedor_service: ProveedorService):
        self.proveedor_service = proveedor_service

    def menu_proveedor(self):
        while True:
            while True:
                limpiar_pantalla()
                print("\n----------------------------")
                print("== GESTIÓN DE PROVEEDORES ==")
                print("----------------------------")
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
                    self._registrar_proveedor()                
                case 2:
                    self._mostrar_proveedores()
                case 3:
                    self._eliminar_proveedor()                
                case 4:
                    self._actualizar_proveedor()            
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
        limpiar_pantalla()
        print("\n------------------------------------------------------------")
        print("              -- LISTADO DE PROVEEDORES --")
        print("------------------------------------------------------------")
        self._listar_proveedores()
        detener()

    def _listar_proveedores(self):
        proveedores = self.proveedor_service.get_proveedores()
        if not proveedores:
            print("\nNo hay proveedores registrados.")
            return None
        
        tabla = tabla_proveedores(proveedores)
        print(tabla)

        return proveedores
    

    # =========================
    # REGISTRAR PROVEEDORES
    # =========================
    def _registrar_proveedor(self):
        limpiar_pantalla()
        print("\n------------------------------------------------------------")
        print("               -- REGISTRAR PROVEEDOR --")
        print("------------------------------------------------------------")
        
        nombre   = self._pedir_nombre()
        telefono = self._pedir_telefono()
        email    = self._pedir_email()
        
        try:
            self.proveedor_service.validar_duplicado(nombre)
            self.proveedor_service.registrar_proveedor(nombre, telefono, email)
            print("\nProveedor registrado exitosamente.")
            pausa()
            
        except ValueError as e:
            mensaje_error(e)
            pausaLarga()
        
    # =========================
    # ACTUALIZAR PROVEEDORES
    # =========================
    def _actualizar_proveedor(self):
        limpiar_pantalla()
        print("\n------------------------------------------------------------")
        print("               -- ACTUALIZAR PROVEEDOR --")
        print("------------------------------------------------------------")

        proveedor = self._seleccionar_proveedor("Selecciona el número a actualizar (0 para cancelar): ")
        if proveedor is None:
            pausa()
            return
        print(f"\nEditando: {proveedor.nombre} | Deja en blanco para conservar el valor actual.\n")
        proveedor.nombre   = self._pedir_nombre(proveedor.nombre)
        proveedor.telefono = self._pedir_telefono(proveedor.telefono)
        proveedor.email    = self._pedir_email(proveedor.email)

        print("\nProveedor actualizado correctamente.")
        pausa()

    # =========================
    # ELIMINAR PROVEEDORES
    # =========================
    def _eliminar_proveedor(self):
        limpiar_pantalla()
        print("\n------------------------------------------------------------")
        print("               -- ELIMINAR PROVEEDOR --")
        print("------------------------------------------------------------")

        proveedor = self._seleccionar_proveedor("Selecciona el número a eliminar (0 para cancelar): ")
        if proveedor is None:
            pausa()
            return
        
        self.proveedor_service.eliminar_proveedor(proveedor.nombre)
        
        print("\nProveedor eliminado correctamente.")
        pausa()



    def _seleccionar_proveedor(self, mensaje="Selecciona el número del proveedor (0 para cancelar): "):
        proveedores = self._listar_proveedores()
        if proveedores is None:
            pausa()
            return None

        while True:
            try:
                idx = validar_indice(input(mensaje), len(proveedores))
                
                if idx == -1:
                    return None
                else:
                    return proveedores[idx]
            
            except ValueError as e:
                mensaje_error(e)
                pausa()

    def _pedir_nombre(self, actual=""):
        while True:
            nombre = input(f"Nombre [{actual}]: ").strip() if actual else input("Nombre: ")
            if actual and not nombre:
                return actual        # conserva el valor actual
            try:
                return self.proveedor_service.validar_nombre(nombre)
            except ValueError as e:
                mensaje_error(e)
                pausaLarga()
    
    def _pedir_telefono(self, actual=""):
        while True:
            telefono = input(f"Teléfono [{actual}]: ").strip() if actual else input("Teléfono: ")
            if actual and not telefono:
                return actual
            try:
                return self.proveedor_service.validar_telefono(telefono)
            except ValueError as e:
                mensaje_error(e)
                pausaLarga()
    
    def _pedir_email(self, actual=""):
        while True:
            email = input(f"Email [{actual}]: ").strip() if actual else input("Email: ")
            if actual and not email:
                return actual
            try:
                return self.proveedor_service.validar_email(email)
            except ValueError as e:
                mensaje_error(e)
                pausaLarga()