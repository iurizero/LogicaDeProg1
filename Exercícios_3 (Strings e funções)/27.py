def soma_de_lista(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma


tamanho_lista = int(input("Digite o tamanho da lista que quer preencher e somar: "))

lista = []

for i in range (tamanho_lista):
    lista.append(int(input(f"Digite o {i+1} valor a incorporar na lista: ")))
    
print(lista)
print(f"\nO valor de soma da lista é: {soma_de_lista(lista)}")