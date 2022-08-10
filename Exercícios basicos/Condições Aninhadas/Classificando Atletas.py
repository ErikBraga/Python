from datetime import date

ano = int(input('Ano de nascimento: '))
ano_atual = date.today().year  # ano atual do computador
idade = ano_atual - ano
print(f'O atleta tem {idade} anos.')
print('Classificação: ', end='')
if idade <= 9:  # se a idade for menor ou igual a 9 anos o atleta é "mirim"
    print('MIRIM')
elif idade <= 14:  # se a idade for maior que 9 e menor ou igual a 14 o atleta é "infantil"
    print('INFANTIL')
elif idade <= 19:  # se a idade for maior que 14 e menor ou igual a 19 o atleta é "junior"
    print('JUNIOR')
elif idade <= 25:  # se a idade for maior que 19 e menor ou igual a 25 o atleta é "sênior"
    print('SÊNIOR')
else:  # se a idade for maior que 25 o atleta é "master"
    print('MASTER')
