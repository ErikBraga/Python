valores = []
cont = 0
while True:
    valores.append(int(input('Digite um valor: ')))  # adiciona à lista "valores" quantos valores o usuário quiser
    cont += 1  # contador de cada número adicionado na lista "valores"
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Tente novamente...', end='')
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
valores.sort(reverse=True)  # organiza a lista em ordem decrescente
print('-=' * 30)
print(f'Você digitou {cont} elementos.')
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:  # se o número 5 estiver presente na lista "valores"
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista')
