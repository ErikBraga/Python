media = mais_velho = mulheres = 0
nome_velho = ''
for c in range(1, 5):  # analisador das informações de 4 pessoas
    print(f'-----  {c}ª PESSOA -----')
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    media += idade  # soma para o calculo da média do grupo
    if c == 1:
        mais_velho = idade
        nome_velho = nome
    elif idade > mais_velho and sexo == 'M':  # parâmetro para o nome e idade do homem mais velho do grupo
        mais_velho = idade
        nome_velho = nome
    if sexo == 'F' and idade < 20:  # para somar quantas mulheres do grupo tem menos de 20 anos
        mulheres += 1
print(f'A média de idade do grupo é de {media // 4} anos')  # média de idade do grupo
print(f'O homem mais velho tem {mais_velho} anos e se chama {nome_velho}')  # nome e idade do homem mais velho do grupo
if mulheres == 1:  # se a variável "mulheres" tiver apenas uma mulher
    print(f'O grupo possui apenas {mulheres} mulher com menos de 20 anos')
else:
    print(f'Ao todo são {mulheres} mulheres com menos de 20 anos')
