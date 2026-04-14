# SISTEMA DE GESTIÓN DE INVENTARIO - GRUPO 3

## Descripción del proyecto
El proyecto consiste en el desarrollo de un sistema básico de gestión de inventarios utilizando pseudocódigo en PSeInt.

El objetivo principal es simular la lógica de negocio de un inventario, permitiendo administrar productos, proveedores y movimientos de stock (entradas y salidas), asegurando que no existan cantidades negativas.

Trabajo correspondiente a la **Entrega #1 del proyecto final de Lógica de Programación.**

## Funcionalidades implementadas
### Módulo 1: Registro de Productos
Permite ingresar nuevos productos al inventario
- Valida que el producto no exista previamente
- Guarda el nombre, stock inicial, el proveedor del producto y el precio

### Módulo 2: Consultar Stock
Permite visualizar los productos registrados, con todos sus datos (nombre, stock, proveedor y precio)

### Módulo 3: Registro de Proveedores
Permite registrar proveedores al sistema, evitando duplicados

### Módulo 4: Aumento de Stock
Permite agregar unidades a un producto existente (aumentar el stock)
- El usuario selecciona el producto por índice
- Se actualiza sumando la cantidad ingresada 

### Módulo 5: Disminución de Stock
Permite retirar unidades de un producto 
- Valida que el stock disponible sea suficiente 
- Evita que el stock sea negativo

## Lógica del sistema
El sistema utiliza estructuras básicas como:
- Arreglos para almacenar productos, stock, precios y proveedores
- Validaciones para evitar duplicados
- Menú interactivo con opciones
- Bucles y condiciones para el control del flujo

## Estado del proyecto
El proyecto está en fase de desarrollo, pero hasta el momento se tiene: 
- Estructura base del sistema
- Módulos principales definidos
- Implementación funcional en PSeInt

En las siguientes entregas se tiene previsto:
- Migrar el proyecto al lenguaje Python
- Mejorar la estructura del sistema (uso de clases y modularización)
- Implementar validaciones más robustas

## Integrantes del equipo
- Carlos Alfredo Ayala Mejía -- AM25008
- Wendy Carolina Aristondo Soto -- AS21020
- Brandon William Gomez Monge -- GM21057