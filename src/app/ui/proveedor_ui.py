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
                    self._registrar_proveedor()
                
                case 2:
                    self._mostrar_proveedores()
                case 3:
                    limpiar_pantalla()
                    pass
                    continue
                
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
    

    # =========================
    # REGISTRAR PROVEEDORES
    # =========================
    def _registrar_proveedor(self):
        limpiar_pantalla()
        print("\n── Registrar proveedor ──")
        
        nombre   = self._pedir_nombre()
        telefono = self._pedir_telefono()
        email    = self._pedir_email()
        self.proveedor_service.registrar_proveedor(nombre, telefono, email)
        print("\nProveedor registrado exitosamente.")
        pausa()
        
    # =========================
    # ACTUALIZAR PROVEEDORES
    # =========================
    def _actualizar_proveedor(self):
        limpiar_pantalla()
        print("\n── Actualizar proveedor ──")

        proveedor = self._seleccionar_proveedor("Selecciona el número a actualizar (0 para cancelar): ")
        if proveedor is None:
            return
        print(f"\nEditando: {proveedor.nombre} | Deja en blanco para conservar el valor actual.\n")
        proveedor.nombre   = self._pedir_nombre(proveedor.nombre)
        proveedor.telefono = self._pedir_telefono(proveedor.telefono)
        proveedor.email    = self._pedir_email(proveedor.email)

        print("\nProveedor actualizado correctamente.")
        pausa()
        
    def _seleccionar_proveedor(self, mensaje="Selecciona el número del proveedor (0 para cancelar): "):
        proveedores = self._listar_proveedores()
        if proveedores is None:
            pausa()
            return None

        while True:
            try:
                idx = int(input(f"\n{mensaje}")) - 1
                if idx == -1:
                    return None
                if 0 <= idx < len(proveedores):
                    return proveedores[idx]
                print("Número fuera de rango. Intenta nuevamente.")
            except ValueError:
                print("Ingresa un número válido.")

    def _pedir_nombre(self, actual=""):
        while True:
            nombre = input(f"Nombre   [{actual}]: ").strip() if actual else input("Nombre   : ")
            if actual and not nombre:
                return actual        # conserva el valor actual
            try:
                return self.proveedor_service.validar_nombre(nombre)
            except ValueError as e:
                print(f"{e}. Intenta nuevamente.\n")
    
    def _pedir_telefono(self, actual=""):
        while True:
            telefono = input(f"Teléfono [{actual}]: ").strip() if actual else input("Teléfono : ")
            if actual and not telefono:
                return actual
            try:
                return self.proveedor_service.validar_telefono(telefono)
            except ValueError as e:
                print(f"{e}. Intenta nuevamente.\n")
    
    def _pedir_email(self, actual=""):
        while True:
            email = input(f"Email    [{actual}]: ").strip() if actual else input("Email    : ")
            if actual and not email:
                return actual
            try:
                return self.proveedor_service.validar_email(email)
            except ValueError as e:
                print(f"{e}. Intenta nuevamente.\n")