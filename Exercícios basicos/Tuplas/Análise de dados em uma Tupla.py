numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print(f'Você digitou os valores {numeros}')
if numeros.count(9) == 1:
    print(f'O valor 9 apareceu {numeros.count(9)} vez')
elif numeros.count(9) == 0:
    print(f'O valor 9 não aparece na lista')
else:
    print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if numeros.count(3) == 1:
    print(f'O valor 3 apareceu {numeros.index(3) + 1}ª posição')
else:
    print('O valor 3 não aparece na lista')
print(f'Os valores pares digitados foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
