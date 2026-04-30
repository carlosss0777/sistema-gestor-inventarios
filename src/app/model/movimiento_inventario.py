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

    @nombre_producto.setter
    def nombre_producto(self, valor):
        self._nombre_producto = valor

    # Tipo de movimiento
    @property
    def tipo_movimiento(self):
        return self._tipo_movimiento

    @tipo_movimiento.setter
    def tipo_movimiento(self, valor):
        if valor.lower() not in ["entrada", "salida"]:
            raise ValueError("El tipo de movimiento debe ser 'entrada' o 'salida'")
        self._tipo_movimiento = valor.lower()

    # Cantidad
    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        if valor <= 0:
            raise ValueError("La cantidad debe ser mayor que 0")
        self._cantidad = valor

    # Fecha
    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        self._fecha = valor