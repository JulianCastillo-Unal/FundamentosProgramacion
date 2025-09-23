#Solución
v = int(input('Ingresar el valor de la compra->'))
if v >= 1 and v <= 50_000:
    d = 1
elif v > 50_000 and v <= 100_000:
    d = 0.95
elif v > 100_000 and v <= 700_000:
    d = 0.89
elif v > 700_000 and v <= 1_500_000:
    d = 0.82
elif v > 1_500_000:
    d = 0.75
else:
    d = 0
total = v*d
print(f'El valor de la compra fue de {v:,.0f}, \n\tTotal = {total:,.2f}')