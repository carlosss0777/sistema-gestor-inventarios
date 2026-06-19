# Pruebas a proveedor_service

from app.service.proveedor_service import ProveedorService
from tests.fakes import ProveedorRepositoryFalso
import unittest


class TestProveedorService(unittest.TestCase):
    # comandos para ejecutar las pruebas: 
    # cd src/
    # python -m unittest tests.test_proveedor_service
    
    def setUp(self):
        # Inicializamos un repositorio falso limpio para cada prueba
        self.repo_falso = ProveedorRepositoryFalso()        
        self.service = ProveedorService(self.repo_falso)
        
        # Agregar un proveedor base para usar en búsquedas/actualizaciones
        self.proveedor_base = self.service.registrar_proveedor("Proveedor Central", "2222-3333", "contacto@central.com")
        
    # pruebas de los metodos
    
    # Pruebas de Validacion
    def test_validar_nombre_correcto(self):
        nombre_valido = "   Proveedor ABC   "
        resultado = self.service.validar_nombre(nombre_valido)
        self.assertEqual(resultado, "Proveedor ABC")

if __name__ == '__main__':
    unittest.main()