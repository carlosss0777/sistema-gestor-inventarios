from app.model.producto import Producto

class ProductoService:
    def __init__(self):
        self.lista_productos = []
    
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