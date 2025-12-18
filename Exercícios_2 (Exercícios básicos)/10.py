def conversor_milimetros(num1):
    return num1 / 1000

num1 = float(input("Digite o valor em metros a ser convertido para milímetros: "))
resultado = conversor_milimetros(num1)
print(f"O valor em milímetros é: {resultado:.2f}")