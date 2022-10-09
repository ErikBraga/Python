from datetime import date
maior = menor = 0  # duas variáveis com valor 0
ano = date.today().year  # ano atual do computador
for c in range(1, 8):
    pessoas = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    if ano - pessoas >= 18:  # descobre se a pessoa é maior de idade
        maior += 1
    else:  # se não, ela é menor de idade
        menor += 1
if maior == 1:  # se caso a variável "maior" tiver apenas uma pessoa
    print(f'Ao todo tivemos {maior} pessoa maior de idade')
else:  # se a variável "maior" tiver mais de uma pessoa
    print(f'Ao todo tivemos {maior} pessoas maiores de idade')
if menor == 1:  # se caso a variável "menor" tiver apenas uma pessoa
    print(f'E também tivemos {menor} pessoa menores de idade')
else:  # se a variável "menor" tiver mais de uma pessoa
    print(f'e também tivemos {menor} pessoas menores de idade')
