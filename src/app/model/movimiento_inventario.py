# Clase movimiento_inventario del sistema
class MovimientoInventario:
    # constructor de la clase movimiento_inventario
    def __init__(self, nombre_producto, tipo_movimiento, cantidad, fecha):
        self._nombre_producto = nombre_producto
        self._tipo_movimiento = tipo_movimiento
        self._cantidad = cantidad
        self._fecha = fecha

    # getter del nombre del producto
    @property
    def nombre_producto(self):
        return self._nombre_producto


    # getter del tipo de movimiento
    @property
    def tipo_movimiento(self):
        return self._tipo_movimiento


    # getter de la cantidad
    @property
    def cantidad(self):
        return self._cantidad


    # getter de la fecha
    @property
    def fecha(self):
        return self._fecha
