from math import hypot

cto = float(input('Comprimento do cateto oposto: '))
cta = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {hypot(cto, cta):.2f}')


