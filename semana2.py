# Bloque 1
"""
# El bot cubre todos los escenarios
precio_entrada = 65000.0
precio_actual = 64500.0

ganancia_pct = ((precio_actual - precio_entrada) / precio_entrada) * 100

if ganancia_pct >= 0.7:
    print(f"META ALCANZADA - Cerrar posicion ({ganancia_pct:.2f}%)")
elif ganancia_pct > 0:
    print(f"En ganancia, mantener posicion ({ganancia_pct:.2f}%)")
elif ganancia_pct == 0:
    print(f"Sin cambio ({ganancia_pct:.2f}%)")
else:
    print(f"En perdida - evaluar stop loss ({ganancia_pct:.2f}%)")
"""


# Bloque 2
"""
# Condicionales - el bot toma decisiones
# La meta como variable, no como numero magico
precio_entrada = 65000.0
precio_actual = 64500.0
meta_diaria = 0.7 # 0.7% de ganacia por dia operado


# Calculo

ganancia_pct = (precio_actual - precio_entrada) / precio_entrada * 100

if ganancia_pct >= meta_diaria:
    print(f"META ALCANZADA - Cerrar posicion ({ganancia_pct:.2f}%)")
elif ganancia_pct > 0:
    print(f"En ganacia, mantener posicion ({ganancia_pct:.2f}%)")
elif ganancia_pct == 0:
    print(f"Sin cambio ({ganancia_pct:.2f})")
else:
    print(f"En perdida - Evaluar stop loss ({ganancia_pct:.2f}%)")
"""


# Bloque 3
# Condiciones combinadas
precio_entrada = 65000.0
precio_actual = 64350.0
meta_diaria = 0.7
stop_loss = -1.0 # Si perdemos mas del 1%, salir

ganancia_pct = (precio_actual - precio_entrada) / precio_entrada * 100
volumen_alto = True # Simulamos una condicion de mercado

# Evaluacion de la situacion

if ganancia_pct >= meta_diaria and volumen_alto:
    print(f"META ALCANZADA con volumen alto - Cerrar posicion ({ganancia_pct:.2f}%)")
elif ganancia_pct >= meta_diaria and not volumen_alto:
    print(f"META ALCANZADA pero volumen bajo - Esperar ({ganancia_pct:.2f}%)")
elif ganancia_pct <= stop_loss:
    print(f"STOP LOSS activado - Salir ya ({ganancia_pct:.2f}%)")
else:
    print(f"En operacion normal ({ganancia_pct:.2f}%)")




