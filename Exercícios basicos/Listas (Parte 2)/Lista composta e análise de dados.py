pessoas = []
dados = []  # lista temporaria
maior_peso = menor_peso = 0
while True:
    dados.append(str(input('Nome: ')).strip().capitalize())  # adiciona o "nome" na lista "dados"
    dados.append(float(input('Peso: ')))  # adiciona o "peso" na lista "dados"
    if len(pessoas) == 0:  # se a lista "pessoas" tiver vazia
        maior_peso = dados[1]  # "maior_peso" recebe o primeiro peso registrado
        menor_peso = dados[1]  # "menor_peso" recebe o primeiro peso registrado
    else:
        if dados[1] > maior_peso:  # se o proximo peso digitado for maior que o "maior_peso"
            maior_peso = dados[1]
        if dados[1] < menor_peso:  # se o proximo peso digitado for menor que o "menor_peso"
            menor_peso = dados[1]
    pessoas.append(dados[:])  # a lista "pessoas" recebe uma cópia da lista "dados"
    dados.clear()  # lista "dados" é limpada para receber novos valores temporariamente
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior_peso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior_peso:  # se p[1] for o maior peso da lista "pessoas"
        print(f'[{p[0]}]', end=' ')  # printa o nome das pessoas com o maior peso da lista
print()
print(f'O menor peso foi de {menor_peso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor_peso:  # se p[1] for o menor peso da lista "pessoas"
        print(f'[{p[0]}]', end=' ')  # printa o nome das pessoas com o menor peso da lista
print()
