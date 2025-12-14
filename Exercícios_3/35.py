def checagem_palavra(palavra, lista):
    if palavra in lista:
        return True
    else:
        return False

lista = ['maçã', 'banana', 'jaca', 'laranja', 'pitanga', 'acerola']

fruta = str(input("Digite uma fruta pra ver se está entre as desejadas: "))

if checagem_palavra(fruta, lista):
    print(f"A fruta {fruta} estava dentro das permitidas!")

else:
    print(f"Infelizmente você errou, as frutas permitidas eram: {lista}")