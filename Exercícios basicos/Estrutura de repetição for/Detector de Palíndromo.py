frase = str(input('Digite uma frase: ')).strip().upper()
junto = frase.replace(' ', '')  # tira os espaços no meio da string "frase"
inverso = ''  # variável inverso vazia
for letras in range(len(junto) - 1, - 1, - 1):  # pega o tamanho da string "junto", e vai voltando as letras começando pela última
    inverso += junto[letras]  # armazena a frase invertida na variável "inverso"
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')
