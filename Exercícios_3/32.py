def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

def mmc(a, b):
    return (a * b) // mdc(a, b)

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(f"O MMC entre {num1} e {num2} é {mmc(num1, num2)}")
