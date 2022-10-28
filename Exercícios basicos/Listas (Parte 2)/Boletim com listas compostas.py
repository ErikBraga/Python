alunos = []
temp = []
while True:
    temp.append(str(input('Nome: ')).strip().capitalize())
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    alunos.append(temp[:])  # adiciona uma cópia de "temp" na lista "alunos"
    temp.clear()  # limpa a lista "temp" para receber novos números
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 20)
print(f'No. NOME {"MÉDIA":>13}')
print('-' * 25)
for i, p in enumerate(alunos):
    print(f'{i}   {p[0]:<14}{(p[1] + p[2]) / 2:.1f}')  # p[1] = nota1, p[2] = nota2 / 2 para calcular a média
print('-' * 25)
while True:
    notas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if notas < len(alunos):
        print(f'Notas de {alunos[notas][0]} são {alunos[notas][1:]}')
        print('-' * 30)
    if notas == 999:
        break
