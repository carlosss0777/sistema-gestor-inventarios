# Clase movimiento_inventario del sistema
class MovimientoInventario:
    def __init__(self, nombre_producto, tipo_movimiento, cantidad, fecha):
        self._nombre_producto = nombre_producto
        self._tipo_movimiento = tipo_movimiento
        self._cantidad = cantidad
        self._fecha = fecha

    # Nombre del producto
    @property
    def nombre_producto(self):
        return self._nombre_producto


    # Tipo de movimiento
    @property
    def tipo_movimiento(self):
        return self._tipo_movimiento


    # Cantidad
    @property
    def cantidad(self):
        return self._cantidad


    # Fecha
    @property
    def fecha(self):
        return self._fecha
