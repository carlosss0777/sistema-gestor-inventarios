from app.repository.producto_repository import producto_repository
from app.model.producto import Producto

class ProductoService:
    def __init__(self, repository: producto_repository, lista_proveedores):
        """Inicializa el servicio de productos con un repositorio y una lista de proveedores. Carga los productos desde el repositorio al iniciar el servicio.

        Args:
            repository (producto_repository): Repositorio para manejar la persistencia de productos.
            lista_proveedores (list): Lista de proveedores para cargar los productos asociados.
        """
        self._repo = repository
        self.lista_productos: list[Producto] = self._repo.cargar(lista_proveedores)
    
    # =========================
    # VALIDACIONES DE DATOS
    # =========================
    def validar_nombre(self, nombre):
        """Valida el nombre del producto, asegurándose de que no esté vacío ni contenga solo espacios. Si el nombre es válido, se devuelve sin espacios adicionales.

        Args:
            nombre (str): El nombre del producto a validar.

        Raises:
            ValueError: Si el nombre es vacío o contiene solo espacios.
        
        Returns:
            str: El nombre del producto validado y sin espacios adicionales.
        """
        if nombre is None or nombre.strip() == "":
            raise ValueError("El nombre del producto no puede estar vacío")
        return nombre.strip()
    
    def validar_stock(self, stock):
        """Valida el stock del producto, asegurándose de que no esté vacío, sea numérico y no sea negativo. Si el stock es válido, se devuelve como un entero.

        Args:
            stock (str): El stock del producto a validar.
        
        Raises:
            ValueError: Si el stock es vacío, no es numérico o es negativo.
        
        Returns:
            int: El stock del producto validado como un entero.
        """
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
        """Valida el precio del producto, asegurándose de que no esté vacío, sea numérico y no sea negativo. Si el precio es válido, se devuelve como un float.

        Args:
            precio (str): El precio del producto a validar.

        Raises:
            ValueError: Si el precio es vacío, no es numérico o es negativo.

        Returns:
            float: El precio del producto validado como un float.
        """
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
        """Valida la descripción del producto, asegurándose de que no esté vacía.

        Args:
            descripcion (str): La descripción del producto a validar.

        Raises:
            ValueError: Si la descripción es vacía.

        Returns:
            str: La descripción del producto validada y sin espacios adicionales.
        """
        if descripcion is None or descripcion.strip() == "":
            raise ValueError("La descripción no puede estar vacía")
        return descripcion.strip()

    # =========================
    # REGISTRAR PRODUCTO
    # =========================

    def registrar_producto(self, nombre, stock, proveedor, precio, descripcion):
        """Registra un nuevo producto después de validar sus datos. Crea una instancia de Producto con los datos validados, la agrega a la lista de productos y guarda la lista actualizada en el repositorio.

        Args:
            nombre (str): El nombre del producto a registrar.
            stock (str): El stock del producto a registrar.
            proveedor (Proveedor): El proveedor asociado al producto a registrar.
            precio (str): El precio del producto a registrar.
            descripcion (str): La descripción del producto a registrar.
        
        Raises:
            ValueError: Si alguno de los datos del producto no es válido según las validaciones definidas.
        
        Returns:
            Producto: El producto registrado con los datos validados.
        """
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
        """Busca un producto por su nombre en la lista de productos. La búsqueda es insensible a mayúsculas y minúsculas.

        Args:
            nombre (str): El nombre del producto a buscar.

        Returns:
            Producto o None: El producto encontrado con el nombre especificado, o None si no se encuentra ningún producto con ese nombre.
        """
        for producto in self.lista_productos:
            if producto.nombre.lower() == nombre.lower():
                return producto

        return None
    
    # =========================
    # ELIMINAR PRODUCTO
    # =========================

    def eliminar_producto(self, nombre):
        """Elimina un producto de la lista de productos por su nombre. Primero busca el producto utilizando el método buscar_producto

        Args:
            nombre (str): El nombre del producto a eliminar.
        
        Raises:
            ValueError: Si no se encuentra ningún producto con el nombre especificado.
        """
        producto = self.buscar_producto(nombre)

        if producto is None:
            raise ValueError("Producto no encontrado")

        self.lista_productos.remove(producto)
        self._repo.guardar(self.lista_productos)
        
    # =========================
    # Validar duplicado
    # =========================
    def validar_duplicado(self, nombre_producto, proveedor):
        """Valida que no exista un producto con el mismo nombre y proveedor en la lista de productos. La validación es insensible a mayúsculas y minúsculas.

        Args:
            nombre_producto (str): El nombre del producto a validar.
            proveedor (Proveedor): El proveedor del producto a validar.

        Raises:
            ValueError: Si ya existe un producto con el mismo nombre y proveedor.
        """
        for producto in self.lista_productos:
            if producto.nombre.lower() == nombre_producto.lower() and producto.proveedor == proveedor:
                raise ValueError("Ya se ha registrado el mismo producto con el mismo proveedor")
            
    # =========================
    # Actualizar producto
    # =========================
    def actualizar_producto(self, producto:Producto, nombre, precio, descripcion, proveedor):
        """Actualiza los datos de un producto existente después de validar los nuevos datos. Modifica el nombre, precio, descripción y proveedor del producto, luego guarda la lista actualizada en el repositorio.

        Args:
            producto (Producto): El producto a actualizar.
            nombre (str): El nuevo nombre del producto.
            precio (str): El nuevo precio del producto.
            descripcion (str): La nueva descripción del producto.
            proveedor (Proveedor): El nuevo proveedor del producto.
    
        Raises:
            ValueError: Si alguno de los nuevos datos del producto no es válido según las validaciones definidas.
        """
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
        """Actualiza el precio de un producto existente después de validar el nuevo precio. Modifica el precio del producto y luego guarda la lista actualizada en el repositorio.

        Args:
            producto (Producto): El producto al que se le actualizará el precio.
            precio (str): El nuevo precio del producto.
        
        Raises:
            ValueError: Si el nuevo precio no es válido según las validaciones definidas.
        """
        nuevo_precio = self.validar_precio(precio)
        
        producto.precio = nuevo_precio
        
        self._repo.guardar(self.lista_productos)
            
    # =========================
    # Disminuir o aumentar stock
    # =========================
    def cambiar_stock(self, producto, cantidad, tipo_mov):
        """Actualiza el stock de un producto existente según el tipo de movimiento (Entrada o Salida). Si el tipo de movimiento es "Entrada", se aumenta el stock en la cantidad especificada; si es "Salida", se disminuye el stock en la cantidad especificada. Luego, guarda la lista actualizada en el repositorio.

        Args:
            producto (Producto): El producto al que se le actualizará el stock.
            cantidad (int): La cantidad por la cual se actualizará el stock.
            tipo_mov (str): El tipo de movimiento, que puede ser "Entrada" para aumentar el stock o "Salida" para disminuir el stock.
        """
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
        """Sincroniza la lista de productos actual con el repositorio, guardando los datos actualizados en el almacenamiento persistente. Este método se puede utilizar para asegurarse de que cualquier cambio realizado en la lista de productos se refleje en el repositorio.
        """
        self._repo.guardar(self.lista_productos)