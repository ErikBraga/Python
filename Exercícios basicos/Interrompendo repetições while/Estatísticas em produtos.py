tot = mais_barato = mais_mil = cont = 0
nome_barato = ''
print('-' * 30)
print(f'{"LOJA SUPER BARATÃO":^30}')
print('-' * 30)
while True:
    produto = str(input('Nome do Produto: ')).strip().capitalize()
    preco = float(input('Preço: R$'))
    cont += 1
    tot += preco
    if preco >= 1000:
        mais_mil += 1
    if cont == 1:
        mais_barato = preco
        nome_barato = produto
    elif preco < mais_barato:
        mais_barato = preco
        nome_barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'{"FIM DO PROGRAMA":-^30}')
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos apenas um produto custando mais de R$1000.00' if mais_mil == 1 else f'Temos {mais_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_barato} que custa R${mais_barato:.2f}')


