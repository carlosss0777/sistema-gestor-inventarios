from app.repository.proveedor_repository import proveedor_repository
from app.model.proveedor import Proveedor
import re

class ProveedorService:
    def __init__(self, repository: proveedor_repository):
        self._repo = repository
        self.lista_proveedores: list[Proveedor] = self._repo.cargar()
        # self.datos_prueba()

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
        
        self._repo.guardar(self.lista_proveedores)
        
        return proveedor

    # =========================
    # OBTENER PROVEEDORES
    # =========================
    def get_all(self):
        return self.lista_proveedores

    def get_proveedores(self):
        proveedores_activos = []
        for proveedor in self.lista_proveedores:
            if proveedor.activo:
                proveedores_activos.append(proveedor)
                
        return proveedores_activos

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

        proveedor.activo = False
        self._repo.guardar(self.lista_proveedores)
        
    # =========================
    # VALIDAR DUPLICADO
    # =========================
    
    def validar_duplicado(self, nombre_proveedor):
        for proveedor in self.lista_proveedores:
            if proveedor.nombre.lower() == nombre_proveedor.lower():
                raise ValueError("Ya se ha registrado un proveedor con el mismo nombre")
          
    # =========================
    # Actualizar proveedor
    # =========================
    def actualizar_proveedor(self, proveedor:Proveedor, nombre, telefono, email, producto_service=None):
        nuevo_nombre = self.validar_nombre(nombre)
        nuevo_telefono = self.validar_telefono(telefono)
        nuevo_email = self.validar_email(email)
        
        proveedor.nombre = nuevo_nombre
        proveedor.telefono = nuevo_telefono
        proveedor.email = nuevo_email
        
        self._repo.guardar(self.lista_proveedores)
        
        if producto_service:
            producto_service.sincronizar_json()
            
        return proveedor
     
    """       
    # =========================
    # DATOS DE PRUEBA
    # =========================
    
    def datos_prueba(self):
        prov1 = Proveedor("TechSuppier", "2341-8212", "tech@supplier.sv")
        prov2 = Proveedor("Global Electronics", "2345-7593", "global@electronics.dev")
        prov3 = Proveedor("CompuWorld", "2953-2946", "world.compu@gmail.com")
        
        self.lista_proveedores.append(prov1)
        self.lista_proveedores.append(prov2)
        self.lista_proveedores.append(prov3)
    """