valores = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:  # se o valor digitado em "num" não estiver na lista "valores", ele é adicionado
        valores.append(num)
        print('Valor Adicionado com sucesso...')
    else:  # se o valor digitado em "num" ja estiver na lista "valores", ele é ignorado
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 30)
print(f'Você digitou os valores {sorted(valores)}')  # print da lista organizada em ordem crescente

