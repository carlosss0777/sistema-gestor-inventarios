# SISTEMA GESTOR DE INVENTARIOS
> Proyecto Final de Lógica de Programación - Grupo 3

## Descripción del proyecto
Aplicación CLI de gestión de inventaros desarrollado con Python con arquitectura por capas y persistencia de datos en JSON. Permite administrar productos, proveedores y movimientos de stock de forma completa y estructurada. 

## Integrantes del equipo
| Nombre | Carnet | Correo | Usuario |
|--------|-------|-------|-------|
| Carlos Alfredo Ayala Mejía | AM25008 | AM25008@ues.edu.sv | [@AM25008](https://github.com/AM25008), [@carlosss0777](https://github.com/carlosss0777) |
| Brandon William Gomez Monge | GM21057 | GM21057@ues.edu.sv | [@BrandonGomezUES](https://github.com/BrandonGomezUES) |
| Wendy Carolina Aristondo Soto | AS21020 | AS21020@ues.edu.sv | [@Carito-code](https://github.com/Carito-code) |

## Funcionalidades implementadas
### Productos
- Registra productos (nombre, stock, proveedor, precio y descripción)
- Listar productos en tabla
- Editar datos de un producto
- Actualizar precio individualmente
- Eliminar productos
- Visualizar stock actual con indicador de nivel (Alto / Bajo)

### Proveedores
- Registrar proveedores (nombre, teléfono, email)
- Listar proveedores
- Editar datos de un proveedor
- Eliminar proveedores (soft delete): el proveedor deja de estar disponible para nuevos productos, pero los registros existentes conservan su referencia

### Movimientos de stock
- Registrar entradas (aumenta el stock)
- Registrar salidas (disminuye el stock)
- Ver historial de movimientos con fecha y hora

## Lógica del negocio
**1- Relación producto-proveedor:** un producto solo puede registrarse si existe al menos un proveedor. Cada producto debe estar asociado a uno.

**2- Control del stock mediante movimientos:** el stock no se modifica directamente. Solo a través de entradas y salidas registradas en el sistema.

**3- Restricción de stock negativo:** no se permite registrar una salida si la cantidad supera al stock disponible.

**4- Validación de duplicados:** no se puede registrar un producto con el mismo nombre y proveedor, ni dos proveedores con el mismo nombre.

**5- Validación de datos:** campos obligatorios, valores numéricos y formato de teléfono para los proveedores (`1234-5678`).

**6- Soft delete de proveedores:** al eliminar un proveedor, se marca como inactivo en vez de borrarse físicamente. Los productos ya registrados conservan el nombre del proveedor en su historial, pero el proveedor no aparece disponible al registrar nuevos productos.


## Estructura del proyecto
```
sistema-gestor-inventarios/
│
├── docs/                                   # Documentación
│   └── pseudocodigo/                       # Pseudocódigo de la primera entrega
│       └── demoInventario.psc              # Algoritmo del sistema en pseudocodigo
│
├── src/
│   ├── app/
│   │   ├── __init__.py
│   │   │
│   │   ├── model/                          # Modelos de datos
│   │   │   ├── __init__.py
│   │   │   ├── producto.py
│   │   │   ├── proveedor.py
│   │   │   └── movimiento_inventario.py
│   │   │
│   │   ├── repository/                     # Lectura y escritura de datos en disco
│   │   │   ├── __init__.py
│   │   │   ├── producto_repository.py
│   │   │   ├── proveedor_repository.py
│   │   │   └── movimiento_repository.py
│   │   │
│   │   ├── service/                        # Lógica del negocio
│   │   │   ├── __init__.py
│   │   │   ├── producto_service.py
│   │   │   ├── proveedor_service.py
│   │   │   └── movimiento_service.py
│   │   │
│   │   ├── ui/                             # Interfaz de usuario por consola
│   │   │   ├── __init__.py
│   │   │   ├── menu_principal.py
│   │   │   ├── producto_ui.py
│   │   │   ├── proveedor_ui.py
│   │   │   ├── movimiento_ui.py
│   │   │   └── entradas_salidas_ui.py
│   │   │
│   │   ├── utils/                          # Herramientas auxiliares reutilizables
│   │   │   ├── __init__.py
│   │   │   ├── tools.py                    # Funciones de consola
│   │   │   ├── tablas.py                   # Formateo de tablas con tabulate
│   │   │   └── validators.py               # Validaciones globales compartidas
│   │   │
│   │   └── main.py                         # Punto de entrada del sistema
│   │
│   ├── tests/                              # Pruebas unitarias de los servicios
│   │   ├── __init__.py
│   │   ├── fakes.py                        # Repositories falsos compartidos para las pruebas
│   │   ├── test_producto_service.py
│   │   ├── test_proveedor_service.py
│   │   └── test_movimiento_service.py
│   │
│   └── data/                               # Archivos JSON generados en tiempo de ejecución
│       ├── productos.json
│       ├── proveedores.json
│       └── movimientos.json
│
├── .gitignore                              # Archivos y directorios ignorados por Git
└── README.md                               # Documentación principal del proyecto
```

## Descripción de capas
### Model
Se definen los atributos como privados, con acceso unicamente a través de `getters` y `setters`.
| Clase | Archivo | Atributos principales |
|---|---|---|
| `Producto` | `producto.py` | nombre, stock, proveedor, precio, descripción |
| `Proveedor` | `proveedor.py` | nombre, teléfono, email, estado (soft delete) |
| `MovimientoInventario` | `movimiento_inventario.py` | producto, tipo (Entrada/Salida), cantidad, fecha |

### Repository
Traducen entre listas de objetos y los archivos JSON de `data/`.
| Archivo | Particularidad al cargar/guardar |
|---|---|
| `producto_repository.py` | Reconstruye la referencia al `Proveedor` buscando por nombre |
| `proveedor_repository.py` | Persiste la bandera `activo` para mantener el soft delete entre ejecuciones |
| `movimiento_repository.py` | Convierte la fecha entre `datetime` y string al guardar/cargar |

### Service
Capa de la lógica, donde se hacen todas las validaciones.
| Archivo | Lanza error si... | Operación destacada |
|---|---|---|
| `producto_service.py` | nombre/precio/stock inválidos, o producto duplicado para el mismo proveedor | `cambiar_stock()` aplica entradas y salidas |
| `proveedor_service.py` | nombre vacío, teléfono con formato distinto a `1234-5678`, o email inválido | eliminar marca `activo = False` en vez de borrar |
| `movimiento_service.py` | cantidad no numérica, negativa, o salida mayor al stock disponible | `registrar_movimiento()` guarda fecha y hora automáticamente |

### UI
Menús por consola, capturas de datos e impresión de excepciones.
| Módulo | Opciones disponibles |
|---|---|
| Productos (`producto_ui.py`) | registrar, listar, actualizar, eliminar, ver stock, actualizar precio |
| Proveedores (`proveedor_ui.py`) | registrar, listar, actualizar, eliminar (soft delete) |
| Movimientos (`movimiento_ui.py` / `entradas_salidas_ui.py`) | registrar entrada, registrar salida, ver historial |

`menu_principal.py` conecta los tres módulos y permite navegar entre ellos.

### Utils
| Archivo | Para qué se usa |
|---|---|
| `tools.py` | limpiar pantalla, pausas y formato estándar de mensajes de error |
| `tablas.py` | formatea cada tabla (productos, proveedores, stock, movimientos) con `tabulate` |
| `validators.py` | valida los índices ingresados al seleccionar elementos de una lista |

### Tests
| Archivo | Qué cubre |
|---|---|
| `test_producto_service.py` | validaciones de producto, registro/eliminación, cambios de stock y duplicados |
| `test_proveedor_service.py` | validaciones de proveedor, registro, soft delete y filtrado de activos |
| `test_movimiento_service.py` | validación de cantidades, entradas/salidas y restricción de stock negativo |
 
Cada archivo usa el `setUp()` para instanciar el service con un repository falso definido en `fakes.py`, evitando así depender de los archivos reales en `data/`.

Cada capa recibe sus dependencias por parámetro en el constructor (inyección de dependencias), lo que facilita el mantenimiento y las pruebas.

## Persistencia de datos
Los datos se guardan automáticamente en archivos JSON dentro de la carpeta `data/` cada vez que se realiza una operación (crear, actualizar o eliminar). Al iniciar el programa, los datos se cargan desde esos archivos.

La carpeta `data/` está en el `.gitignore` y no se sube al repositorio, ya que contiene datos locales de cada usuario. Se crea automáticamente la primera vez que se ejecuta el programa.

## Tecnologías utilizadas
| Tecnología | Uso en el proyecto |
|------------|-------------------|
| **Python 3.x** | Lenguaje principal del sistema |
| **tabulate** | Formateo visual de tablas en consola |
| **json** | Serialización y persistencia de datos en archivos JSON |
| **unittest** | Framework para las pruebas unitarias de los servicios |
| **Git y GitHub** | Control de versiones y trabajo colaborativo |
| **Visual Studio Code** | Entorno de desarrollo |

## Requisitos previos
Antes de ejecutar el proyecto asegurate de tener instalado:
 
- **Python 3.10 o superior** — lenguaje principal del proyecto
- **pip** — gestor de paquetes de Python (viene incluido con Python)
- **Git** — para clonar el repositorio


## Ejecutar el sistema
**1- Clonar el repositorio**
```bash
git clone https://github.com/carlosss0777/sistema-gestor-inventarios.git
```

**2- Acceder a la carpeta del proyecto**
```bash
cd sistema-gestor-inventarios/src
```

**3- Crear el entorno virtual**
```bash
# Windows
python -m venv venv

# Linux / Mac
python3 -m venv venv
```

**4- Activar el entorno virtual**
```bash
# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

**5- Instalar dependencias**
```bash
pip install tabulate
```

**6- Ejecutar el sistema**
```bash
# Windows
python -m app.main

# Linux / Mac
python3 -m app.main
```

Para desactivar el entorno virtual cuando termines:
```bash
deactivate
```

Al ejecuar verás el menú principal:
```
-----------------------------------
== SISTEMA GESTOR DE INVENTARIOS ==
-----------------------------------
1- Gestión de productos
2- Gestión de proveedores
3- Gestión de movimientos
0- Salir del sistema
 
Elige una opcion:
```

## Casos de uso
### Caso 1: Registrar un proveedor
```
== GESTIÓN DE PROVEEDORES ==
1- Registrar proveedor
 
Nombre: Logitech
Teléfono: 2222-3333
Email: ventas@logitech.com
 
✔ Proveedor registrado exitosamente.
```

### Caso 2: Registrar un producto
```
== GESTIÓN DE PRODUCTOS ==
1- Registrar producto
 
Nombre: Mouse Gamer
Stock: 15
Precio: $39.99
Descripción: Mouse inalámbrico RGB
 
-- PROVEEDORES REGISTRADOS --
╒════╤══════════╤═════════════╤══════════════════════╕
│    │  Nombre  │  Teléfono   │        Email         │
╞════╪══════════╪═════════════╪══════════════════════╡
│ 1  │ Logitech │  2222-3333  │ ventas@logitech.com  │
╘════╧══════════╧═════════════╧══════════════════════╛
 
Selecciona el proveedor: 1
 
✔ Producto registrado exitosamente.
```

### Caso 3: Registrar una entrada de stock
```
== REGISTRO DE ENTRADAS/SALIDAS DE STOCK ==
1- Registrar entrada de stock
 
-- PRODUCTOS --
╒════╤══════════════╤══════════╤═════════╤══════════╤═══════════════════════╕
│    │    Nombre    │  Precio  │  Stock  │Proveedor │      Descripcion      │
╞════╪══════════════╪══════════╪═════════╪══════════╪═══════════════════════╡
│ 1  │  Mouse Gamer │  $39.99  │   15    │ Logitech │  Mouse inalámbrico RGB│
╘════╧══════════════╧══════════╧═════════╧══════════╧═══════════════════════╛
 
Selecciona el producto: 1
Ingresa la cantidad a añadir: 10
 
✔ Movimiento registrado correctamente.
```

### Caso 4: Validaciones en acción
Si se intenta registrar una salida mayor al stock disponible:
```
Ingresa la cantidad a restar: 999
 
------------------------------------------------------------
  ERROR: No hay suficiente stock disponible
  Intenta nuevamente.
------------------------------------------------------------
```

## Ejecutar las pruebas
Las pruebas cubren la capa `service`, que es donde vive la lógica del negocio. Se utilizan repositories falsos (`fakes.py`) para que las pruebas no lean ni escriban archivos reales durante su ejecución.

Desde la carpeta `src/`:

### Ejecutar todas las pruebas de una vez
```bash
# Windows
python -m unittest discover tests -v

# Linux / Mac
python3 -m unittest discover tests -v
```

### Ejecutarlas pruebas de un módulo específico
#### Solo el modulo de productos
```bash
# Windows
python -m unittest tests.test_producto_service -v

# Linux / Mac
python3 -m unittest tests.test_producto_service -v
```

#### Solo el modulo de proveedores
```bash
# Windows
python -m unittest tests.test_proveedor_service -v

# Linux / Mac
python3 -m unittest tests.test_proveedor_service -v
```

#### Solo el modulo de movimientos
```bash
# Windows
python -m unittest tests.test_movimiento_service -v

# Linux / Mac
python3 -m unittest tests.test_movimiento_service -v
```

> El flag `-v` (verbose) muestra el nombre de cada prueba al ejecutarse. Sin él solo muestra un punto por prueba pasada y la cantidad total al final.

## Recomendaciones de uso
>[!TIP]
> Se recomienda **registrar proveedores antes que productos**, dado que cada producto debe estar asociado a un proveedor. Si se intenta registrar un producto sin ninguno disponible, el sistema ofrece la opción de registrar uno en el momento, pero se recomienda hacerlo con anticipación.

>[!TIP]
> De igual forma, se recomienda **registrar productos antes de registrar movimientos**, ya que los movimientos requieren seleccionar un producto existente, así que debe haber al menos uno registrado.

>[!WARNING]
> **No eliminar la carpeta `data/` manualmente** a menos que quieras borrar todos los registros del sistema.

### El orden recomendado es:

1- Registrar proveedores

2- Registrar productos

3- Registrar movimientos

## Notas
>[!NOTE]
> - La carpeta `data/` se crea automáticamente la primera vez que se ejecuta el programa.
> - Si se elimina la carpeta `data/`, el sistema arranca sin registros como si fuera la primera vez.