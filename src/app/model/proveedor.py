# Clase proveedor del sistema
class Proveedor:
    def __init__(self, nombre_proveedor, telefono_proveedor, email_proveedor):
        self._nombre = nombre_proveedor
        self._telefono = telefono_proveedor
        self._email = email_proveedor
        self._activo = True
        
    @property
    def activo(self):
        return self._activo
    
    @activo.setter
    def activo(self, valor):
        self._activo = valor

    # Nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    # Teléfono
    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        self._telefono = valor

    # Email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        self._email = valor



