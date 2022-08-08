from datetime import date

nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year  # ano atual do computador
idade = ano_atual - nasc  # idade da pessoa com base no ano de nascimento
print(f'Quem nasceu em {nasc} tem {idade} anos em 2022.')
if idade < 18:
    rest = 18 - idade  # variável para saber quantos anos faltam para o alistamento
    if rest == 1:  # condição para evitar o erro de português em "anos"
        print(f'Ainda falta {rest} ano para o alistamento')
    else:
        print(f'Ainda faltam {rest} anos para o alistamento')
    print(f'Seu alistamento será em {ano_atual + rest}.')  # string para mostrar em que ano será o alistamento
elif idade > 18:
    rest = idade - 18  # variável para saber á quantos anos o alistamento está atrasado
    if rest == 1:
        print(f'Você já deveria ter se alistado há {rest} ano.')
    else:
        print(f'Você já deveria ter se alistado há {rest} anos.')
    print(f'Seu alistamento foi em {ano_atual - rest}.')  # string para mostrar em que ano foi o alistamento
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
