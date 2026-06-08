# Pruebas a producto_service

from app.service.producto_service import ProductoService
from tests.fakes import ProductoRepositoryFalso
from app.model.proveedor import Proveedor
import unittest


class TestProductoService(unittest.TestCase):
    
    def setUp(self):
        # proveedor de prueba reutilizable en todos los tests
        self.proveedor = Proveedor("Logitech", "2222-2222", "logi@tech.dev")
        self.service   = ProductoService(ProductoRepositoryFalso(), [])
        
    # Prueba al metodo validar_nombre()
    def test_validar_nombre(self):
        # Nombres no validos
        
        # Nombre vacio
        nombre_vacio = ""
        with self.assertRaises(ValueError):
            self.service.validar_nombre(nombre_vacio)
            
        # Nombre valido
        nombre_valido = "Mouse Inalambrico"
        self.assertEqual(self.service.validar_nombre(nombre_valido), nombre_valido)
        
    # Prueba al metodo validar_stock()
    def test_validar_stock(self):
        # Stocks no valido
        
        # Stock vacio
        stock_vacio = ""
        with self.assertRaises(ValueError):
            self.service.validar_stock(stock_vacio)
            
        # Stock negativo
        stock_negativo = "-5"
        with self.assertRaises(ValueError):
            self.service.validar_stock(stock_negativo)
        
        # Stock no numerico
        stock_no_numerico = "diez"
        with self.assertRaises(ValueError):
            self.service.validar_stock(stock_no_numerico)
            
        # Stock negativo
        stock_negativo = "-3"
        with self.assertRaises(ValueError):
            self.service.validar_stock(stock_negativo)
            
        # Stock valido
        stock_valido = "10"
        self.assertEqual(self.service.validar_stock(stock_valido), 10)
        
    # Prueba al metodo validar_precio()
    def test_validar_precio(self):
        # Precios no validos

        # Precio vacio
        precio_vacio = ""
        with self.assertRaises(ValueError):
            self.service.validar_precio(precio_vacio)
            
        # Precio negativo
        precio_negativo = "-100.50"
        with self.assertRaises(ValueError):
            self.service.validar_precio(precio_negativo)
            
        # Precio no numerico
        precio_no_numerico = "cien"
        with self.assertRaises(ValueError):
            self.service.validar_precio(precio_no_numerico)
            
        # Precio valido
        precio_valido = "199.99"
        self.assertEqual(self.service.validar_precio(precio_valido), 199.99)

    # Prueba al metodo validar_descripcion()
    def test_validar_descripcion(self):
        # Descripcion no validas
        
        # Descripcion vacia
        descripcion_vacia = ""
        with self.assertRaises(ValueError):
            self.service.validar_descripcion(descripcion_vacia)
            
        # Descripcion valida
        descripcion_valida = "Mouse inalambrico con sensor de alta precision"
        self.assertEqual(self.service.validar_descripcion(descripcion_valida), descripcion_valida)
        
    # Prueba al metodo registrar_producto()
    def test_registrar_producto(self):
        # Registro de producto exitoso
        nombre = "Teclado Mecanico"
        stock = "20"
        precio = "89.99"
        descripcion = "Teclado mecanico con retroiluminacion RGB"
        
        producto = self.service.registrar_producto(nombre, 
                                                   stock, 
                                                   self.proveedor, 
                                                   precio, 
                                                   descripcion)
        
        self.assertEqual(producto.nombre, nombre)
        self.assertEqual(producto.stock, 20)
        self.assertEqual(producto.precio, 89.99)
        self.assertEqual(producto.descripcion, descripcion)
        self.assertEqual(producto.proveedor, self.proveedor)
        
    # Prueba al metodo get_productos()
    def test_get_productos(self):
        # Lista vacia de productos
        productos = self.service.get_productos()
        self.assertEqual(len(productos), 0)
        
        # Lista con productos
        # Se agrega un producto de prueba a la lista
        self.service.registrar_producto("Monitor 4K", "15", self.proveedor, "399.99", "Monitor 4K de 27 pulgadas")
        productos = self.service.get_productos()
        self.assertEqual(len(productos), 1)
        
    # Prueba al metodo buscar_producto()
    def test_buscar_producto(self):
        # Producto no encontrado
        producto = self.service.buscar_producto("Producto Inexistente")
        self.assertIsNone(producto)
        
        # Producto encontrado
        nombre = "Auriculares Bluetooth"
        self.service.registrar_producto(nombre, "30", self.proveedor, "59.99", "Auriculares Bluetooth con cancelacion de ruido")
        producto_encontrado = self.service.buscar_producto(nombre)
        self.assertIsNotNone(producto_encontrado)
        # Se verifica que el producto encontrado tenga el mismo nombre que el buscado
        self.assertEqual(producto_encontrado.nombre, nombre)
        
    # Prueba al metodo eliminar_producto()
    def test_eliminar_producto(self):
        producto = self.service.registrar_producto("Webcam HD", "25", self.proveedor, "79.99", "Webcam HD con micrófono integrado")
        
        # Eliminacion exitosa
        self.service.eliminar_producto(producto.nombre)
        # Se verifica que el producto ya no exista
        producto_eliminado = self.service.buscar_producto(producto.nombre)
        self.assertIsNone(producto_eliminado)
    
    # Prueba al metodo validar_duplicado()
    def test_validar_duplicado(self):
        nombre = "Iphone 13"
        self.service.registrar_producto(nombre, "50", self.proveedor, "999.99", "Smartphone de ultima generacion")
        
        # Producto duplicado
        with self.assertRaises(ValueError):
            self.service.validar_duplicado(nombre, self.proveedor)
            
        # Producto no duplicado
        nombre_no_duplicado = "Samsung Galaxy S21"
        proveedor_diferente = Proveedor("Samsung", "3333-3333", "samsung@tech.com")
        self.assertIsNone(self.service.validar_duplicado(nombre_no_duplicado, proveedor_diferente))
        
    # Prueba al metodo actualizar_producto()
    def test_actualizar_producto(self):
        # Datos iniciales del producto
        nombre_inicial = "Tablet Android"
        stock_inicial = "35"
        precio_inicial = "299.99"
        descripcion_inicial = "Tablet Android con pantalla de 10 pulgadas"
        producto = self.service.registrar_producto(nombre_inicial, 
                                                   stock_inicial, 
                                                   self.proveedor, 
                                                   precio_inicial, 
                                                   descripcion_inicial)
        
        # Se actualizan los datos
        nuevo_nombre = "Tablet Android Pro"
        nuevo_precio = "349.99"
        nueva_descripcion = "Tablet Android Pro con pantalla de 12 pulgadas"
        
        self.service.actualizar_producto(producto, nuevo_nombre, nuevo_precio, nueva_descripcion, self.proveedor)
        
        # Se verifica que los datos hayan sido actualizados
        self.assertEqual(producto.nombre, nuevo_nombre)
        self.assertEqual(producto.stock, 35)
        self.assertEqual(producto.precio, 349.99)
        self.assertEqual(producto.descripcion, nueva_descripcion)
        
    # Prueba al metodo actualizar_precio()
    def test_actualizar_precio(self):
        # Precio inicial del producto
        precio_inicial = "49.99"
        producto = self.service.registrar_producto("Mouse Gamer", "40", self.proveedor, precio_inicial, "Mouse gamer con luces RGB")
        
        # Se actualiza el precio
        nuevo_precio = "69.99"
        self.service.actualizar_precio(producto, nuevo_precio)
        
        # Se verifica que el precio haya sido actualizado
        self.assertEqual(producto.precio, 69.99)

         
if __name__ == '__main__':
    unittest.main()