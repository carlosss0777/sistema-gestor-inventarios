# SISTEMA DE GESTIÓN DE INVENTARIO - GRUPO 3

## Descripción del proyecto
Sistema de gestión de inventarios desarrollado con Python que permite gestionar productos, proveedores y movimientos (entradas/salidas) mediante una interfaz de consola.

El sistema está desarrollado utilizando Programación Orientada a Objetos, organizando el código en diferentes módulos para facilitar su comprensión y mantenimiento.

Trabajo correspondiente a la **Entrega #2 del Proyecto Final de Lógica de Programación.**

## Integrantes del equipo
| Nombre | Carnet |
|--------|-------|
| Brandon William Gomez Monge | GM21057 |
| Wendy Carolina Aristondo Soto | AS21020 |
| Carlos Alfredo Ayala Mejía | AM25008 |

## Funcionalidades implementadas
### Productos
- Registra productos (nombre, stock, proveedor, precio y descripción)
- Listar productos en tabla
- Editar datos de un producto
- Actualizar precio individualmente
- Eliminar productos
- Visualizar stock actual con indicador de nivel (Alto o Bajo)

### Proveedores
- Registrar proveedores (nombre, teléfono, email)
- Listar proveedores
- Editar datos de un proveedor
- Eliminar proveedores

### Movimientos de stock
- Registrar entradas (aumenta el stock)
- Registrar salidas (disminuye el stock)
- Ver historial de movimientos con fecha y hora

## Lógica del negocio
**1- Relación producto-proveedor:** un producto solo puede registrarse si existe al menos un proveedor. Cada producto debe estar asociado a uno.

**2- Control del stock mediante movimientos:** no se modifica directamente, sino a través de entradas y salidas.

**3- Restricción de stock negativo:** no se permite registrar una salida si la cantidad supera al stock disponible.

**4- Validación de duplicados:** no se puede registrar un producto con el mismo nombre y proveedor, ni dos proveedores con el mismo nombre.

**5- Validación de datos:** campos obligatorios, valores numéricos y formato de teléfono para los proveedores (`1234-5678`)

## Estructura del proyecto
```
sistema-gestor-inventarios/
│
├── docs/                                   # Documentación
│   └── pseudocodigo/                       # Carpeta de pseudocódigo
│       └── demoInventario.psc
│
├── src/                                    # Carpeta principal del sistema
│   └── app/
│       ├── model/                          # Definición de entidades de datos
│       │   ├── producto.py
│       │   ├── proveedor.py
│       │   └── movimiento_inventario.py
│       │
│       ├── service/                        # Lógica del negocio
│       │   ├── producto_service.py
│       │   ├── proveedor_service.py
│       │   └── movimiento_service.py
│       │
│       ├── ui/                             # Interfaz de usuario
│       │   ├── menu_principal.py
│       │   ├── producto_ui.py
│       │   ├── proveedor_ui.py
│       │   ├── movimiento_ui.py
│       │   └── entradas_salidas_ui.py
│       │
│       ├── utils/                          # Utilidades y métodos auxiliares
│       │   ├── __init__.py
│       │   ├── tools.py
│       │   ├── tablas.py
│       │   └── validators.py
│       │
│       └── main.py                         # Ejecición del sistema
│
├── tests/                                  # Pruebas unitarias
├── .gitignore                              # Archivos y directorios ignorados por Git
└── README.md                               # Documentación principal del proyecto
```

## Tecnologías utilizadas
- **Python 3.x**
- **tabulate** - formateo visual de tablas en consola
- **Git y GitHub** - control de versiones
- **Visual Studio Code** - entorno de desarrollo

## Cómo ejecutar
**1-** Instalar dependencias
```
pip install tabulate
```

**2-** Clonar el repositorio
```
git clone https://github.com/carlosss0777/sistema-gestor-inventarios.git
```

**3-** Acceder a la carpeta del proyecto
```
cd sistema-gestor-inventarios/src
```

**3-** Ejecutar el sistema
```
# Windows:
python -m app.main

# Linux / Mac:
python3 -m app.main
```
