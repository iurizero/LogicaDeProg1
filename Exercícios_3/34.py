def validar_string(string):
    if len(string) <= 1 and len(string) >= 10:
        return True
    else:
        return False

texto = str(input("Digite o seu texto: "))

if validar_string(texto):
    print("A string está dentro do limite de caracteres")
else:
    print("A string não está dentro do limite de 10 caracteres")
