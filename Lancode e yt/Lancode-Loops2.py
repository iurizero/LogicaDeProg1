print("\nBem vindo ao contador de vogais")
print("--------------------------")

frase=str(input("\nDigite uma palavra: "))
frase=frase.lower()
vogais="aeiou"
final=[]

for i in frase:
    if i in vogais:
        if i not in final:
            final.append(i)
        
print(f"A palavra {frase} tem as seguintes vogais: {final}")