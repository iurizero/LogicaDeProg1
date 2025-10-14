L = []
x = 0
while True:
    x = int(input("Digite um valor (0 para sair): "))
    if x == 0:
        break
    else:
        L.append(x)

b = 0
while b < len(L):
    print(f"O valor digitado na posição {b+1} foi de {L[b]}")
    b += 1
print(f"\nA lista final digitada foi: {L}")