# Repositories falsos compartidos para todas las pruebas

"""
Repositories falsos para pruebas unitarias. Estos repositorios no interactúan con archivos ni datos, sino que simulan el comportamiento esperado para facilitar las pruebas de los servicios (necesarios porque todos los servicios reciben en el constructor el repository, si no se colocan, dara error).
"""
class ProductoRepositoryFalso:
    # Metodo guardar() no hace nada, solo simula el comportamiento de guardar una lista de productos
    def guardar(self, lista): pass
    # Metodo cargar() devuelve una lista vacia, simulando que no hay productos guardados
    def cargar(self, proveedores): return []

class ProveedorRepositoryFalso:
    def guardar(self, lista): pass
    def cargar(self): return []

class MovimientoRepositoryFalso:
    def guardar(self, lista): pass
    def cargar(self): return []