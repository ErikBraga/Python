valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um número: ')))  # adiciona à lista quantos valores o usuário quiser
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Tente novamente...', end='')
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 30)
print(f'A lista completa é {valores}')  # print da lista "valores"
for n in valores:
    if n % 2 == 0:  # filtro de números pares da lista "valores"
        pares.append(n)
    else:  # filtro de números ímpares da lista "valores"
        impares.append(n)
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
