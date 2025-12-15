texto = "matemática"
print(texto[0]) #TEXTOS FUNCIONAM COM INDICES
print(texto[-1]) #VER A ÚLTIMA LETRA
print(len(texto)) #Serve p ver o tamanho do texto

print("------------------------")

#repetição com for
for i in texto:
    print(i)
    
texto.upper() #Transforma tudo em maiúsculo
print(texto.upper())
texto.lower() #Transforma tudo em minúsculo
print(texto.lower())

#Verificar se está contido
frase = "O homem é alto e gosta de matemática"
if texto.lower() in frase.lower():
    print("Tudo certo!")
    
#Remoção de espaços em branco (SÓ REMOVE ESPAÇOS NO FINAL E COMEÇO DA STRING)
texto2 = "    Fique quieto    "
print(texto2)
print(texto2.strip())

#Seccionar a string
partes = frase.split()
print(partes)

partes2 = frase.split('m')
print(partes2)

#Readicionar strings seccionadas
frase = " ".join(partes) #Adiciona a uma nova variável uma lista que contenha apenas strings
print(frase)
frase = " ".join(partes2)
print(frase)
#Fatiamento de strings
texto = "matemática"

print(texto[0:4])   # mate
print(texto[:4])    # mate
print(texto[4:])    # mática
print(texto[::2])   # m t m t c
print(texto[::-1])  # acitámetam

#Métodos de busca
frase = "python é incrível"

print(frase.find("é"))    # retorna índice
print(frase.count("o"))   # quantas vezes aparece
print(frase.startswith("python"))
print(frase.endswith("ível"))

#Substituição de palavras
texto = "Eu gosto de matemática"
novo = texto.replace("matemática", "python")
print(novo)

#Verificação de tipos de texto
texto = "123"
print(texto.isdigit())
texto = "abc"
print(texto.isalpha())  
texto = "abc123"
print(texto.isalnum())
texto = "   "
print(texto.isspace())

"""📌 Resumo rápido — checklist do que falta
Se você souber tudo isso, pode considerar strings fechadas:
✅ Slicing
✅ Imutabilidade
✅ find, count, startswith, endswith
✅ replace
✅ isdigit, isalpha, isalnum, isspace
✅ f-strings
✅ join"""