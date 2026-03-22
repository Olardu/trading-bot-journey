# Mi version del analizador
par = "ETH/USDT"
precio_entrada = 3200.0
precio_actual = 3222.4
cantidad = 5
meta_diaria = 0.7

# Calculo
diferencia = precio_actual - precio_entrada
ganancia_total = diferencia * cantidad
ganacia_unidad = diferencia / cantidad
ganancia_ptc = (diferencia / precio_entrada) * 100

# Resultados
print( f"Par operado: {par}")
print( f"Precio de entrada: {precio_entrada}")
print( f"Precio actual: {precio_actual}")
print(f"Ganacia por unidad: {ganacia_unidad:.2f}")
print(f"Ganancia total: {ganancia_total:.2f}")
print(f"Ganancia porcentual: {ganancia_ptc:.2f}%")
print(f"Meta diaria: {meta_diaria}%")
