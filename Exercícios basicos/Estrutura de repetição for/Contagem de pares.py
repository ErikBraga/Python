for c in range(2, 51, 2):
    print(c, end=' ')  # contagem de pares

print()  # print apenas para quebrar a linha
for c in range(1, 51):
    if c % 2 == 0:  # segunda forma de contar pares usando "for"
        print(c, end=' ')
