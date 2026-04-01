Algoritmo demoInventario
	Definir option, stock, stockProductos, numeroProductos, numeroProveedores, i, posicion Como Entero
	Definir proveedores, productos, nombreProducto, nombreProveedor Como Caracter
	Definir precio, preciosProductos Como Real
	Definir encontrado Como Logico
	
	Dimension productos[100] // lista d productos
	Dimension stockProductos[100] // lista de cantidades
	Dimension precioProductos[100] // lista de precios
	Dimension proveedores[10] // lista de proveedores
	
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
				Si numeroProductos == 0 Entonces
					Escribir "No se han registrado productos"
					
				SiNo
					Repetir
						Escribir "Seleccione el indice del producto (1 al ", numeroProductos, "):"
						
						Para i <- 1 Hasta numeroProductos Hacer
							Escribir i, "- ", productos[i], " (Stock: ", stockProductos[i], ")"
						FinPara
						
						Leer posicion
						
						Si posicion <= 0 O posicion > numeroProductos
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
			5:
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
				Escribir "Saliendo del sistema..."
				
			De Otro Modo:
				Escribir "Opcion no valida. Intenta nuevamente..."
				Escribir ""
		FinSegun
	FinMientras
FinAlgoritmo