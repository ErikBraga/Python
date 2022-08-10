peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura (m) '))
imc = peso / (altura * altura)  # calculo de IMC
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:  # se o imc estiver abaixo de 18.5
    print('Você está abaixo do peso.')
elif 18.5 == imc <= 24.9:  # se o imc estiver entre 18.5 e 24.9
    print('Você está com um peso normal.')
elif imc <= 29.9:  # se o imc estiver entre 25 e 29.9
    print('Você está com sobrepeso.')
elif imc <= 34.9:  # se o imc estiver entre 30 e 34.9
    print('Você está com obesidade grau I.')
elif imc <= 39.9:  # se o imc estiver entre 35 e 39.9
    print('Você está com obesidade grau II.')
else:  # se o imc estiver igual ou acima de 40
    print('Você está com obesidade grau III.')
