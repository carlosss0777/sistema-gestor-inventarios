# Clase proveedor del sistema
class Proveedor:
    # Constructor de la clase proveedor
    def __init__(self, nombre_proveedor, telefono_proveedor, email_proveedor):
        self._nombre = nombre_proveedor
        self._telefono = telefono_proveedor
        self._email = email_proveedor
        self._activo = True
        
    # getter del estado del proveedor
    @property
    def activo(self):
        return self._activo
    
    # setter del estado del proveedor
    @activo.setter
    def activo(self, valor):
        self._activo = valor

    # getter del nombre del proveedor
    @property
    def nombre(self):
        return self._nombre

    # setter del nombre del proveedor
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    # getter del telefono del proveedor
    @property
    def telefono(self):
        return self._telefono

    # setter del telefono del proveedor
    @telefono.setter
    def telefono(self, valor):
        self._telefono = valor

    # getter del email del proveedor
    @property
    def email(self):
        return self._email

    # setter del email del proveedor
    @email.setter
    def email(self, valor):
        self._email = valor



