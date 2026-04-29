inventario = [
    ["manzanas", 50, 0.5],
    ["peras", 30, 0.75],
    ["naranjas", 20, 0.6]
]

def actualizar_precio(producto, nuevo_precio):
    for i, item in enumerate(inventario):
        if item[0] == producto:
            del inventario[i]
            nueva_sublista = [producto, item[1], nuevo_precio]
            inventario.insert(i, nueva_sublista)
            print(f" Precio de '{producto}' actualizado a ${nuevo_precio:.2f}")
            return
    print(f" Producto '{producto}' no encontrado")

def registrar_venta(producto, cantidad):
    for i, item in enumerate(inventario):
        if item[0] == producto:
            if item[1] >= cantidad:
                nuevo_stock = item[1] - cantidad
                del inventario[i]
                nueva_sublista = [producto, nuevo_stock, item[2]]
                inventario.insert(i, nueva_sublista)
                print(f" Venta: {cantidad} {producto}. Nuevo stock: {nuevo_stock}")
            else:
                print(f" Stock insuficiente. Solo hay {item[1]}")
            return
    print(f" Producto '{producto}' no encontrado")

def anadir_producto(producto, cantidad, precio):
    for i, item in enumerate(inventario):
        if item[0] == producto:
            nuevo_stock = item[1] + cantidad
            del inventario[i]
            nueva_sublista = [producto, nuevo_stock, item[2]]
            inventario.insert(i, nueva_sublista)  # <- corregido: insert(i, ...)
            print(f" Stock actualizado: {producto} ahora tiene {nuevo_stock}")
            return
    # Solo si no se encontró el producto, se añade al final
    inventario.append([producto, cantidad, precio])
    print(f" Nuevo producto '{producto}' añadido")

def mostrar_inventario():
    print("\n INVENTARIO:")
    print(f"{'N°':<3} {'Producto':<12} {'Cantidad':<8} {'Precio':<8}")
    print("-" * 35)
    for i, item in enumerate(inventario, start=1):
        nombre, cant, precio = item
        print(f"{i:<3} {nombre:<12} {cant:<8} ${precio:<8.2f}")
    print("-" * 35)
    print(f"Total: {len(inventario)} productos")

actualizar_precio("peras", 0.90)
registrar_venta("manzanas", 100)
anadir_producto("uvas", 15, 1.20)
mostrar_inventario()