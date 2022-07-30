valor = float(input('Qual é o preço do produto? R$'))
porcentagem = 5 / 100 * valor
print(f'O produto que custava R${valor}, na promoção com desconto de 5% vai custar R${valor-porcentagem:.2f}')
