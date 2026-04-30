# Validaciones para los movimientos

from app.model.movimiento_inventario import MovimientoInventario

class movimiento_service:
    def __init__(self):
        self.lista_movimientos = []
        
    # validacion de la cantidad
    def validar_cantidad(self, cantidad):
        if cantidad is None or cantidad.strip() == "":
            raise ValueError("La cantidad no puede estar vacia")
        
        try:
            cantidad_int = int(cantidad)
        except ValueError:
            raise ValueError("La cantidad debe ser numerica")
        
        if cantidad_int < 0:
            raise ValueError("La cantidad no puede ser negativa")
        
        return cantidad_int
        
    # validacion del stock negativo
    def validar_salida(self, cantidad, stock_actual):
        cantidad_int = self.validar_cantidad(cantidad)
        
        if cantidad_int > stock_actual:
            raise ValueError("No hay suficiente stock disponible")
        
        return cantidad_int
        
    # registro del movimiento
    def registrar_movimiento(self, nombre_producto, tipo_movimiento, cantidad, fecha):
        movimiento = MovimientoInventario(nombre_producto, tipo_movimiento, cantidad, fecha)
        
        self.lista_movimientos.append(movimiento)
        
    def get_movimientos(self):
        return self.lista_movimientos