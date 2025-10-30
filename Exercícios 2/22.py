metragem = float(input("Digite o tamanho de metros quadrados existente no ambiente a ser pintado: "))

litragem = metragem/3
contador = 0

while contador < litragem:
    contador+=1


tintas = contador/18
if tintas%2 !=0:
    tintas+=1
    
tintas = int(tintas)
preco_final = tintas*80

print(f"Será necessário {tintas:.0f} latas de tinta para pintar a metragem informada, o valor final é de {preco_final:.2f}R$")