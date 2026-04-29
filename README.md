# Trabajo GA1 220501093-04 AA1 EV03 – Fundamentos de Python: Estructuras de Datos en Python

## Reto Módulo 1: Listas – Sistema de inventario

### Descripción del reto
Construir un sistema de inventario usando listas anidadas que gestione productos, precios y stock. Se implementan funciones para actualizar precio, registrar ventas, añadir productos y mostrar el inventario.

### Solución implementada
El código se encuentra en `modulo1_listas/inventario_listas.py`. Se utilizaron exclusivamente los subtemas proporcionados:
- **Creación y Acceso**: listas con `[]`, índices, `len()`.
- **Métodos para añadir**: `append()`, `insert()`.
- **Métodos para eliminar**: `del lista[i]`.
- **Recorrido de listas**: `enumerate()`.

No se usó modificación directa (`lista[i] = valor`) porque no aparece en los subtemas; en su lugar, se aplica `del` + `insert` para actualizar valores.

### Evidencia de ejecución

![Ejecución normal](images/gestion_inventario_ejecucion.png)
Se puede ver la actualizacion del precio de las peras que estaban en 0.75 a 0.90 usando del y tambien insert. Despues se registro una venta de 10 manzanas se aplica del para eliminar la sublista original y insert para poder colocar la nueva con stock 40. Despues se añade un nuevo producto que son las uvas usando append(). Por ultimo mostrar_inventario() recorre la lista con enumerate() y muestra los datos usando indices y len().

![Validación de stock insuficiente](images/gestion_inventario_prueba.png)
En esta imagen se ve que se intento vender 100 manzanas pero solo hay 50. La funcion registrar_venta() hace que verifique la condicion item[1] >= cantidad y al ser falsa muestra el mensaje de error sin modificar el inventario. Se pudo ver que se uso la estructura de condicionales y tambien con el acceso de elementos de la lista anidada.

### Reflexión personal

Haciendo este reto entendi lo importante de los subtemas que se vieron en la pagina. Como las listas no estan modificadas por indice, aprendi a usar el del y el insert. Tambien entendi como usar enummerte() para poder recorrer 