# Practica de la semana 2
# Incluiremos como variable la tasa de interes de la FED
# Teniendo en cuenta que suele aumentar la liquidez en el mercado cuando estan bajas
# Puede lograr una apreciacion en las acciones al haber mas dinero barato para invertir

precio_entrada = 65000.0
precio_actual = 65455.0
meta_diaria = 0.7
stop_loss = -1.0 # Si perdemos mas del 1%, salir
ganancia_pct = (precio_actual - precio_entrada) / precio_entrada * 100
volumen_alto = True # Simulamos una condicion de mercado
tasas_interes = True # Tomamos true como altas, false como bajas

# Evaluacion de la situacion

if ganancia_pct <= stop_loss and not tasas_interes:
    print(f"STOP LOSS activado - Salir ya ({ganancia_pct:.2f}%)")
elif ganancia_pct <= stop_loss and tasas_interes:
    print(f"STOP LOSS activado - posible rebote, evaluar ({ganancia_pct:.2f}%)")
elif ganancia_pct >= meta_diaria and volumen_alto and tasas_interes:
    print(f"META ALCANZADA con volumen alto y tasas altas - Cerrar ({ganancia_pct:.2f}%)")
elif ganancia_pct >= meta_diaria and volumen_alto and not tasas_interes:
    print(f"META ALCANZADA con volumen alto y tasas bajas - Cerrar igual ({ganancia_pct:.2f}%)")
elif ganancia_pct >= meta_diaria and not volumen_alto:
    print(f"META ALCANZADA pero volumen bajo - Esperar ({ganancia_pct:.2f}%)")
else:
    print(f"En operacion normal ({ganancia_pct:.2f}%)")
