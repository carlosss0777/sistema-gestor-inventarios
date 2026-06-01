from app.model.proveedor import Proveedor
from app.model.producto import Producto
import json
import os

# ruta donde se guardan los datos
RUTA_ARCHIVO = "data/productos.json"

class producto_repository:
    
    def guardar(self, lista_productos: list[Producto]):
        os.makedirs("data", exist_ok=True)
        
        datos = []
        
        for producto in lista_productos:
            datos.append({
                "nombre": producto.nombre,
                "stock": producto.stock,
                "proveedor": producto.proveedor.nombre,
                "precio": producto.precio,
                "descripcion": producto.descripcion
            })
            
        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
    
    # retorna lista de objetos producto
    def cargar(self, lista_proveedores: list[Proveedor]) -> list[Producto]:
        if not os.path.exists(RUTA_ARCHIVO):
            return []
        
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
            datos = json.load(f)
            
        productos = []
        
        for dato in datos:
            proveedor = next(
                (p for p in lista_proveedores if p.nombre == dato["proveedor"]), None
            )
            if proveedor is None:
                continue
            
            productos.append(Producto(dato["nombre"], 
                                        dato["stock"], 
                                        proveedor, 
                                        dato["precio"], 
                                        dato["descripcion"]))
            
        return productos