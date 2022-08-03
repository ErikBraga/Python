nome = str(input('Qual é seu nome completo? ')).lower().split()  # "split" para separar o nome em listas e evitar erro no nome "Silvana" ou parecidos
print('Analisando seu nome')
print(f'Seu nome tem "Silva"? {"silva" in nome}')  # analisa se o nome "Silva" está presente na variável "nome"
