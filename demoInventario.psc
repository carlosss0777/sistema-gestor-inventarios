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
				
				
				// Parte 2: Hacer un bucle para recorrer la lista de productos y mostrar el nombre, stock y precio
			2:
				
				
				// Parte 3: pedir al usuario el nombre del producto al que quiere añadir
				// stock. Finalmente sumar y mostrar el stock total
			3:
				
				
				// Parte 4: pedir al usuario el nombre del producto al que quiere restar
				// stock. Finalmente sumar y mostrar el stock total
			4:
				
				
				
			5:
				Escribir "Saliendo del sistema..."
				
			De Otro Modo:
				Escribir "Opcion no valida. Intenta nuevamente..."
				Escribir ""
		FinSegun
	FinMientras
FinAlgoritmo