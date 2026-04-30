ventas = [
    {"producto": "laptop", "unidades": 20, "precio": 800, "categoria": "electrónica"},
    {"producto": "teclado", "unidades": 50, "precio": 25, "categoria": "electrónica"},
    {"producto": "mouse", "unidades": 30, "precio": 15, "categoria": "electrónica"},
    {"producto": "monitor", "unidades": 10, "precio": 200, "categoria": "electrónica"},
    {"producto": "cuaderno", "unidades": 100, "precio": 2, "categoria": "papeleria"},
    {"producto": "lapicero", "unidades": 200, "precio": 1, "categoria": "papeleria"},
]

valor_total = [v["unidades"] * v["precio"] for v in ventas]
print("Valor total por producto:", valor_total)

productos_destacados = [v["producto"] for v in ventas if v["unidades"] * v["precio"] > 1000]
print(" Productos con valor > 1000:", productos_destacados)

producto_info = {v["producto"]: {"valor": v["unidades"] * v["precio"], "unidades": v["unidades"]} for v in ventas}
print("Informacion por productos:", producto_info)

premium = {v["producto"]: v["unidades"] * v["precio"] for v in ventas if v["precio"] > 50}
ranking_premium = {k: v for k, v in sorted(premium.items(), key=lambda item: item[1], reverse=True)}
print("Ranking premium (ordenado por valor):", ranking_premium)

categorias_unicas = {v["categoria"] for v in ventas}
print ("Categorias unicas:", categorias_unicas)

productos_baratos = {v["producto"] for v in ventas if v["precio"] <= 50}
print(" Productos baratos (precio < 50):", productos_baratos)

resumen_formateado = {v["producto"]: {"valor": v["unidades"] * v["precio"], "unidades": v["unidades"], "precio": v["precio"]} for v in ventas}
print("\n Resumen formateado completo:")
for prod, datos in resumen_formateado.items():
    print(f"   {prod}: {datos}")

gran_total = sum(valor_total)
print(f"\n   Gran total de ventas: {gran_total}")