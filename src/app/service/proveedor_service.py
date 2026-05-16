from app.model.proveedor import Proveedor
import re

class ProveedorService:
    def __init__(self):
        self.lista_proveedores = []

    # =========================
    # Validaciones
    # =========================

    def validar_nombre(self, nombre):
        if nombre is None or nombre.strip() == "":
            raise ValueError("El nombre del proveedor no puede estar vacío")

        return nombre.strip()

    def validar_telefono(self, telefono):
        if telefono is None or telefono.strip() == "":
            raise ValueError("El telefono no puede estar vacio")
    
        patron = r"^\d{4}-\d{4}$"
    
        if not re.match(patron, telefono):
            raise ValueError("El telefono debe tener el formato 1234-5678")

        return telefono
    
    def validar_email(self, email):
        if email is None or email.strip() == "":
            raise ValueError("El email no puede estar vacío")

        if "@" not in email or "." not in email:
            raise ValueError("El email no es válido")

        return email.strip()

    # =========================
    # REGISTRAR PROVEEDOR
    # =========================

    def registrar_proveedor(self, nombre, telefono, email):

        nombre = self.validar_nombre(nombre)
        telefono = self.validar_telefono(telefono)
        email = self.validar_email(email)

        proveedor = Proveedor(
            nombre,
            telefono,
            email
        )

        self.lista_proveedores.append(proveedor)

    # =========================
    # OBTENER PROVEEDORES
    # =========================

    def get_proveedores(self):
        return self.lista_proveedores

    # =========================
    # BUSCAR PROVEEDOR
    # =========================

    def buscar_proveedor(self, nombre):
        for proveedor in self.lista_proveedores:
            if proveedor.nombre.lower() == nombre.lower():
                return proveedor

        return None
        
    # =========================
    # ELIMINAR PROVEEDOR
    # =========================

    def eliminar_proveedor(self, nombre):
        proveedor = self.buscar_proveedor(nombre)

        if proveedor is None:
            raise ValueError("Proveedor no encontrado")

        self.lista_proveedores.remove(proveedor)    
        
    # =========================
    # VALIDAR DUPLICADO
    # =========================
    
    def validar_duplicado(self, nombre_proveedor):
        for proveedor in self.lista_proveedores:
            if proveedor.nombre.lower() == nombre_proveedor.lower():
                raise ValueError("Ya se ha registrado un proveedor con el mismo nombre")