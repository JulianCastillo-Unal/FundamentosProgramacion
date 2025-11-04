#Solución
def fLisPla(x):
    cumple = isinstance(x, list)
    if cumple:
        print('Hola, x es una lista')
    else:
        print('Chao, x no es una lista')

# lista = [1,2,3,4]
# print(isinstance(lista, list))4
fLisPla([1,2,3])


def ValidarLista(lista):
    """
    Reune todos los datos de una lista y genera una sumatoria y un maximo y un minimo de estos
    """
    suma= 0
    maximo, minimo = 0,0
    if (isinstance(lista, list)):
        for valor in lista:
            if isinstance(valor, (int, float)):
                pass
            else:
                return 'Error, no todos los valores son numericos'
        suma = sum(lista)
        maximo = max(lista)
        minimo = min(lista)
        return [suma, maximo, minimo]
    else:
        return 'Error, no es una lista'
		
x = [2,6,8,10,12,14,'i']
y = 'Hola, perdidossss'

print(ValidarLista(x))
print(ValidarLista(y))