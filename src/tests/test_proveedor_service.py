# Pruebas a proveedor_service

from app.service.proveedor_service import ProveedorService
from tests.fakes import ProveedorRepositoryFalso
import unittest


class TestProveedorService(unittest.TestCase):
    # comandos para ejecutar las pruebas: 
    # cd src/
    # python -m unittest tests.test_proveedor_service
    
    def setUp(self):
        self.service = ProveedorService(ProveedorRepositoryFalso())
        
    # pruebas de los metodos


if __name__ == '__main__':
    unittest.main()