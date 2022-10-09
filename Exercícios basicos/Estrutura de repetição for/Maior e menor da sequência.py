maior_peso = menor_peso = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:  # se o contador estiver no primeiro parâmetro
        maior_peso = peso  # pega o primeiro valor "peso" que aparecer e coloca na variável "maior_peso"
        menor_peso = peso  # pega o primeiro valor "peso" que aparecer e coloca na variável "menor_peso"
    elif peso > maior_peso:  # se o peso for maior que a variável "maior_peso"
        maior_peso = peso
    elif peso < menor_peso:  # se o peso for menor que a variável "menor_peso"
        menor_peso = peso
print(f'O maior peso lido foi de {maior_peso}Kg')
print(f'O menor peso lido foi de {menor_peso}Kg')
