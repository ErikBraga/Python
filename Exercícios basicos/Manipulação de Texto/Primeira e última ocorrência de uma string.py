frase = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra "A" aparece {frase.count("a")} vezes na frase.')  # conta quantas vezes aparece a letra "A" na string
print(f'A primeira letra "A" apareceu na posição {frase.find("a")+1}')  # +1 para a contagem não começar no 0
print(f'A última letra "A" apareceu na posição {frase.rfind("a")+1}')  # +1 para não ficar um número desigual com o de cima
