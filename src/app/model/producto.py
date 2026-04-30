# Clase producto del sistema
class Producto:
    def __init__(self, nombre, stock, proveedor, precio, descripcion):
        self._nombre = nombre
        self._stock = stock
        self._proveedor = proveedor
        self._precio = precio
        self._descripcion = descripcion

    # GETTER
    @property
    def nombre(self):
        return self._nombre

    # SETTER
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise ValueError("El stock no puede ser negativo")
        self._stock = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor

    @property
    def proveedor(self):
        return self._proveedor

    @proveedor.setter
    def proveedor(self, valor):
        self._proveedor = valor

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor):
        self._descripcion = valor