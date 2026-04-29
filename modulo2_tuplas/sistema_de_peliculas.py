catalogo = (
    ("12 Hombres en Pugna", "Sidney Lumet", 1957, 9.0),
    ("EL Caballero Oscuro", "Chritopher Nolan", 2008, 9.0),
    ("El viaje de Chihiro", "Hayao Miyazaki", 2001, 8.6),
    ("Parásitos", "Bong Joon-ho", 2019, 8.5),
    ("Forrest Gump", "Robert Zemeckis", 1994, 8.8)
)

print("=== CATÁLOGO DE PELÍULAS ===")
for titulo, director, año, puntuacion in catalogo:
    print(f"{titulo} ({año}) - Director: {director} - Puntuación: {puntuacion}")

primera, *resto = catalogo
print(f"\n Primera Película: {primera[0]} ({primera[2]})")
print(f"Resto del catálogo: {len(resto)} películas")

def buscar_por_director(director_buscado):
    coincidencias = ()
    for titulo, director, año, puntuacion in catalogo:
        if director == director_buscado:
            coincidencias += ((titulo, director, año, puntuacion),)
    return coincidencias 
    
def obtener_estadisticas(peliculas):
    if len(peliculas) == 0:
        return (0.0, 0.0, 0.0)
    primera_pelicula = peliculas[0]
    puntuacion_min = primera_pelicula[3]
    puntuacion_max = primera_pelicula[3]
    suma = 0.0

    for peli in peliculas:
        punt = peli[3]
        if punt < puntuacion_min:
            puntuacion_min = punt
        if punt > puntuacion_max:
            puntuacion_max = punt
        suma += punt

    promedio = suma / len(peliculas)
    return (puntuacion_min, puntuacion_max, promedio)

director = "Chritopher Nolan"
print(f"\n=== Peliculas de {director} ===")
coincidencias = buscar_por_director(director)
for titulo, dir, año, punt in coincidencias:
    print(f"- {titulo} ({año}) - Puntuación: {punt}")

min_punt, max_punt, prom_punt = obtener_estadisticas(catalogo)
print(f"\n-- Estadísticas Del Catálogo --")
print(f"Puntuación mínima: {min_punt}")
print(f"Puntuación máxima: {max_punt}")
print(f"Puntuación promedio: {prom_punt:.2f}")
