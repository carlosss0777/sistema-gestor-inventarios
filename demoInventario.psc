Algoritmo demoInventario
	Definir option, stock, stockProductos, numeroProductos Como Entero
	Definir proveedores, productos, nombreProducto Como Caracter
	Definir precio, preciosProductos Como Real
	
	Dimension productos[100] // lista d productos
	Dimension stockProductos[100] // lista de cantidades
	Dimension precioProductos[100] // lista de precios
	// Dimension proveedores[3]  
	
	proveedores <- "Logitech"
	
	// proveedores[1] <- "Logitech"
	// proveedores[2] <- "Samsung" // proveedores iniciales 
	// proveedores[3] <- "Razer"
	
	option <- 0
	
	Mientras option <> 5 Hacer
		Escribir "-- SISTEMA DE INVENTARIO --"
		Escribir "1. Registrar producto"
		Escribir "2. Ver Stock"
		Escribir "3. Aumentar stock"
		Escribir "4. Disminuir stock"
		Escribir "5. Salir del sistema"
		Leer option
		
		Segun option Hacer
				// Parte 1: pedir al usuario el nombre del producto, la cantidad incial (stock) y el precio
				// y añadir cada uno a la lista de productos, stpckProductos, precioProductos
			1:
				Si numeroProductos < 100 Entonces
					Escribir "Ingrese el nombre del producto:"
					Leer nombreProducto
					
					encontrado <- Falso
					Si numeroProductos > 0 Entonces
						Para i <- 1 Hasta numeroProductos Hacer
							Si Mayusculas(productos[i]) = Mayusculas(nombreProducto) Entonces
								encontrado <- Verdadero
							FinSi
						FinPara	
					FinSi
					
					Si encontrado = Verdadero Entonces
						Escribir "Error: El producto ya existe en el inventario."
						Esperar 500 Milisegundos
					Sino
						numeroProductos <- numeroProductos + 1
						productos[numeroProductos] <- nombreProducto
						Escribir "Ingresar cantidad inicial (stock):"
						Leer stockProductos[numeroProductos]
						Escribir "Ingresar precio del producto:"
						Leer precioProductos[numeroProductos]
						Escribir "---- Producto: ",nombreProducto," registrado con éxito ----"
						Escribir ""
						Esperar 500 Milisegundos
					FinSi
				Sino
					Escribir "Inventario lleno."
				FinSi
				
				// Parte 2: Hacer un bucle para recorrer la lista de productos y mostrar el nombre, stock y precio
			2:			
				
				
				// Parte 3: pedir al usuario el nombre del producto al que quiere añadir
				// stock. Finalmente sumar y mostrar el stock total
			3:
				Si numeroProductos == 0 Entonces
					Escribir "No se han registrado productos"
					
				SiNo
					Repetir
						Escribir "Seleccione el indice del producto (1 al ", numeroProductos, "):"
						
						Para i <- 1 Hasta numeroProductos Hacer
							Escribir i, "- ", productos[i], " (Stock: ", stockProductos[i], ")"
						FinPara
						
						Leer posicion
						
						Si posicion <= 0 O posicion >= numeroProductos
							Escribir "Error: Indice de producto no valido. Intenta nuevamente..."
							Escribir ""
						FinSi
					Hasta Que posicion >= 1 Y posicion <= numeroProductos
					
					Escribir "Has seleccionado: ", productos[posicion]
					Escribir "Stock actual: ", stockProductos[posicion]
					Escribir "Cantidad a añadir:"
					Leer stock
					
					stockProductos[posicion] <- stockProductos[posicion] + stock
					Escribir "------ Nuevo stock: ", stockProductos[posicion]," ----------"
					Escribir ""
					Esperar 500 Milisegundos
					
				FinSi
				
				// Parte 4: pedir al usuario el nombre del producto al que quiere restar
				// stock. Finalmente sumar y mostrar el stock total
			4:
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
				
			5:
				Escribir "Saliendo del sistema..."
				
			De Otro Modo:
				Escribir "Opcion no valida. Intenta nuevamente..."
				Escribir ""
		FinSegun
	FinMientras
FinAlgoritmo