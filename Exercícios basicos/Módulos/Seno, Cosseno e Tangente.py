from math import cos, sin, tan, radians

angulo = float(input('Digite o ângulo que você deseja: '))
conversão = radians(angulo)  # conversão para radianos
print(f'O ângulo de {angulo} tem o SENO de {sin(conversão):.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {cos(conversão):.2f}')
print(f'O ângulo de {angulo} tem o TANGENTE de {tan(conversão):.2f}')
