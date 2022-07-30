salario = float(input('Qual é o salário do Funcionário? R$'))
porcentagem = 15/100 * salario
print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${salario+porcentagem:.2f}')
