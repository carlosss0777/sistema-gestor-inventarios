# Repositories falsos compartidos para todas las pruebas

class ProductoRepositoryFalso:
    def guardar(self, lista): pass
    def cargar(self, proveedores): return []

class ProveedorRepositoryFalso:
    def guardar(self, lista): pass
    def cargar(self): return []

class MovimientoRepositoryFalso:
    def guardar(self, lista): pass
    def cargar(self): return []