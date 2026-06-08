# Pruebas a movimiento_service

from app.service.movimiento_service import movimiento_service
from tests.fakes import MovimientoRepositoryFalso
import unittest


class TestMovimientoService(unittest.TestCase):
    # comandos para ejecutar las pruebas: 
    # cd src/
    # python -m unittest tests.test_movimiento_service
    
    def setUp(self):
        self.service = movimiento_service(MovimientoRepositoryFalso())

    # pruebas de los metodos


if __name__ == '__main__':
    unittest.main()