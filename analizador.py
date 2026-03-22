# Mini analizador de operaciones

precio_entrada = 66000.0
precio_actual = 66462.0
nombre_par = "BTC/USDT"
cantidad = 10
meta_diaria = 0.7

# Calculo
diferencia = precio_actual - precio_entrada
ganancia_total = diferencia * cantidad
ganancia_ptc = (diferencia / precio_entrada) * 100

# Resultados
print( f"Par operado: {nombre_par}")
print( f"Precio de entrada: {precio_entrada}")
print( f"Precio actual: {precio_actual}")
print(f"Ganacia por unidad: {diferencia}")
print(f"Ganancia total: {ganancia_total}")
print(f"Ganancia porcentual: {ganancia_ptc:.2f}%")
print(f"Meta diaria: {meta_diaria}%")