from app.model.proveedor import Proveedor
import json
import os

# ruta donde se guardan los datos
RUTA_ARCHIVO = "data/proveedores.json"

class proveedor_repository:
    
    # Guardar la lista de proveedores en el JSON
    def guardar(self, lista_proveedores: list[Proveedor]):
        """Guarda la lista de proveedores en un archivo JSON. Cada proveedor se guarda como un diccionario con sus atributos.

        Args:
            lista_proveedores (list[Proveedor]): Lista de objetos Proveedor a guardar

        Returns:
            None
        """
        os.makedirs("data", exist_ok=True)
        
        datos = []
        
        for proveedor in lista_proveedores:
            datos.append({
                "nombre": proveedor.nombre,
                "telefono": proveedor.telefono,
                "email": proveedor.email,
                "activo": proveedor.activo
            })
            
        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
    
    # Cargar la lista de proveedores desde el JSON
    def cargar(self) -> list[Proveedor]:
        """Carga la lista de proveedores desde un archivo JSON. Cada proveedor se convierte en un objeto Proveedor.

        Returns:
            list[Proveedor]: Lista de objetos Proveedor cargados desde el archivo JSON
        """
        if not os.path.exists(RUTA_ARCHIVO):
            return []
        
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
            datos = json.load(f)
            
        proveedores = []
        
        for dato in datos:
            p = Proveedor(dato["nombre"], dato["telefono"], dato["email"])
            p.activo = dato.get("activo", True)
            proveedores.append(p)
            
        return proveedores