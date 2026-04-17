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
					Escribir "------------------------------------------"
					Escribir "Error: debe registrar proveedores primero"
					Escribir "------------------------------------------"
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
						Escribir "-------------------------"
						Escribir "Cancelando selección..."
						Escribir "-------------------------"
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
								Escribir "-------------------------------------------------"
								Escribir "Error: Este producto ya existe con ese proveedor"
								Escribir "-------------------------------------------------"
								Esperar 500 Milisegundos
							Sino						
								numeroProductos <- numeroProductos + 1
								
								productos[numeroProductos] <- nombreProducto
								proveedorProducto[numeroProductos] <- posicion 
								
								Escribir "Ingresar cantidad inicial (stock):"
								Leer stockProductos[numeroProductos]
								
								Escribir "Ingresar precio del producto:"
								Leer precioProductos[numeroProductos]
								
								Escribir ""
								Escribir "---- Producto: ",nombreProducto," ----"
								Escribir "---- Proveedor: ", proveedores[posicion]," registrado con éxito ----"
								Escribir ""
								Esperar 500 Milisegundos
							FinSi				
						Sino
							Escribir "-------------------"
							Escribir "Inventario lleno."
							Escribir "-------------------"
						FinSi
					FinSi
				FinSi   
				
			2:			
				// Modulo 2: Consultar stock actual
				Si numeroProductos == 0 Entonces
					Escribir "---------------------------------"
					Escribir "No hay productos registrados"
					Escribir "---------------------------------"
					
				SiNo
					Para  i <- 1 Hasta numeroProductos Con Paso 1 Hacer
						Escribir "--- PRODUCTO ", i, " ---"
						Escribir "Nombre del producto: ", productos[i]
						Escribir "Proveedor del producto: ", proveedores[proveedorProducto[i]]
						Escribir "Stock del producto: ", stockProductos[i]
						Escribir "Precio del producto: ", precioProductos[i]
						Escribir "---------------------------------------------------"
						Escribir ""
					FinPara
				FinSi
				
			3:
				// Modulo 3: registro de los proveedores
				Si numeroProveedores > 10 Entonces
					Escribir "---------------------------------"
					Escribir "Maximo de proveedores alcanzado"
					Escribir "---------------------------------"
					
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
						Escribir "--------------------------------------------"
						Escribir "Error: El proveedor ya ha sido registrado"
						Escribir "--------------------------------------------"
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
					Escribir "--------------------------------"
					Escribir "No se han registrado productos"
					Escribir "--------------------------------"
					
				SiNo
					Repetir
						Escribir "Seleccione el índice del producto (1 al ", numeroProductos, ") o 0 para salir:"
						
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
						Escribir "-------------------------"
						Escribir "Cancelando selección..."
						Escribir "-------------------------"
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
					Escribir "--------------------------------"
					Escribir "No hay productos registrados aún"
					Escribir "--------------------------------"
				Sino
					Escribir "Seleccione el número del producto (1 al ", numeroProductos, "):"
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
							Escribir "--------------------------------------------"
							Escribir "Error: No hay suficiente stock disponible"
							Escribir "--------------------------------------------"
						FinSi
					Sino
						Escribir "--------------------------------------------"
						Escribir "Error: El número de producto no es válido"
						Escribir "--------------------------------------------"
					FinSi
				FinSi
				
			6:
				// Salida del sistema
				Escribir ""
				Escribir "-------------------------"
				Escribir "Saliendo del sistema..."
				Escribir "-------------------------"
				Esperar 500 Milisegundos
				
			De Otro Modo:
				Escribir ""
				Escribir "--------------------------------------------"
				Escribir "Opción no válida. Intenta nuevamente..."
				Escribir "--------------------------------------------"
				Escribir ""
		FinSegun
	FinMientras
FinAlgoritmo