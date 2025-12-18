def valida_faixa(numero, minimo, maximo):
    if minimo <= numero <= maximo:
        return True
    else:
        return False
    
valor = int(input("Digite um número: "))

if valida_faixa(valor, 10, 50):
    print("Número dentro da faixa permitida.")
else:
    print("Número fora da faixa.")
