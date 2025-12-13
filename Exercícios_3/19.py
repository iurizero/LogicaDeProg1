lista_nomes = []
palavra = ""
formatador = int(input("Digite a largura da coluna pra podermos começar: "))

for i in range (10):
    palavra = str(input(f"Digite o {i+1} nome da lista: "))[:formatador]
    lista_nomes.append(palavra)
    
print(lista_nomes)