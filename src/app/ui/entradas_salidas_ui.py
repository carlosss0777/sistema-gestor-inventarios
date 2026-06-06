# Modulo de registro movimientos de stock

from app.service.movimiento_service import movimiento_service
from app.service.producto_service import ProductoService
from app.ui.producto_ui import producto_ui
from datetime import datetime
from app.utils.tools import *

class entradas_salidas_ui:
    def __init__(self, movimiento_service: movimiento_service, producto_service: ProductoService, producto_ui: producto_ui):
        """
        Clase encargada de gestionar el registro de entradas y salidas de stock.

        Args:
            movimiento_service (movimiento_service): Servicio para gestionar movimientos de stock.
            producto_service (ProductoService): Servicio para gestionar productos.
            producto_ui (producto_ui): Interfaz de usuario para seleccionar productos. 
        """
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
        """
        Metodo principal para registrar un movimiento de stock (entrada o salida).

        Args:
            tipo_movimiento (str): Tipo de movimiento ("Entrada" o "Salida").
        """
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
        """
        Metodo para registrar una entrada de stock. Llama al método principal de registro de movimientos con el tipo "Entrada".
        """
        self._registrar_movimiento("Entrada")
         
    # =========================
    # REGISTRAR SALIDA
    # =========================
    def _registrar_salida(self):
        """
        Metodo para registrar una salida de stock. Llama al método principal de registro de movimientos con el tipo "Salida".
        """
        self._registrar_movimiento("Salida")
        
    # ======================================
    # PEDIR DE CANTIDAD A AUMENTAR/DISMINUIR
    # ======================================
    def _pedir_cantidad(self, tipo_movimiento, stock_actual):
        """
        Pide al usuario la cantidad a aumentar o disminuir del stock, dependiendo del tipo de movimiento. Valida que la cantidad sea un número positivo y, en caso de salida, que no supere el stock actual.

        Args:
            tipo_movimiento (str): Tipo de movimiento ("Entrada" o "Salida").
            stock_actual (int): Stock actual del producto (necesario para validar salidas).

        Returns:
            int: La cantidad validada.
        """
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