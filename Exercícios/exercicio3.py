print("BEM VINDO AO SISTEMA DE VERIFICAR IDADES")
print("-----------------------------------")
idade=int(input("Insira a idade a ser verificada: "))

if idade>=0 and idade<=12:
    print("\nLEGAL! VOCÊ É UMA CRIANÇA")

elif idade>=13 and idade<=17:
    print("\nLEGAL! VOCÊ É UM ADOLESCENTE")

elif idade>=18 and idade<=59:
    print("\nLEGAL! VOCÊ É UM ADULTO")

elif idade>=60 and idade<=120:
    print("\nLEGAL! VOCÊ É UM IDOSO")

else:
    print("\nValor inserido errado, favor repetir a execução do programa")
    
print("-----------------------------------") 