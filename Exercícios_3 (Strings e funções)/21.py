def maior_numero (x,y):
    if x > y:
        print(f"O numero {x} é o maior")
    
    elif x < y:
        print(f"O numero {y} é o maior")

    elif x == y:
        print("Os dois números tem o mesmo valor")
        
a = float(input("Digite um número: "))
b = float(input("Digite outro numero a ser comparado: "))

maior_numero(a,b)