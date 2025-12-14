def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(f"O MDC entre {num1} e {num2} é {mdc(num1, num2)}")
