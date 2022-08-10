print('-=' * 15)
print('Analisador de Triângulos')
print('-=' * 15)
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:  # calcula se a soma de dois lados vai ser maior que o terceiro lado
    if l1 == l2 == l3:  # se todos os segmentos forem iguais
        print('Os segmentos acima PODEM formar um triângulo EQUILÁTERO')
    elif l1 == l2 or l1 == l3 or l2 == l3:  # se apenas dois segmentos forem iguais
        print('Os segmentos acima PODEM formar um triângulo ISÓSCELES')
    elif l1 != l2 and l1 != l3 and l2 != l3:  # se todos os segmentos forem diferentes
        print('Os segmentos acima PODEM formar um triângulo ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')
