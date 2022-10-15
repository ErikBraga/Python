fatorial = int(input('Digite um número para\ncalcular seu Fatorial: '))
num = fatorial  # variável para guardar o valor do fatorial, usado para informação no final do código
soma = fatorial
while fatorial != 1:
    fatorial -= 1
    soma *= fatorial
print(f'O fatorial de {num}! é {soma}')
