# Validaciones para los movimientos

from app.model.movimiento_inventario import MovimientoInventario
from app.repository.movimiento_repository import movimiento_repository
from datetime import datetime

class movimiento_service:
    def __init__(self, repository: movimiento_repository):
        """
        Inicializa el servicio de movimientos de inventario con un repositorio específico. Carga la lista de movimientos desde el repositorio y la almacena en memoria para su uso posterior.

        Args:
            repository (movimiento_repository): El repositorio que se utilizará para cargar y guardar los datos de movimientos de inventario.
        """
        self._repo = repository
        self.lista_movimientos: list[MovimientoInventario] = self._repo.cargar()
        
    # validacion de la cantidad
    def validar_cantidad(self, cantidad):
        """
        Valida que la cantidad de un movimiento de inventario sea un número entero positivo.

        Args:
            cantidad (str): La cantidad a validar, que se espera que sea una cadena que representa un número entero.

        Raises:
            ValueError: Si la cantidad es nula, vacía, no es un número entero o es negativa. 
        
        Returns:
            int: La cantidad validada como un número entero positivo.
        """
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
        """
        Valida que la cantidad de un movimiento de salida no exceda el stock actual disponible. 

        Args:
            cantidad (str): La cantidad a validar, que se espera que sea una cadena que representa un número entero.
            stock_actual (int): El stock actual disponible del producto.
        
        Raises:
            ValueError: Si la cantidad es mayor que el stock actual disponible.
        """
        cantidad_int = self.validar_cantidad(cantidad)
        
        if cantidad_int > stock_actual:
            raise ValueError("No hay suficiente stock disponible")
        
        return cantidad_int
        
    # registro del movimiento
    def registrar_movimiento(self, nombre_producto, tipo_movimiento, cantidad, fecha_hora):
        """
        Registra un nuevo movimiento de inventario con los datos proporcionados. Crea una instancia de MovimientoInventario con el nombre del producto, el tipo de movimiento, la cantidad y la fecha y hora del movimiento. Luego, agrega el movimiento a la lista de movimientos y guarda la lista actualizada en el repositorio.

        Args:
            nombre_producto (str): El nombre del producto asociado al movimiento de inventario.
            tipo_movimiento (str): El tipo de movimiento, que puede ser "Entrada" para aumentar el stock o "Salida" para disminuir el stock.
            cantidad (str): La cantidad del movimiento, que se espera que sea una cadena que representa un número entero.
            fecha_hora (datetime): La fecha y hora en que se registra el movimiento de inventario.

        Returns:
            MovimientoInventario: El movimiento de inventario registrado con los datos proporcionados.
        """
        fecha_hora = datetime.now()
        
        movimiento = MovimientoInventario(nombre_producto, tipo_movimiento, cantidad, fecha_hora)
        
        self.lista_movimientos.append(movimiento)
        self._repo.guardar(self.lista_movimientos)
        return movimiento
        
    def get_movimientos(self):
        """
        Obtiene la lista completa de movimientos de inventario registrados. Este método devuelve la lista completa de movimientos sin aplicar ningún filtro, lo que permite acceder a todos los movimientos registrados en el sistema.

        Returns:
            list[MovimientoInventario]: La lista completa de movimientos de inventario registrados.
        """
        return self.lista_movimientos