salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:  # se o salário for menor que 1250 o aumento é de 15%
    soma = salario * 15 / 100  # calculo da porcentagem
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${salario+soma:.2f} agora.')
if salario > 1250:  # se o salário for maior que 1250 o aumento é de 10%
    soma = salario * 10 / 100  # calculo da porcentagem
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${salario+soma:.2f} agora.')
