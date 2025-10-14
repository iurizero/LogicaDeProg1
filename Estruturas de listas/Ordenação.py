l = [10, 9, 8, 2, 3, 4]
lista_ordenada = []
for i in range (len(l)):
    maior_nota =  max(l)
    lista_ordenada.append(maior_nota)
    l.pop(l.index(maior_nota))
    
print(lista_ordenada)
