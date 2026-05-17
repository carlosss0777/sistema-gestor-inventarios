# Formato de tablas

from tabulate import tabulate

# Tabla para los productos y sus datos
def tabla_productos(lista_productos):
    productos_data = []
    
    for producto in lista_productos:
        productos_data.append({
            "Nombre": producto.nombre,
            "Precio": f"${producto.precio}",
            "Stock": producto.stock,
            "Proveedor": producto.proveedor.nombre,
            "Descripcion": producto.descripcion
        })
        
    tabla = tabulate(productos_data, 
                     headers='keys', 
                     tablefmt='fancy_grid', 
                     stralign='center', 
                     numalign='center',
                     showindex=range(1, len(productos_data)+1)
                    )
    
    return tabla

# Tabla para ver el stock de los productos
def tabla_stock(lista_productos):
    productos_data = []
    
    for producto in lista_productos:
        estado = "Bajo" if producto.stock < 5 else "Alto"
        
        productos_data.append({
            "Nombre": producto.nombre,
            "Stock": producto.stock,
            "Nivel de stock": estado
        })
    
    tabla = tabulate(productos_data, 
                     headers='keys', 
                     tablefmt='fancy_grid', 
                     stralign='center', 
                     numalign='center',
                     showindex=range(1, len(productos_data)+1)
                    )
    
    return tabla

# Tabla para ver proveerdores y sus datos
def tabla_proveedores(lista_proveedores):
    proveedores_data = []
    
    for proveedor in lista_proveedores:
        proveedores_data.append({
            "Nombre": proveedor.nombre,
            "Telefono": proveedor.telefono,
            "Email": proveedor.email
        })
    
    tabla = tabulate(proveedores_data,
                     headers='keys', 
                     tablefmt='fancy_grid', 
                     stralign='center', 
                     numalign='center',
                     showindex=range(1, len(proveedores_data)+1)
                    )
    
    return tabla

# Tabla para ver los movimientos de stock
def tabla_movimientos(lista_movimientos):
    movimientos_data = []
    
    for movimiento in lista_movimientos:
        fecha = movimiento.fecha
        
        movimientos_data.append({
            "Producto": movimiento.nombre_producto,
            "Tipo de movimiento": movimiento.tipo_movimiento,
            "Cantidad": movimiento.cantidad,
            "Fecha": fecha.strftime('%d/%m/%Y'),
            "Hora": fecha.strftime('%H:%M')
        })
        
    tabla = tabulate(movimientos_data,
                     headers='keys', 
                     tablefmt='fancy_grid', 
                     stralign='center', 
                     numalign='center',
                     showindex=range(1, len(movimientos_data)+1)
                    )
    
    return tabla