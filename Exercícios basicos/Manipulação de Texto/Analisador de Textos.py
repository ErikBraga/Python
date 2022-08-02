nome = str(input('Digite seu nome completo: ')).capitalize().strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome.replace(" ", ""))} letras')
nome = nome.split()
print(f'Seu primeiro nome é {nome[0]} e ele tem {len(nome[0])} letras')


