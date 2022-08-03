nome = str(input('Digite seu nome completo: ')).capitalize().strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')  # printa o nome em maiúsculo
print(f'Seu nome em minúsculas é {nome.lower()}')  # printa o nome em minúsculo
print(f'Seu nome tem ao todo {len(nome.replace(" ", ""))} letras')  # remove os espaços do nome e conta o total de letras
nome = nome.split()  # separa o nome em listas
print(f'Seu primeiro nome é {nome[0]} e ele tem {len(nome[0])} letras')  # conta quantas letras tem o nome da primeira lista
