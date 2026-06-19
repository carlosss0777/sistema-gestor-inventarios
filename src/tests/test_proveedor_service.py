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

    def test_validar_nombre_vacio_o_ninguno(self):
        with self.assertRaises(ValueError):
            self.service.validar_nombre("")
        with self.assertRaises(ValueError):
            self.service.validar_nombre("   ")
        with self.assertRaises(ValueError):
            self.service.validar_nombre(None)
    
    def test_validar_telefono_correcto(self):
        tel_valido = "7777-8888"
        resultado = self.service.validar_telefono(tel_valido)
        self.assertEqual(resultado, "7777-8888")

    def test_validar_telefono_formato_incorrecto(self):
        formatos_invalidos = ["12345678", "123-45678", "abcd-efgh", "", None]
        for tel in formatos_invalidos:
            with self.subTest(telefono=tel):
                with self.assertRaises(ValueError):
                    self.service.validar_telefono(tel)
    
    def test_validar_email_correcto(self):
        email_valido = "  test@proveedor.com  "
        resultado = self.service.validar_email(email_valido)
        self.assertEqual(resultado, "test@proveedor.com")

    def test_validar_email_incorrecto(self):
        emails_invalidos = ["testproveedor.com", "test@proveedor", "", None]
        for email in emails_invalidos:
            with self.subTest(email=email):
                with self.assertRaises(ValueError):
                    self.service.validar_email(email)

if __name__ == '__main__':
    unittest.main()