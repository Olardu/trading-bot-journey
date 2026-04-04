# Practica de la semana 3
# Incluiremos las listas de precio, el porcentaje de ganancia por dia y su estado
# El estado de cada dia, en operacion, meta alcanzada o activar el stop loss
# Y el porcentaje de cada estado por dia

precios = [48000.0, 48500.0, 47200.0, 48336.0, 47800.0, 48100.0, 48350.0]
precio_entrada = 48000.0
meta_diaria = 0.7
stop_loss = -1.0
dias_meta = 0
dias_perdida = 0
dias_operacion = 0

print("--- Estado del dia ---")
for precio in precios:
    ganancia_pct = ((precio - precio_entrada) / precio_entrada) * 100

    if ganancia_pct >= meta_diaria:
        print(f"✅ {precio} | {ganancia_pct:.2f}% | META ALCANZADA")
        dias_meta += 1
    elif ganancia_pct <= stop_loss:
        print(f"❌ {precio} | {ganancia_pct:.2f}% | STOP LOSS ACTIVADO")
        dias_perdida += 1
    else:
        print(f"📈 {precio} | {ganancia_pct:.2f}% | En operacion")
        dias_operacion += 1

print(f"\n")
print("--- Estadisticas de los dias ---")
print(f"Dias en meta:       {dias_meta}")
print(f"Dias en perdida:    {dias_perdida}")
print(f"Dias en operacion:  {dias_operacion}")
print(f"Total dias:         {len(precios)}")
print(f"\n")
total = len(precios)
print(f"--- Resumen de la serie ---")
print(f"Total dias analizados:  {total}")
print(f"Dias en meta:           {dias_meta} ({dias_meta/total*100:.1f}%)")
print(f"Dias en perdida:        {dias_perdida} ({dias_perdida/total*100:.1f}%)")
print(f"Dias en operacion:      {dias_operacion} ({dias_operacion/total*100:.1f}%)")