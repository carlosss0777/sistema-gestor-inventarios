# Clase producto del sistema
class Producto:
    # Constructor de la clase producto
    def __init__(self, nombre, stock, proveedor, precio, descripcion):
        self._nombre = nombre
        self._stock = stock
        self._proveedor = proveedor
        self._precio = precio
        self._descripcion = descripcion

    # getter del nombre del producto
    @property
    def nombre(self):
        return self._nombre

    # setter del nombre del producto
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    # getter del stock del producto
    @property
    def stock(self):
        return self._stock

    # setter del stock del producto
    @stock.setter
    def stock(self, valor):
        self._stock = valor

    # getter del precio del producto
    @property
    def precio(self):
        return self._precio

    # setter del precio del producto
    @precio.setter
    def precio(self, valor):
        self._precio = valor

    # getter del proveedor del producto
    @property
    def proveedor(self):
        return self._proveedor

    # setter del proveedor del producto
    @proveedor.setter
    def proveedor(self, valor):
        self._proveedor = valor

    # getter de la descripcion del producto
    @property
    def descripcion(self):
        return self._descripcion

    # setter de la descripcion del producto
    @descripcion.setter
    def descripcion(self, valor):
        self._descripcion = valor
        
    # Metodo para mostrar el nombre del producto al imprimirlo
    def __str__(self):
        return self.nombre