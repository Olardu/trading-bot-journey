"""
# Bloque 1 — Tu primera lista de precios
# Listas - series de precios historicos
precios = [65000.0, 65200.0, 64800.0, 65455.0, 65100.0]

print(precios)          # toda la lista
print(precios[0])       # primer precio
print(precios[4])       # ultimo precio
print(len(precios))     # cuantos precios hay

"""

"""
# Bloque 2 — Recorrer la lista con un loop
# Loop basico - revisar cada precio
precios = [65000.0, 65200.0, 64800.0, 65455.0, 65100.0]
meta_diaria = 0.7
precio_entrada = 65000.0

for precio in precios:
    ganancia_pct = ((precio - precio_entrada) / precio_entrada) * 100
    print(f"Precio: {precio} | Ganancia: {ganancia_pct:.2f}%")
"""

"""
# Bloque 3 — Loop con condicional adentro
# Loop + condicional combinados
precios = [65000.0, 65200.0, 64350.0, 65455.0, 65100.0]
precio_entrada = 65000.0
meta_diaria = 0.7
stop_loss = -1.0

for precio in precios:
    ganancia_pct = ((precio - precio_entrada) / precio_entrada) * 100

    if ganancia_pct >= meta_diaria:
        print(f"✅ {precio} | {ganancia_pct:.2f}% | META ALCANZADA")
    elif ganancia_pct <= stop_loss:
        print(f"❌ {precio} | {ganancia_pct:.2f}% | STOP LOSS ACTIVADO")
    else:
        print(f"📈 {precio} | {ganancia_pct:.2f}% | En operacion")
"""

"""
# Bloque 4  — Calculando estadísticas de la serie
precios = [65000.0, 65200.0, 64350.0, 65455.0, 65100.0]
precio_entrada = 65000.0
meta_diaria = 0.7
stop_loss = -1.0
dias_meta = 0
dias_perdida = 0

for precio in precios:
    ganancia_pct = ((precio - precio_entrada) / precio_entrada) * 100
    if ganancia_pct >= meta_diaria:
        dias_meta += 1
    elif ganancia_pct <= stop_loss:
        dias_perdida += 1

print(f"Dias de meta: {dias_meta}")
print(f"Dias de perdida: {dias_perdida}")
print(f"Total dias: {len(precios)}")
"""

# Bloque 5 — Cerrando la Semana 3 con estilo
# Resumen ejecutivo de la serie
precios = [65000.0, 65200.0, 64350.0, 65455.0, 65100.0]
precio_entrada = 65000.0
meta_diaria = 0.7
stop_loss = -1.0
dias_meta = 0
dias_perdida = 0
dias_normal = 0

for precio in precios:
    ganancia_pct = ((precio - precio_entrada) / precio_entrada) * 100
    if ganancia_pct >= meta_diaria:
        dias_meta += 1
    elif ganancia_pct <= stop_loss:
        dias_perdida += 1
    else:
        dias_normal += 1

total = len(precios)
print(f"--- Resumen de la serie ---")
print(f"Total dias analizados:  {total}")
print(f"Dias en metra:          {dias_meta} ({dias_meta / total * 100:.1f}%)")
print(f"Dias en perdida:        {dias_perdida} ({dias_perdida / total * 100:.1f}%)")
print(f"Dias normales:          {dias_normal} ({dias_normal / total * 100:.1f}%)")
