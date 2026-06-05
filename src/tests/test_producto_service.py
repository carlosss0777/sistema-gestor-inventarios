# Pruebas a producto_service

from app.service.producto_service import ProductoService
from tests.fakes import ProductoRepositoryFalso
from app.model.proveedor import Proveedor
import unittest


class TestProductoService(unittest.TestCase):
    # comando para ejecutar las pruebas: 
    # python -m unittest src.tests.test_producto_service
    
    def setUp(self):
        # proveedor de prueba reutilizable en todos los tests
        self.proveedor = Proveedor("Logitech", "2222-2222", "logi@tech.dev")
        self.service   = ProductoService(ProductoRepositoryFalso(), [])
        
    # pruebas de los metodos


if __name__ == '__main__':
    unittest.main()