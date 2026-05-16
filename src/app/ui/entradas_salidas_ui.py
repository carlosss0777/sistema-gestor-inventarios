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
                    self._registrar_entrada()
                
                case 2:
                    limpiar_pantalla()
                    self._registrar_salida()
                
                case 0:
                    print("\nCancelando registro...\n")
                    pausa()
                    break
                
                case _:
                    print("\nOpción no válida. Intenta nuevamente...")
                    pausa()
    
    # ============================================
    # METODO PRINCIPAL PARA REGISTRO DE MOVIMIENTOS
    # =============================================
    def _registrar_movimiento(self, tipo_movimiento):
        limpiar_pantalla()
    
        print("\n------------------------------------------------------------")
        print(f"        -- REGISTRAR {tipo_movimiento.upper()} --")
        print("------------------------------------------------------------")
    
        producto = self.producto_ui._seleccionar_producto("Selecciona el producto (0 para cancelar): ")
        if producto is None:
            pausa()
            return
    
        cantidad = self._pedir_cantidad(tipo_movimiento, producto.stock)
        fecha_hora = datetime.now()
    
        self.producto_service.cambiar_stock(producto, cantidad, tipo_movimiento)
        self.movimiento_service.registrar_movimiento(producto, tipo_movimiento, cantidad, fecha_hora)
    
        print("\nMovimiento registrado correctamente.")
        detener()
              
    # =========================
    # REGISTRAR ENTRADA
    # =========================      
    def _registrar_entrada(self):
        self._registrar_movimiento("Entrada")
         
    # =========================
    # REGISTRAR SALIDA
    # =========================
    def _registrar_salida(self):
        self._registrar_movimiento("Salida")
        
    # ======================================
    # PEDIR DE CANTIDAD A AUMENTAR/DISMINUIR
    # ======================================
    def _pedir_cantidad(self, tipo_movimiento, stock_actual):
        while True:
            cantidad = input("Ingresa la cantidad a añadir: " if tipo_movimiento == "Entrada" else "Ingresa la cantidad a restar: "
            )

            try:
                if tipo_movimiento == "Entrada":
                    return self.movimiento_service.validar_cantidad(cantidad)
                else:
                    return self.movimiento_service.validar_salida(cantidad, stock_actual)
            except ValueError as e:
                mensaje_error(e)
                pausaLarga()