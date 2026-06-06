from app.repository.proveedor_repository import proveedor_repository
from app.model.proveedor import Proveedor
import re

class ProveedorService:
    def __init__(self, repository: proveedor_repository):
        """Inicializa el servicio de proveedores con un repositorio específico. Carga la lista de proveedores desde el repositorio y la almacena en memoria para su uso posterior. También se pueden cargar datos de prueba si es necesario.

        Args:
            repository (proveedor_repository): El repositorio que se utilizará para cargar y guardar los datos de proveedores.
        """
        self._repo = repository
        self.lista_proveedores: list[Proveedor] = self._repo.cargar()
        # self.datos_prueba()

    # =========================
    # Validaciones de datos
    # =========================
    def validar_nombre(self, nombre):
        """Valida que el nombre del proveedor no esté vacío ni sea nulo.

        Args:
            nombre (str): El nombre del proveedor a validar.
        
        Raises:
            ValueError: Si el nombre del proveedor es nulo o está vacío.
        
        Returns:
            str: El nombre del proveedor validado y sin espacios en blanco al inicio o al final.
        """
        if nombre is None or nombre.strip() == "":
            raise ValueError("El nombre del proveedor no puede estar vacío")

        return nombre.strip()

    def validar_telefono(self, telefono):
        """Valida que el teléfono del proveedor tenga el formato correcto.

        Args:
            telefono (str): El teléfono del proveedor a validar.

        Raises:
            ValueError: Si el teléfono no tiene el formato correcto.

        Returns:
            str: El teléfono del proveedor validado.
        """
        if telefono is None or telefono.strip() == "":
            raise ValueError("El telefono no puede estar vacio")
    
        patron = r"^\d{4}-\d{4}$"
    
        if not re.match(patron, telefono):
            raise ValueError("El telefono debe tener el formato 1234-5678")

        return telefono
    
    def validar_email(self, email):
        """Valida que el email del proveedor tenga el formato correcto.

        Args:
            email (str): El email del proveedor a validar.

        Raises:
            ValueError: Si el email no tiene el formato correcto.

        Returns:
            str: El email del proveedor validado.
        """
        if email is None or email.strip() == "":
            raise ValueError("El email no puede estar vacío")

        if "@" not in email or "." not in email:
            raise ValueError("El email no es válido")

        return email.strip()

    # =========================
    # REGISTRAR PROVEEDOR
    # =========================
    def registrar_proveedor(self, nombre, telefono, email):
        """Registra un nuevo proveedor después de validar los datos de entrada. Crea una instancia de Proveedor con los datos validados, la agrega a la lista de proveedores y luego guarda la lista actualizada en el repositorio.

        Args:
            nombre (str): El nombre del proveedor a registrar.
            telefono (str): El teléfono del proveedor a registrar.
            email (str): El email del proveedor a registrar.
        
        Raises:
            ValueError: Si alguno de los datos de entrada no es válido según las validaciones definidas.
        """
        nombre = self.validar_nombre(nombre)
        telefono = self.validar_telefono(telefono)
        email = self.validar_email(email)

        proveedor = Proveedor(
            nombre,
            telefono,
            email
        )

        self.lista_proveedores.append(proveedor)
        
        self._repo.guardar(self.lista_proveedores)
        
        return proveedor

    # =========================
    # OBTENER PROVEEDORES
    # =========================
    def get_all(self):
        """Obtiene la lista completa de proveedores, incluyendo aquellos que están marcados como inactivos. Este método devuelve la lista completa sin filtrar por el estado de actividad de los proveedores.
        """
        return self.lista_proveedores

    def get_proveedores(self):
        """
        Obtiene la lista de proveedores activos, filtrando aquellos que están marcados como inactivos. Este método devuelve solo los proveedores que tienen el atributo "activo" establecido en True, lo que indica que están activos y disponibles para su uso.
        """
        proveedores_activos = []
        for proveedor in self.lista_proveedores:
            if proveedor.activo:
                proveedores_activos.append(proveedor)
                
        return proveedores_activos

    # =========================
    # BUSCAR PROVEEDOR
    # =========================
    def buscar_proveedor(self, nombre):
        """
        Busca un proveedor por su nombre en la lista de proveedores.

        Args:
            nombre (str): El nombre del proveedor a buscar.

        Returns:
            Proveedor o None: El proveedor encontrado con el nombre especificado, o None si no se encuentra ningún proveedor con ese nombre.
        """
        for proveedor in self.lista_proveedores:
            if proveedor.nombre.lower() == nombre.lower():
                return proveedor

        return None
        
    # =========================
    # ELIMINAR PROVEEDOR
    # =========================
    def eliminar_proveedor(self, nombre):
        """
        Elimina un proveedor de la lista de proveedores por su nombre. En lugar de eliminar físicamente el proveedor de la lista, este método marca al proveedor como inactivo estableciendo su atributo "activo" en False. Luego, guarda la lista actualizada en el repositorio.

        Args:
            nombre (str): El nombre del proveedor a eliminar.

        Raises:
            ValueError: Si no se encuentra ningún proveedor con el nombre especificado.
        """
        proveedor = self.buscar_proveedor(nombre)

        if proveedor is None:
            raise ValueError("Proveedor no encontrado")

        proveedor.activo = False
        self._repo.guardar(self.lista_proveedores)
        
    # =========================
    # VALIDAR DUPLICADO
    # =========================
    def validar_duplicado(self, nombre_proveedor):
        """
        Valida que no exista un proveedor con el mismo nombre en la lista de proveedores. La validación es insensible a mayúsculas y minúsculas.

        Args:
            nombre_proveedor (str): El nombre del proveedor a validar.

        Raises:
            ValueError: Si ya existe un proveedor con el mismo nombre.
        """
        for proveedor in self.lista_proveedores:
            if proveedor.nombre.lower() == nombre_proveedor.lower():
                raise ValueError("Ya se ha registrado un proveedor con el mismo nombre")
          
    # =========================
    # Actualizar proveedor
    # =========================
    def actualizar_proveedor(self, proveedor:Proveedor, nombre, telefono, email, producto_service=None):
        """
        Actualiza los datos de un proveedor existente después de validar los nuevos datos de entrada.

        Args:
            proveedor (Proveedor): El proveedor que se va a actualizar. 
            nombre (str): El nuevo nombre del proveedor.
            telefono (str): El nuevo teléfono del proveedor.
            email (str): El nuevo email del proveedor.
            producto_service (ProductoService, opcional): El servicio de productos para sincronizar los datos en caso de que el proveedor esté asociado a algún producto. Si se proporciona, se llamará al método sincronizar_json() del servicio de productos después de actualizar el proveedor para asegurarse de que los cambios se reflejen en los productos asociados. Por defecto, es None.

        Raises:
            ValueError: Si alguno de los nuevos datos de entrada no es válido según las validaciones definidas. 
        """
        nuevo_nombre = self.validar_nombre(nombre)
        nuevo_telefono = self.validar_telefono(telefono)
        nuevo_email = self.validar_email(email)
        
        proveedor.nombre = nuevo_nombre
        proveedor.telefono = nuevo_telefono
        proveedor.email = nuevo_email
        
        self._repo.guardar(self.lista_proveedores)
        
        if producto_service:
            producto_service.sincronizar_json()
            
        return proveedor