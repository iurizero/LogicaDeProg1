print("BEM VINDO AO SISTEMA DE VERIFCAR NUMEROS MAIORES")
print("-----------------------------------")
valor1=int(input("Insira o primeiro valor a ser verificado: "))
valor2=int(input("Insira o segundo valor a ser verificado: "))
valor3=int(input("Insira o terceiro valor a ser verificado: "))

if valor1>valor2 and valor1>valor3:
    print("\nO PRIMEIRO VALOR INFORMADO É O MAIOR")

elif valor2>valor1 and valor2>valor3:
    print("\nO SEGUNDO VALOR INFORMADO É O MAIOR")
    
else:
    print("\nO TERCEIRO VALOR INFORMADO É O MAIOR")
    
print("-----------------------------------") 