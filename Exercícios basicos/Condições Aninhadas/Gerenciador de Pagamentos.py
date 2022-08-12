print(f'{" Lojas Guanabara ":=^40}')
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
escolha = int(input('Qual é a opção? '))
if escolha == 1:  # se a escolha for à vista
    desconto = preco * 10 / 100  # recebe um desconto de 10%
    print(f'Sua compra de R${preco:.2f} vai custar R${preco - desconto:.2f} no final.')
elif escolha == 2:  # se a escolha for à vista no cartão
    desconto = preco * 5 / 100  # recebe um desconto de 5%
    print(f'Sua compra de R${preco:.2f} vai custar R${preco - desconto:.2f} no final.')
elif escolha == 3:  # se escolha for em 2 vezes no cartão
    print(f'Sua compra será parcelada em 2x de {preco / 2:.2f}')
elif escolha == 4:  # se a escolha for em 3x ou mais no cartão
    parcelas = int(input('Quantas parcelas? '))  # número de parcelas desejadas
    juros = preco * 20 / 100  # juros de 20%
    print(f'sua compra será parcelada em {parcelas}x de R${(preco + juros) / parcelas:.2f} COM JUROS')
    print(f'Sua compra de R${preco:.2f} vai custar R${preco + juros:.2f} no final.')
else:
    print('Escolha inválida.')
