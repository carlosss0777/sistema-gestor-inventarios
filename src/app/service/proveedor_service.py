from app.model.proveedor import proveedor

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
            raise ValueError("El teléfono no puede estar vacío")

        if not telefono.isdigit():
            raise ValueError("El teléfono debe contener solo números")

        return telefono
    
    def validar_email(self, email):
        if email is None or email.strip() == "":
            raise ValueError("El email no puede estar vacío")

        if "@" not in email or "." not in email:
            raise ValueError("El email no es válido")

        return email.strip()    