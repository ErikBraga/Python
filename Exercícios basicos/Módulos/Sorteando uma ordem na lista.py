from random import shuffle

a1 = str(input('Primeiro aluno: ')).capitalize()
a2 = str(input('Segundo aluno: ')).capitalize()
a3 = str(input('Terceiro aluno: ')).capitalize()
a4 = str(input('Quarto aluno: ')).capitalize()
lista = [a1, a2, a3, a4]  # cria uma lista com os 4 alunos
shuffle(lista)  # altera a ordem da variável "lista"
print('A ordem de apresentação será')
print(lista)

