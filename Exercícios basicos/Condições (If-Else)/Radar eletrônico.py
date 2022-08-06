velocidade = int(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    soma = (velocidade - 80) * 7  # soma da multa para cada km acima da velocidade permitida
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa de R${soma:.2f}')
print('Tenha um bom dia! Dirija com segurança!')
