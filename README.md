# cotizacion_de_ventanas

## Autor: David Cuartas Hernandez

## Descripción

Este proyecto tiene como objetivo gestionar la etapa de cotización teniendo en cuenta los estilos de ventanas y materiales, así como calcular los costos asociados a la fabricación de ventanas. Incluye funcionalidades para la selección de estilos de ventanas, tipos de acabados de aluminio, tipos de vidrio, y la opción de agregar esmerilado al vidrio. Además, permite calcular los costos basados en las dimensiones de las ventanas y aplicar descuentos según la cantidad de unidades.

## Requerimientos

### Gestión de Estilos de Ventanas
- Permitir la selección de los estilos de ventanas: O, XO, OXXO, OXO.
- Validar que los estilos no permitidos (como XOX) no se puedan seleccionar.

### Gestión de Materiales
- Permitir la selección del tipo de acabado del aluminio: Pulido, Lacado Brillante, Lacado Mate, Anodizado.
- Permitir la selección del tipo de vidrio: Transparente, Bronce, Azul.
- Opción para agregar esmerilado al vidrio seleccionado.

### Cálculo de Costos
- Calcular el costo del aluminio basado en el perímetro de cada ventana, descontando las esquinas.
- Calcular el costo del vidrio basado en el área de cada ventana, considerando que el vidrio es 1.5 cm más pequeño en cada lado.
- Incluir el costo de las esquinas y las chapas en el cálculo.
- Aplicar un descuento del 10% si la cantidad de ventanas supera las 100 unidades.

### Actualización de Precios
- Opción para actualizar los precios del artículo seleccionado.

### Interfaz de Usuario
- Formulario para ingresar las dimensiones de la ventana (ancho y alto).
- Selección de estilo de ventana.
- Selección de tipo de acabado del aluminio.
- Selección de tipo de vidrio y opción de esmerilado.
- Mostrar el costo total de la ventana desglosado por materiales y descuentos aplicados.

### Generación de Cotizaciones
- Generar un reporte de cotización que incluya todos los detalles de la ventana y el costo total.

### Instalación
Clona el repositorio:
git clone https://github.com/tu-usuario/proyecto-ventanas.git

### Tecnologías:
Python 3+: Lenguaje de programación principal para el desarrollo de la aplicación

### Estructura del proyecto:

### main.py: 
Archivo principal donde se ejecutará la aplicación.
### ventana.py: 
Módulo que contiene la clase Ventana, encargada de representar una ventana y realizar los cálculos correspondientes.
### materiales.py:
 Módulo que contiene los datos de los materiales (aluminio, vidrio, etc.) y sus precios