L = [10, 5, 9, 4, 5]
V = L

V[0] = 6

print("Primeira Lista")
print(L)

print("\nSegunda Lista")
print(V)
print("\nListas permanecem iguais mesmo com a alteração sendo feita em apenas uma dela")

print("\nAgora vamos ao exemplo correto")

G = [10, 5, 9, 4, 5]
J = G[:] #Jeito certo de copiar uma lista

G[0] = 5

print("\nPrimeira Lista")
print(G)

print("\nSegunda Lista")
print(J)