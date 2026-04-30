# Clase proveedor del sistema
class Proveedor:
    def __init__(self, nombre_proveedor, telefono_proveedor, email_proveedor):
        self._nombre = nombre_proveedor
        self._telefono = telefono_proveedor
        self._email = email_proveedor

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
        if not valor.isdigit():
            raise ValueError("El teléfono solo debe contener números")
        self._telefono = valor

    # Email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if "@" not in valor:
            raise ValueError("El email no es válido")
        self._email = valor



