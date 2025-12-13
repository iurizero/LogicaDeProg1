def procura_lista(i, lista):
    return lista.index(i)

lista = []
for i in range(10):
    lista.append(input(f"Digite o {i+1} valor a adicionar na lista: "))

checado = input("Digite o número pra ver em qual posição ele está na lista: ")

if checado in lista:
    print(f"\nO número {checado} está na {(procura_lista(checado, lista)) + 1} posição da lista.")
else:
    print("\nNúmero não encontrado na lista.")

print("\nLista completa:")
print(lista)
