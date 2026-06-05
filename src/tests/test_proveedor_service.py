# Pruebas a proveedor_service

from app.service.proveedor_service import ProveedorService
from tests.fakes import ProveedorRepositoryFalso
import unittest


class TestProveedorService(unittest.TestCase):
    # comando para ejecutar las pruebas: 
    # python -m unittest src.tests.test_proveedor_service
    
    def setUp(self):
        self.service = ProveedorService(ProveedorRepositoryFalso())
        
    # pruebas de los metodos


if __name__ == '__main__':
    unittest.main()