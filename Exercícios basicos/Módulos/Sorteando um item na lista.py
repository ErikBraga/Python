from random import choice

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
alunos = [a1, a2, a3, a4]  # cria uma lista com os 4 alunos
print(f'O aluno escolhido foi {choice(alunos).capitalize()}')  # escolhe um aluno aleatório da lista "alunos"
