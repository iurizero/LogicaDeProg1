def multiplos(x, y):
    if x%y == 0:
        return(True)
    else:
        return(False)
    
a = float(input("Digite o numero que você quer testar se é multiplo: "))
b = float(input("Digite o numero que seria o multiplicador: "))

if multiplos(a,b) == True:
    print(f"O número {a} é sim um multiplo de {b}")
else:
    print(f"O número {a} NÃO É MÚLTIPLO de {b}")
