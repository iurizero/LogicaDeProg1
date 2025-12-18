def percorre_lista(lista, nivel):
    for item in lista:
        if type(item) == list:
            percorre_lista(item, nivel + 1)
        else:
            print("  " * nivel + str(item))

lista = [1, 2, [3, 4, [5]], 6]
percorre_lista(lista, 0)
