print('-=' * 15)
print('Analisador de Triângulos')
print('-=' * 15)
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:  # calcula se a soma de dois lados vai ser maior que o terceiro lado
    print('Os segmentos acima PODEM formar um triângulo.')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')
