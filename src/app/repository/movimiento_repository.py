from app.model.movimiento_inventario import MovimientoInventario
from datetime import datetime
import json
import os

# ruta donde se guardan los datos
RUTA_ARCHIVO = "data/movimientos.json"

class movimiento_repository:
    
    # Guardar la lista de movimientos en el JSON
    def guardar(self, lista_movimientos: list[MovimientoInventario]):
        os.makedirs("data", exist_ok=True)
        """Guarda la lista de movimientos en un archivo JSON. Cada movimiento se guarda como un diccionario con sus atributos.

        Args:
            lista_movimientos (list[MovimientoInventario]): Lista de objetos MovimientoInventario a guardar
        
        Returns:
            None
        """
        datos = []
        
        for movimiento in lista_movimientos:
            if isinstance(movimiento.nombre_producto, str):
                nombre = movimiento.nombre_producto
            else:
                nombre = movimiento.nombre_producto.nombre
                
            datos.append({
                "nombre_producto": nombre,
                "tipo_movimiento": movimiento.tipo_movimiento,
                "cantidad": movimiento.cantidad,
                "fecha": movimiento.fecha.strftime("%d-%m-%Y %H:%M:%S")
            })
            
        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
    
    # Cargar la lista de movimientos desde el JSON
    def cargar(self) -> list[MovimientoInventario]:
        """Carga la lista de movimientos desde un archivo JSON. Cada movimiento se convierte en un objeto MovimientoInventario.

        Returns:
            list[MovimientoInventario]: Lista de objetos MovimientoInventario cargados desde el archivo JSON
        """
        if not os.path.exists(RUTA_ARCHIVO):
            return []
        
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
            datos = json.load(f)
            
        movimientos = []
        
        for dato in datos:
            fecha = datetime.strptime(dato["fecha"], "%d-%m-%Y %H:%M:%S")
            
            mov = MovimientoInventario(dato["nombre_producto"], 
                                     dato["tipo_movimiento"], 
                                     dato["cantidad"], 
                                     fecha)
            movimientos.append(mov)
            
        return movimientos