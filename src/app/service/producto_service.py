from app.repository.producto_repository import producto_repository
from app.model.producto import Producto

class ProductoService:
    def __init__(self, repository: producto_repository, lista_proveedores):
        self._repo = repository
        self.lista_productos: list[Producto] = self._repo.cargar(lista_proveedores)
    
    # =========================
    # VALIDACIONES
    # =========================
    def validar_nombre(self, nombre):
        if nombre is None or nombre.strip() == "":
            raise ValueError("El nombre del producto no puede estar vacío")
        return nombre.strip()
    
    def validar_stock(self, stock):
        if stock is None or str(stock).strip() == "":
            raise ValueError("El stock no puede estar vacío")
        try:
            stock_int = int(stock)
        except ValueError:
            raise ValueError("El stock debe ser numérico")
        if stock_int < 0:
            raise ValueError("El stock no puede ser negativo")
        return stock_int

    def validar_precio(self, precio):
        if precio is None or str(precio).strip() == "":
            raise ValueError("El precio no puede estar vacío")
        try:
            precio_float = float(precio)
        except ValueError:
            raise ValueError("El precio debe ser numérico")
        if precio_float < 0:
            raise ValueError("El precio no puede ser negativo")
        return precio_float

    def validar_descripcion(self, descripcion):
        if descripcion is None or descripcion.strip() == "":
            raise ValueError("La descripción no puede estar vacía")
        return descripcion.strip()

    # =========================
    # REGISTRAR PRODUCTO
    # =========================

    def registrar_producto(self, nombre, stock, proveedor, precio, descripcion):

        nombre = self.validar_nombre(nombre)
        stock = self.validar_stock(stock)
        precio = self.validar_precio(precio)
        descripcion = self.validar_descripcion(descripcion)

        producto = Producto(
            nombre,
            stock,
            proveedor,
            precio,
            descripcion
            )

        self.lista_productos.append(producto)
        
        self._repo.guardar(self.lista_productos)
        
        return producto

    # =========================
    # OBTENER PRODUCTOS
    # =========================

    def get_productos(self):
        return self.lista_productos

    # =========================
    # BUSCAR PRODUCTO
    # =========================

    def buscar_producto(self, nombre):
        for producto in self.lista_productos:
            if producto.nombre.lower() == nombre.lower():
                return producto

        return None
    
    # =========================
    # ELIMINAR PRODUCTO
    # =========================

    def eliminar_producto(self, nombre):
        producto = self.buscar_producto(nombre)

        if producto is None:
            raise ValueError("Producto no encontrado")

        self.lista_productos.remove(producto)
        self._repo.guardar(self.lista_productos)
        
    # =========================
    # Validar duplicado
    # =========================
    
    def validar_duplicado(self, nombre_producto, proveedor):
        for producto in self.lista_productos:
            if producto.nombre.lower() == nombre_producto.lower() and producto.proveedor == proveedor:
                raise ValueError("Ya se ha registrado el mismo producto con el mismo proveedor")
            
    # =========================
    # Actualizar producto
    # =========================
    def actualizar_producto(self, producto:Producto, nombre, precio, descripcion, proveedor):
        nuevo_nombre = self.validar_nombre(nombre)
        nuevo_precio = self.validar_precio(precio)
        nueva_descripcion = self.validar_descripcion(descripcion)
        
        producto.nombre = nuevo_nombre
        producto.precio = nuevo_precio
        producto.descripcion = nueva_descripcion
        producto.proveedor = proveedor
        
        self._repo.guardar(self.lista_productos)
        
        return producto
    
    # =========================
    # Actualizar precio
    # =========================
    def actualizar_precio(self, producto:Producto, precio):
        nuevo_precio = self.validar_precio(precio)
        
        producto.precio = nuevo_precio
        
        self._repo.guardar(self.lista_productos)
            
    # =========================
    # Disminuir o aumentar stock
    # =========================
    
    def cambiar_stock(self, producto, cantidad, tipo_mov):
        if tipo_mov == "Entrada":
            stock_actual = producto.stock
        
            nuevo_stock = stock_actual + cantidad
            
            producto.stock = nuevo_stock
            
        elif tipo_mov == "Salida":
            stock_actual = producto.stock
        
            nuevo_stock = stock_actual - cantidad
            
            producto.stock = nuevo_stock
            
        self._repo.guardar(self.lista_productos)
            
    # =========================
    # Sincronizar JSON
    # =========================
    
    def sincronizar_json(self):
        self._repo.guardar(self.lista_productos)