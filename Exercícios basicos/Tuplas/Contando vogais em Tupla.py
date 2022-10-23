lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for palavras in lista:
    print(f'\nNa palavra {palavras} temos ', end='')
    for letras in palavras:
        if letras in 'AEIOU':
            print(letras.lower(), end=' ')
