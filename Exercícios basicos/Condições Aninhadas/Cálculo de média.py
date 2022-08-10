pn = float(input('Primeiro nota: '))
sn = float(input('Segunda nota: '))
media = (pn + sn) / 2  # calculo da média das notas do aluno
print(f'Tirando {pn} e {sn}, a média do aluno é {media:.1f}')
if media < 5:  # se a média for menor que 5 o aluno está reprovado
    print('O aluno está REPROVADO.')
elif 5 <= media < 7:  # se a média está entre 5 e 6.9 o aluno está de recuperação
    print('O aluno está de RECUPERAÇÃO.')
else:  # se a média for de 7 ou superior ele está aprovado
    print('O aluno está APROVADO.')
