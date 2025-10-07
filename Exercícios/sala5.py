a = 1
somafinal = 0
contador = 0
while a != 0:
    a = float(input("\nDigite um valor pra ser agregado na lista (O NUMERO ZERO ENCERRA O PROGRAMA): "))
    somafinal += a
    contador +=1
print(f"O usuário informou {contador-1} números")   
print(f"\nA soma final do caralho todo foi de: {somafinal}\nA media final das somas feitas foi de: {somafinal/(contador-1):.2f}\n")