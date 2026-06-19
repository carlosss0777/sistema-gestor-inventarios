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
    
    # Pruebas de registros y duplicados
    def test_registrar_proveedor_exitoso(self):
        nuevo = self.service.registrar_proveedor("Distribuidora X", "1111-2222", "info@x.com")
        self.assertIn(nuevo, self.service.get_all())
        self.assertEqual(nuevo.nombre, "Distribuidora X")
    
    def test_registrar_proveedor_datos_invalidos(self):
        # Si falla el teléfono, no debería registrarse
        with self.assertRaises(ValueError):
            self.service.registrar_proveedor("Distribuidora Y", "12345", "info@y.com")
    
    def test_validar_duplicado_lanza_error(self):
        # "Proveedor Central" ya fue registrado
        with self.assertRaises(ValueError):
            self.service.validar_duplicado("proveedor central") # Probar insensibilidad a mayúsculas

    def test_validar_duplicado_no_lanza_error(self):
        # No debería lanzar ninguna excepción si el nombre está disponible
        try:
            self.service.validar_duplicado("Proveedor Nuevo Totalmente")
        except ValueError:
            self.fail("validar_duplicado() lanzó ValueError con un nombre inexistente.")
    
    # Pruebas de busqueda y filtrado
    def test_buscar_proveedor_existente_e_inexistente(self):
        encontrado = self.service.buscar_proveedor("pRoVeEdOr CeNtRaL")
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nombre, "Proveedor Central")

        no_encontrado = self.service.buscar_proveedor("No Existo")
        self.assertIsNone(no_encontrado)
        
    def test_get_proveedores_solo_activos(self):
        # Registramos otro y lo ponemos inactivo directamente
        prov_inactivo = self.service.registrar_proveedor("Proveedor Inactivo", "4444-5555", "inactivo@test.com")
        prov_inactivo.activo = False

        activos = self.service.get_proveedores()
        self.assertIn(self.proveedor_base, activos)
        self.assertNotIn(prov_inactivo, activos)

if __name__ == '__main__':
    unittest.main()