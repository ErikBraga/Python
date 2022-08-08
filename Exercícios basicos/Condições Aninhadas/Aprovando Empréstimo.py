valor_casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
parcelas = valor_casa / (anos * 12)  # valor total da casa dividido pelo número de meses
print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anos a prestação será de R${parcelas:.2f}')
if parcelas > salario * 30 / 100:  # se a parcela custar mais que 30% do salário do comprador, o empréstimo é negado
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo APROVADO!')
