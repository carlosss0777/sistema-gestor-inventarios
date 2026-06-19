# Pruebas a movimiento_service

from datetime import datetime
from unittest.mock import patch

from app.service.movimiento_service import movimiento_service
from tests.fakes import MovimientoRepositoryFalso
import unittest


class TestMovimientoService(unittest.TestCase):
    # comandos para ejecutar las pruebas:
    # cd src/
    # python -m unittest tests.test_movimiento_service

    def setUp(self):
        self.repo_falso = MovimientoRepositoryFalso()
        self.service = movimiento_service(self.repo_falso)

    # pruebas de los metodos
    def test_validar_cantidad_valida_retorna_entero(self):
        self.assertEqual(self.service.validar_cantidad("10"), 10)
        self.assertEqual(self.service.validar_cantidad("0"), 0)

    def test_validar_cantidad_vacia_o_nula_lanza_error(self):
        with self.assertRaises(ValueError):
            self.service.validar_cantidad("")
        with self.assertRaises(ValueError):
            self.service.validar_cantidad("   ")
        with self.assertRaises(ValueError):
            self.service.validar_cantidad(None)

    def test_validar_cantidad_no_numerica_lanza_error(self):
        with self.assertRaises(ValueError):
            self.service.validar_cantidad("abc")

    def test_validar_cantidad_negativa_lanza_error(self):
        with self.assertRaises(ValueError):
            self.service.validar_cantidad("-5")

    def test_validar_salida_con_stock_suficiente(self):
        self.assertEqual(self.service.validar_salida("5", 10), 5)
        self.assertEqual(self.service.validar_salida("10", 10), 10)

    def test_validar_salida_con_stock_insuficiente_lanza_error(self):
        with self.assertRaises(ValueError):
            self.service.validar_salida("11", 10)

    def test_validar_salida_cantidad_invalida_lanza_error(self):
        with self.assertRaises(ValueError):
            self.service.validar_salida("abc", 10)

    def test_registrar_movimiento_agrega_movimiento_y_guarda(self):
        class MovimientoRepositorySpy(MovimientoRepositoryFalso):
            def __init__(self):
                self.guardar_llamado = False
                self.movimientos_guardados = None

            def guardar(self, lista):
                self.guardar_llamado = True
                self.movimientos_guardados = lista.copy()

            def cargar(self):
                return []

        repo_spy = MovimientoRepositorySpy()
        service = movimiento_service(repo_spy)
        fecha_fija = datetime(2026, 1, 1, 12, 0, 0)

        with patch("app.service.movimiento_service.datetime") as mock_datetime:
            mock_datetime.now.return_value = fecha_fija
            movimiento = service.registrar_movimiento("Teclado", "Entrada", "5", None)

        self.assertTrue(repo_spy.guardar_llamado)
        self.assertEqual(len(service.get_movimientos()), 1)
        self.assertEqual(movimiento.nombre_producto, "Teclado")
        self.assertEqual(movimiento.tipo_movimiento, "Entrada")
        self.assertEqual(movimiento.cantidad, "5")
        self.assertEqual(movimiento.fecha, fecha_fija)
        self.assertIs(service.get_movimientos()[0], movimiento)
        self.assertEqual(repo_spy.movimientos_guardados, service.get_movimientos())

    def test_get_movimientos_retorna_lista_registrada(self):
        self.assertEqual(self.service.get_movimientos(), [])

        with patch("app.service.movimiento_service.datetime") as mock_datetime:
            mock_datetime.now.return_value = datetime(2026, 1, 1, 12, 0, 0)
            self.service.registrar_movimiento("Mouse", "Salida", "2", None)

        movimientos = self.service.get_movimientos()
        self.assertEqual(len(movimientos), 1)
        self.assertEqual(movimientos[0].nombre_producto, "Mouse")
        self.assertEqual(movimientos[0].tipo_movimiento, "Salida")
        self.assertEqual(movimientos[0].cantidad, "2")




if __name__ == '__main__':
    unittest.main()