lista_positivos = []
lista_negativos = []

for i in range(10):
    a = int(input(f"Digite o {i+1} número a ser checado: "))
    if a>=0:
        lista_positivos.append(a)
        
    else:
        lista_negativos.append(a)
        
print(f"A soma dos positivos digitados foi: {sum(lista_positivos)}")
print(f"Você inseriu {len(lista_negativos)} números negativos, sendo eles: {lista_negativos}")