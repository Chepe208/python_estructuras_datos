ventas_por_region = {
    "Norte": {"Q1": 1200, "Q2": 1350, "Q3": 1500, "Q4": 1700},
    "Sur": {"Q1": 900, "Q2": 1100, "Q3": 1300, "Q4": 1450},
    "Este": {"Q1": 1800, "Q2": 2100, "Q3": 2450, "Q4": 2800},
    "Oeste": {"Q1": 700, "Q2": 850, "Q3": 950, "Q4": 1050},
}

ventas_por_region.update({
    "Centro": {"Q1": 1000, "Q2": 1200, "Q3": 1150, "Q4": 1300},
})

region_removida = ventas_por_region.pop("Oeste", "No encontrada")

totales_anuales = {}
for region, ventas_trim in ventas_por_region.items():
    total = sum(ventas_trim.values())
    totales_anuales[region] = total

region_max = max(totales_anuales.items(), key=lambda item: item[1])

totales_por_trimestre = {}
for region, trimestre in ventas_por_region.items():
    for trimestre, venta in trimestre.items():
        totales_por_trimestre.setdefault(trimestre, 0)
        totales_por_trimestre[trimestre] += venta

gran_total = sum(totales_anuales.values())

porcentajes = {region: (total / gran_total) * 100 for region, total in totales_anuales.items()}

print(f"\n === REPORTE DE VENTAS ANUALES POR REGIÓN ===")
print(f"(Nota: Se eliminó la región: {region_removida if isinstance(region_removida, str) else 'Oeste'})\n")
print(f"{'Región':<10} {'Ventas Anuales':<15} {'Porcentaje':<10}")
print("-" * 42)

for region, total in sorted(totales_anuales.items(), key=lambda x: x[1], reverse=True):
    print(f"{region:<10} {total:<15.2f} {porcentajes[region]:<10.2f}%")

print(f"\n Gran Total Ventas: {gran_total:.2f}")
print(f"Región con mayores ventas: {region_max[0]} con {region_max[1]:.2f}")

print("\n--- Ventas por Trimestre ---")
for trim in sorted(totales_por_trimestre.keys()):
    print(f"{trim}: {totales_por_trimestre[trim]}")

print("\n--- Prueba de Acceso Seguro ---")
print("¿Se procesó la región 'Norte'?", "Norte" in ventas_por_region)
print("Buscando región 'Sur' con get():", ventas_por_region.get("Sur", "No existe"))