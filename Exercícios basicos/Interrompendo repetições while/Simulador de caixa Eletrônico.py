print('=' * 30)
print(f'{"BANCO CDB":^30}')
print('=' * 30)
notas50 = notas20 = notas10 = notas1 = 0  # todas as notas disponiveis no caixa
while True:
    valor = int(input('Que valor você quer sacar? R$'))
    while valor >= 50:  # enquanto "valor" for maior que 50
        valor -= 50  # "valor" recebe -50
        notas50 += 1  # "notas50" recebe +1
    while valor >= 20:
        valor -= 20
        notas20 += 1
    while valor >= 10:
        valor -= 10
        notas10 += 1
    while valor >= 1:
        valor -= 1
        notas1 += 1
    break
if notas50 >= 1:  # sequencia de if para não printar variáveis sem valor
    print(f'Total de {notas50} cédulas de R$50')
if notas20 >= 1:
    print(f'Total de {notas20} cédulas de R$20')
if notas10 >= 1:
    print(f'Total de {notas10} cédulas de R$10')
if notas1 >= 1:
    print(f'Total de {notas1} cédulas de R$1')
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
