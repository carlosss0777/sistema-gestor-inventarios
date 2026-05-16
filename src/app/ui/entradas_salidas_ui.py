# Modulo de registro movimientos de stock

from app.service.movimiento_service import movimiento_service
from app.service.producto_service import ProductoService
from app.ui.producto_ui import producto_ui
from datetime import datetime
from app.utils.tools import *

class entradas_salidas_ui:
    def __init__(self, movimiento_service: movimiento_service, producto_service: ProductoService, producto_ui: producto_ui):
        self.movimiento_service = movimiento_service
        self.producto_service = producto_service
        self.producto_ui = producto_ui
        
    def menu_es(self):
        while True:
            while True:
                limpiar_pantalla()
                print("\n---------------------------------------------")
                print("== REGISTRO DE ENTRADAS/SALIDAS DE STOCK ==")
                print("---------------------------------------------")
                print("1- Registrar entrada de stock")
                print("2- Registrar salida de stock")
                print("0- Cancelar registro")
            
                try:
                    opcion = int(input("Elige una opcion: "))
                    break
                except ValueError:
                    print("\nOpción no válida (debe ingresar un número)")
                    print("Intenta nuevamente...")
                    pausaLarga()
            
            match opcion:
                case 1:
                    limpiar_pantalla()
                    self.registrar_entrada()
                
                case 2:
                    limpiar_pantalla()
                    continue
                
                case 0:
                    print("\nCancelando registro...\n")
                    pausa()
                    break
                
                case _:
                    print("\nOpción no válida. Intenta nuevamente...")
                    pausa()
                    
    def registrar_entrada(self):
        limpiar_pantalla()
        print("\n------------------------------------------------------------")
        print("               -- REGISTRAR ENTRADA --")
        print("------------------------------------------------------------")
        productos = self.producto_service.get_productos()
        
        producto = self.producto_ui._seleccionar_producto("Selecciona el producto a editar (0 para cancelar): ")
        if producto is None:
            pausa()
            return
        
        nombre_producto = producto.nombre
        cantidad = self._pedir_cantidad()
        tipo_movimiento = "Entrada"
        fecha_hora = datetime.now()
        self.producto_service.cambiar_stock(producto, cantidad, tipo_movimiento)
        self.movimiento_service.registrar_movimiento(nombre_producto, tipo_movimiento, cantidad, fecha_hora)
        
        print("\nMovimiento registrado correctamente.")
        detener()
        
    def _pedir_cantidad(self):
        while True:
            cantidad = input("Ingresa la cantidad a añadir: ")
            
            try:
                return self.movimiento_service.validar_cantidad(cantidad)
            except ValueError as e:
                mensaje_error(e)
                pausaLarga()