Algoritmo demoInventario
	Definir option, stock, stockProductos, numeroProductos, numeroProveedores, i, posicion, proveedorProducto Como Entero
	Definir proveedores, productos, nombreProducto, nombreProveedor Como Caracter
	Definir precio, preciosProductos Como Real
	Definir encontrado Como Logico
	
	Dimension productos[100] // lista de productos
	Dimension stockProductos[100] // lista de cantidades
	Dimension precioProductos[100] // lista de precios
	Dimension proveedores[10] // lista de proveedores
	Dimension proveedorProducto[100] // guarda índice del proveedor y producto
	
	Mientras option <> 6 Hacer
		Escribir "-- SISTEMA DE INVENTARIO --"
		Escribir "1. Registrar producto"
		Escribir "2. Ver stock"
		Escribir "3. Registrar proveedor"
		Escribir "4. Aumentar stock"
		Escribir "5. Disminuir stock"
		Escribir "6. Salir del sistema"
		Leer option
		
		Segun option Hacer
			1:
				// Modulo 1: registro de los productos
				Si numeroProveedores = 0 Entonces
					Escribir "Error: debe registrar proveedores primero"
					Esperar 500 Milisegundos
				Sino
					Repetir
						Escribir "Seleccione el número del proveedor (1 al ", numeroProveedores, ") o 0 para salir:"
						
						Para i <- 1 Hasta numeroProveedores Hacer
							Escribir i, "- ", proveedores[i]
						FinPara
						
						Leer posicion
					
						
						Si posicion <> 0 Y (posicion < 1 O posicion > numeroProveedores) Entonces
							Escribir "Error: opción inválida. Intente nuevamente"
							Esperar 500 Milisegundos
						FinSi
						
					Hasta Que (posicion >= 1 Y posicion <= numeroProveedores) O posicion = 0
					Si posicion = 0 Entonces
						Escribir "Cancelando selección..."
					SiNo
						Si numeroProductos < 100 Entonces
							Escribir "Ingrese el nombre del producto:"
							Leer nombreProducto
							
							encontrado <- Falso
							Si numeroProductos > 0 Entonces
								Para i <- 1 Hasta numeroProductos Hacer
									Si Mayusculas(productos[i]) = Mayusculas(nombreProducto) Y proveedorProducto[i] = posicion Entonces
										encontrado <- Verdadero
									FinSi							
								FinPara
							FinSi		
							
							Si encontrado = Verdadero Entonces
								Escribir "Error: Este producto ya existe con ese proveedor"
								Esperar 500 Milisegundos
							Sino						
								numeroProductos <- numeroProductos + 1
								
								productos[numeroProductos] <- nombreProducto
								proveedorProducto[numeroProductos] <- posicion 
								
								Escribir "Ingresar cantidad inicial (stock):"
								Leer stockProductos[numeroProductos]
								
								Escribir "Ingresar precio del producto:"
								Leer precioProductos[numeroProductos]
								
								Escribir "---- Producto: ",nombreProducto," ----"
								Escribir "---- Proveedor: ", proveedores[posicion]," registrado con éxito ----"
								Escribir ""
								Esperar 500 Milisegundos
							FinSi				
						Sino
							Escribir "Inventario lleno."
						FinSi
					FinSi
				FinSi   
				
			
				
			2:			
				// Modulo 2: Consultar stock actual
				
				
				
			3:
				// Modulo 3: registro de los proveedores
				Si numeroProveedores > 10 Entonces
					Escribir "Maximo de proveedores alcanzado"
					
				SiNo
					Escribir "Ingresa el nombre del proveedor: "
					Leer nombreProveedor
					
					encontrado <- Falso
					Si numeroProveedores > 0 Entonces
						Para i <- 1 Hasta numeroProveedores Hacer
							Si Mayusculas(proveedores[i]) = Mayusculas(nombreProveedor) Entonces
								encontrado <- Verdadero
							FinSi
						FinPara	
					FinSi
					
					Si encontrado = Verdadero Entonces
						Escribir ""
						Escribir "Error: El proveedor ya ha sido registrado"
						Escribir ""
						
					SiNo
						numeroProveedores = numeroProveedores + 1
						proveedores[numeroProveedores] <- nombreProveedor
						Escribir ""
						Escribir "---- Proveedor registrado con éxito ----"
						Escribir ""
					FinSi
				FinSi
				
			4:
				// Modulo 4: aumentar stock de productos
				Si numeroProductos == 0 Entonces
					Escribir "No se han registrado productos"
					
				SiNo
					Repetir
						Escribir "Seleccione el indice del producto (1 al ", numeroProductos, ") o 0 para salir:"
						
						Para i <- 1 Hasta numeroProductos Hacer
							Escribir i, "- ", productos[i]," - ",proveedores[proveedorProducto[i]], " (Stock: ", stockProductos[i], ")"
						FinPara
						
						Leer posicion
						Si posicion <> 0 Y (posicion <  numeroProductos O posicion > numeroProductos) Entonces
							Escribir "Error: opción inválida. Intente nuevamente"
							Escribir ""
						FinSi							
					Hasta Que (posicion >= 1 Y posicion <= numeroProductos) O posicion = 0
					
					Si posicion = 0 Entonces
						Escribir "Cancelando selección..."
					SiNo
						Escribir "Has seleccionado: ", productos[posicion]
						Escribir "Stock actual: ", stockProductos[posicion]
						Escribir "Cantidad a añadir:"
						Leer stock
						
						stockProductos[posicion] <- stockProductos[posicion] + stock
						Escribir "------ Nuevo stock: ", stockProductos[posicion]," ----------"
						Escribir ""
						Esperar 500 Milisegundos
						
					FinSi					
				FinSi
				
			5:
				// Modulo 5: restar stock de productos
				Si numeroProductos = 0 Entonces
					Escribir "No hay productos registrados aun"
				Sino
					Escribir "Seleccione el numero del producto (1 al ", numeroProductos, "):"
					Para i <- 1 Hasta numeroProductos Hacer
						Escribir i, ". ", productos[i], " (Stock: ", stockProductos[i], ")"
					FinPara
					
					Leer posicion
					
					Si posicion >= 1 Y posicion <= numeroProductos Entonces
						Escribir "Has seleccionado: ", productos[posicion]
						Escribir "Stock actual: ", stockProductos[posicion]
						Escribir "Cantidad a restar:"
						Leer stock
						
						Si stock <= stockProductos[posicion] Entonces
							stockProductos[posicion] <- stockProductos[posicion] - stock
							Escribir "------ Nuevo stock: ", stockProductos[posicion]," ----------"
							Escribir ""
							Esperar 500 Milisegundos
						Sino
							Escribir "Error: No hay suficiente stock disponible"
							Escribir ""
						FinSi
					Sino
						Escribir "Error: El numero de producto no es válido"
					FinSi
				FinSi
				
			6:
				// Salida del sistema
				Escribir "Saliendo del sistema..."
				
			De Otro Modo:
				Escribir "Opcion no valida. Intenta nuevamente..."
				Escribir ""
		FinSegun
	FinMientras
FinAlgoritmo