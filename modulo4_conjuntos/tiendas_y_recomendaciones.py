tienda_centro = {"leche", "pan", "huevos", "manzanas", "arroz"}
tienda_norte = {"pan", "queso", "huevos", "jugo", "galletas"}
tienda_sur = {"leche", "queso", "yogur", "manzanas", "cereal"}

vacio = set()

tienda_centro.add("cafe")
tienda_norte.update(["te", "miel"])
tienda_sur.discard("cereal")

catalogo_completo = tienda_centro.union(tienda_norte, tienda_sur)
productos_comunes = tienda_centro.intersection(tienda_norte, tienda_sur)

exclusivos_centro = tienda_centro.difference(tienda_norte, tienda_sur)
exclusivos_norte = tienda_norte.difference(tienda_centro, tienda_sur)
exclusivo_sur = tienda_sur.difference(tienda_centro, tienda_norte)

comunes_cn = not tienda_centro.isdisjoint(tienda_norte)

usuario1= {"acción", "aventura", "ciencia ficción"}
usuario2= {"comedia", "drama", "romance"}
usuario3= {"acción", "comedia", "terror", "ciencia ficción"}

comunes_todos = usuario1 & usuario2 & usuario3
universo_generos = usuario1 | usuario2 | usuario3
exclusivos_u1 = usuario1 - (usuario2 | usuario3)
dif_u1_u2 = usuario1 ^ usuario2

subconjunto = {"acción", "aventura"} <= usuario1
subconjunto_u1_u2 = usuario1.issubset(usuario2)

print("=== REPORTE TÉCNICO DE SETS ===")
print(f"Catálogo Total ({len(catalogo_completo)} productos): {catalogo_completo}")
print(f"Comunes a todas: {productos_comunes if productos_comunes else 'Ninguno'}")
print(f"Exclusivos Centro: {exclusivos_centro}")
print(f"¿Solapan Centro y Norte?: {comunes_cn}")

print("\n=== REPORTE DE PELÍCULAS ===")
print(f"Universo de géneros: {universo_generos}")
print(f"Comunes todos: {comunes_todos}")
print(f"Diferencia simétrica U1 y U2: {dif_u1_u2}")
print(f"¿Es 'acción' subconjunto de U1?: {subconjunto}")