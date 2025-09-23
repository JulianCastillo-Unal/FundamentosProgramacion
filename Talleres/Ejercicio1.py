e1 = int(input('Ingresar edad ->'))
e2 = int(input('Ingresar edad ->'))
if (e1 > (2*e2)) or (e2 > (2*e1)):
    print('El promedio de edades es:', (e1+e2)/2)
else:
    print('La diferencia es:', abs(e1-e2))