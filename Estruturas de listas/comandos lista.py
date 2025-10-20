# ============================================================
# GUIA COMPLETO DE LISTAS EM PYTHON 🧱
# Autor: Iuri-Chan gepete da silva
# ============================================================

# --- Criação e Acesso ---
print("\n=== Criação e Acesso ===")
lista = [1, 2, 3, 4]
lista_vazia = []
print("Lista:", lista)
print("Primeiro elemento:", lista[0])
print("Último elemento:", lista[-1])
print("Fatiamento [1:3]:", lista[1:3])
print("Fatiamento [:2]:", lista[:2])
print("Fatiamento [2:]:", lista[2:])

# --- Modificação ---
print("\n=== Modificação ===")
lista = [10, 20, 30, 40]
lista[1] = 99
lista.append(50)
lista.insert(2, 15)
lista.extend([60, 70])
print("Lista modificada:", lista)

# --- Remoção ---
print("\n=== Remoção ===")
lista = [1, 2, 3, 4, 5]
lista.remove(3)
lista.pop()
lista.pop(1)
del lista[0]
print("Após remoções:", lista)
lista.clear()
print("Após clear():", lista)

# --- Busca e Informações ---
print("\n=== Busca e Informações ===")
lista = [10, 20, 30, 40, 30]
print("Lista:", lista)
print("Tamanho:", len(lista))
print("30 está na lista?", 30 in lista)
print("Quantidade de 30:", lista.count(30))
print("Índice do 40:", lista.index(40))

# --- Ordenação e Inversão ---
print("\n=== Ordenação e Inversão ===")
nums = [5, 3, 8, 1]
print("Original:", nums)
nums.sort()
print("Crescente:", nums)
nums.sort(reverse=True)
print("Decrescente:", nums)
nums.reverse()
print("Invertida:", nums)

# --- Iteração ---
print("\n=== Iteração ===")
lista = ["a", "b", "c"]
for item in lista:
    print("Item:", item)

for i, valor in enumerate(lista):
    print(f"Índice {i} -> Valor {valor}")

# --- Compreensão de Listas ---
print("\n=== Compreensão de Listas ===")
quadrados = [x**2 for x in range(5)]
pares = [x for x in range(10) if x % 2 == 0]
print("Quadrados:", quadrados)
print("Pares:", pares)

# --- Funções Úteis ---
print("\n=== Funções Úteis ===")
nums = [1, 2, 3, 4]
print("Soma:", sum(nums))
print("Máximo:", max(nums))
print("Mínimo:", min(nums))
print("Ordenado:", sorted(nums))

# --- Outros usos ---
print("\n=== Outros usos ===")
a = [1, 2, 3]
b = a.copy()
b.append(4)
print("Lista A:", a)
print("Cópia B:", b)
nova = a + [4, 5]
print("Concatenada:", nova)
repetida = [0] * 5
print("Repetida:", repetida)

print("\n=== Fim do Guia ✅ ===")
