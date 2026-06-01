from app.model.proveedor import Proveedor
import json
import os

# ruta donde se guardan los datos
RUTA_ARCHIVO = "data/proveedores.json"

class proveedor_repository:
    
    def guardar(self, lista_proveedores: list[Proveedor]):
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
    
    # retorna lista de objetos proveedor
    def cargar(self) -> list[Proveedor]:
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