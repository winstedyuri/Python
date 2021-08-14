L = [-1, 0, 1, 2]

def maior(L):
    maior = None
    for i in L:
        if maior is None or i > maior:
            maior = i
        return maior

print("A soma dos valores é de:", maior)

print("A média é de:", maior/4)

media = maior/4

if media >= 1:
    print("O valor é positivo")

else: 
    print("O valor é negativo")

