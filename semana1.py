# Variables - guardando informacion de mercado
precio_entrada = 65000.0
precio_actual = 65455.0
nombre_par = "BTC/USDT"
cantidad = 2
mercado_abierto = True

# Mostrando los valores
print(f"Precio de entrada: {precio_entrada}")
print(f"Precio actual: {precio_actual}")
print(f"Nombre del par: {nombre_par}")
print(f"Cantidad: {cantidad}")
print(f"Mercado abierto: {mercado_abierto}")

# Calculando resultados de la operacion
diferencia = precio_actual - precio_entrada
ganacia_total = diferencia * cantidad
ganacia_ptc = (diferencia / precio_entrada) * 100

# Mostrando los resultados
print(f"Diferencia: {diferencia}")
print(f"Ganancia total: {ganacia_total}")
print(f"Ganacia porcentual: {ganacia_ptc:.2f}%")

# Viendo el tipo de cada variable
print(type(precio_entrada))
print(type(nombre_par))
print(type(cantidad))
print(type(mercado_abierto))