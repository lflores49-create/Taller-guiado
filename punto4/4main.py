alcancia = [100, 200, 500]
meta = 1000

total = sum(alcancia)

if total >= meta:
    print("¡Felicidades! Alcanzado tu meta de ahorro.")
else:
    falta = meta - total
    print(f"Aún te faltan {falta} pesos para alcanzar tu objetivo.")
