total = 0
n = int(input('Ingresar n->'))
for i in range(1,n+1):
    if i% 2 == 1:
        total = total + (1/i)
    else:
        total = total - (1/i)
print(total)