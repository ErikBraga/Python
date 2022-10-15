sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'MF':
    print('Dados inválidos. Por favor, ', end='')
    sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
if sexo == 'F':
    print('Sexo feminino registrado com sucesso!')
else:
    print('Sexo masculino registrado com sucesso!')
