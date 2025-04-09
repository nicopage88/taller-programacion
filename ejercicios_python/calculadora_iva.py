def calcular_iva(monto, tasa_iva=0.19):
    """Calcula el IVA de un monto dado."""
    iva = monto * tasa_iva
    total_con_iva = monto + iva
    return iva, total_con_iva

# Ejemplo de uso
try:
    monto = float(input("Ingresa el monto: $"))
    iva, total_con_iva = calcular_iva(monto)
    print(f"IVA (19%): ${iva:.2f}")
    print(f"Total con IVA: ${total_con_iva:.2f}")
except ValueError:
    print("Por favor, ingresa un monto válido.")
