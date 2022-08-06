import datetime

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year  # pega o ano atual do computador
soma = ano % 100  # divisão para pegar apenas os últimos 2 dígitos do número
if soma == 0:  # se a soma for igual a 0 significa que o número termina com 00, exemplo: 1900
    soma = ano % 400  # se o número terminado com 00 for divisível por 400 ele é bissexto
    if soma == 0:
        print(f'O ano {ano} é bissexto')
    else:
        print(f'O ano {ano} não é bissexto')
elif soma % 4 == 0:  # se os últimos 2 dígitos de um número for divisível por 4 ele é bissexto
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')
