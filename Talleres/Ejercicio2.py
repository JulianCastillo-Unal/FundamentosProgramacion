from math import sqrt
a = int(input('Ingresar a->'))
b = int(input('Ingresar b->'))
c = int(input('Ingresar c->'))
d = (b**2)-(4*a*c)
if d > 0:
    x1 = (-b+sqrt(d))/(2*a)
    x2 = (-b-sqrt(d))/(2*a)
    print(f'La ecuacion: \n\t{a}x²+{b}x+{c}=0, tiene dos soluciones')
    print(f'x1={x1:,.2f}')
    print(f'x2={x2:,.2f}')
elif d == 0:
    x0 = (-b)/(2*a)
    print(f'La ecuacion: \n\t{a}x²+{b}x+{c}=0, tiene unica solucion')
    print(f'x0={x0:,.2f}')
else:
    print('No tenemos respuesta en los reales.😒')