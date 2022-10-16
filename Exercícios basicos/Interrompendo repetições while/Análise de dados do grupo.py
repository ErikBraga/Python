tot18 = totM = totF = 0
while True:
    print('-' * 30)
    print(f'{"CADASTRE UMA PESSOA":^30}')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    continuar = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 30)
    if idade >= 18:
        tot18 += 1  # se "idade" for maior ou igual a 18 anos "tot18" recebe +1
    if sexo == 'M':
        totM += 1  # se "sexo" for igual a M (masculino) "totM" recebe +1
    if sexo == 'F' and idade < 20:
        totF += 1  # se o "sexo" for igual a F (feminino) e "idade" for menor que 20 "totF" recebe +1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-' * 30)
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de homens cadastrados: {totM}')
print(f'Total de mulheres com menos de 20 anos cadastradas: {totF}')

