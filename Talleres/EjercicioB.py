from random import randint as ri
ListaABC = [[ri(-100,100),ri(-100,100),ri(-100,100)] for i in range(100)]
if Ver:
    for i,j in enumerate(ListaABC):
        print(f'{str(i+1).zfill(3)}-->\t{j}')
		
for i in ListaABC[:5]:
    print(i)
    print('\t', i[0], i[1], i[2], sep='-->')
	
# #Solución
def fb(a,b,c):
    """
    Funcion para utilizar la ecuacion de ax2+bx+c=0 con la formula del bachiller
    Tiene dos soluciones
    Tiene única solución
    No tiene solución en los reales
    """
    d = b*b-(4*a*c)
    if d > 0:
        x1 = (-b+(d**(1/2)))/(2*a)
        x2 = (-b-(d**(1/2)))/(2*a)
        return ['Tiene dos soluciones',x1,x2]
    elif d == 0:
        x0 = (-b)/(2*a)
        return ['Tiene única solución', x0]
    else:
        return ['No tiene solución en los reales']
fb(1,6,3)

def ValidarDatosABC(lista):
    vc = 0
    for i in lista:
        resultado = fb(i[0], i[1], i[2])
        lista[vc].extend(resultado)
        vc+=1
    return lista
print(ValidarDatosABC(ListaABC[:3]))