# Modulo de proveedores

from app.service.proveedor_service import ProveedorService
from app.service.producto_service import ProductoService
from app.utils.validators import *
from app.utils.tablas import *
from app.utils.tools import *

class proveedor_ui:
    
    def __init__(self, proveedor_service: ProveedorService, producto_service: ProductoService):
        """
        Constructor de la clase proveedor_ui.

        Args:
            proveedor_service (ProveedorService): Instancia del servicio de proveedores.
            producto_service (ProductoService): Instancia del servicio de productos.
        """
        self.proveedor_service = proveedor_service
        self.producto_service = producto_service

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
        """
        Muestra la lista de proveedores registrados en el sistema. Si no hay proveedores, muestra un mensaje indicando que no hay registros. Utiliza una tabla para presentar la información de manera clara y ordenada.
        """
        limpiar_pantalla()
        print("\n------------------------------------------------------------")
        print("              -- LISTADO DE PROVEEDORES --")
        print("------------------------------------------------------------")
        self._listar_proveedores()
        detener()

    def _listar_proveedores(self):
        """
        Obtiene y muestra la lista de proveedores registrados en el sistema. Si no hay proveedores, muestra un mensaje indicando que no hay registros.
        """
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
        """
        Registra un nuevo proveedor en el sistema. Solicita al usuario ingresar el nombre, teléfono y correo electrónico del proveedor. Antes de registrar, valida que el nombre no esté duplicado y que los datos ingresados sean correctos. Si el registro es exitoso, muestra un mensaje de confirmación; si hay errores, muestra mensajes de error correspondientes.
        """
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
        """
        Actualiza los datos de un proveedor existente en el sistema. Primero, muestra la lista de proveedores para que el usuario seleccione cuál desea actualizar. Luego, solicita al usuario ingresar los nuevos datos (nombre, teléfono y correo electrónico) para el proveedor seleccionado. Si el usuario deja algún campo en blanco, se conservará el valor actual. Antes de actualizar, valida que los datos ingresados sean correctos y que el nuevo nombre no esté duplicado (si se cambia). Si la actualización es exitosa, muestra un mensaje de confirmación; si hay errores, muestra mensajes de error correspondientes.
        """
        limpiar_pantalla()
        print("\n------------------------------------------------------------")
        print("               -- ACTUALIZAR PROVEEDOR --")
        print("------------------------------------------------------------")

        proveedor = self._seleccionar_proveedor("Selecciona el número a actualizar (0 para cancelar): ")
        if proveedor is None:
            pausa()
            return
        print(f"\nEditando: {proveedor.nombre} | Deja en blanco para conservar el valor actual.\n")
        nombre   = self._pedir_nombre(proveedor.nombre)
        telefono = self._pedir_telefono(proveedor.telefono)
        email    = self._pedir_email(proveedor.email)
        
        self.proveedor_service.actualizar_proveedor(proveedor, nombre, telefono, email, self.producto_service)

        print("\nProveedor actualizado correctamente.")
        pausa()

    # =========================
    # ELIMINAR PROVEEDORES
    # =========================
    def _eliminar_proveedor(self):
        """
        Elimina un proveedor del sistema. Primero, muestra la lista de proveedores para que el usuario seleccione cuál desea eliminar. Luego, solicita confirmación antes de proceder con la eliminación. Si la eliminación es exitosa, muestra un mensaje de confirmación; si hay errores, muestra mensajes de error correspondientes.
        """
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
        """
        Selecciona un proveedor de la lista mostrada. Muestra la lista de proveedores y solicita al usuario ingresar el número correspondiente al proveedor que desea seleccionar. Si el usuario ingresa 0, se cancela la selección y se retorna None. Si el usuario ingresa un número inválido o fuera del rango, muestra un mensaje de error y solicita nuevamente la entrada.
        """
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
        """
        Pide al usuario ingresar el nombre de un proveedor. Si se proporciona un valor actual, muestra el valor actual entre corchetes y permite al usuario dejarlo en blanco para conservarlo. Valida el nombre ingresado utilizando el servicio de proveedor. Si el nombre es válido, lo retorna. Si ocurre un error durante la validación, muestra un mensaje de error y solicita al usuario que intente nuevamente.
        """
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
        """
        Pide al usuario ingresar el teléfono de un proveedor. Si se proporciona un valor actual, muestra el valor actual entre corchetes y permite al usuario dejarlo en blanco para conservarlo. Valida el teléfono ingresado utilizando el servicio de proveedor. Si el teléfono es válido, lo retorna. Si ocurre un error durante la validación, muestra un mensaje de error y solicita al usuario que intente nuevamente.
        """
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
        """
        Pide al usuario ingresar el correo electrónico de un proveedor. Si se proporciona un valor actual, muestra el valor actual entre corchetes y permite al usuario dejarlo en blanco para conservarlo. Valida el correo electrónico ingresado utilizando el servicio de proveedor. Si el correo electrónico es válido, lo retorna. Si ocurre un error durante la validación, muestra un mensaje de error y solicita al usuario que intente nuevamente.
        """
        while True:
            email = input(f"Email [{actual}]: ").strip() if actual else input("Email: ")
            if actual and not email:
                return actual
            try:
                return self.proveedor_service.validar_email(email)
            except ValueError as e:
                mensaje_error(e)
                pausaLarga()