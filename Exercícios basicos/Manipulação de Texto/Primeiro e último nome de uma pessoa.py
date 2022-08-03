nome = str(input('Digite seu nome completo: ')).title().split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')  # printa o primeiro nome da string
print(f'Seu último nome é {nome[-1]}')  # printa o último nome da string independente do tamanho
