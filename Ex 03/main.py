notas = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

soma_das_notas = 0

for nota in notas:
    soma_das_notas += nota

print(soma_das_notas)

media = soma_das_notas/20

print("A média é de:", media)

print('A valor máximo é:', max(notas))

print('A valor mínimo é:', min(notas))