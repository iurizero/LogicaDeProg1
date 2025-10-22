dia_nascimento = int(input("Digite o dia que você nasceu (1 - 31): "))
while dia_nascimento < 1 or dia_nascimento > 31:
    dia_nascimento = int(input("Dia inválido, informe um valor entre 1 e 31: "))
    
mes_nascimento = int(input("Digite o mês que você nasceu (1-12): "))
while mes_nascimento < 1 or mes_nascimento > 12:
    dia_nascimento = int(input("Dia inválido, informe um valor entre 1 e 31: "))

ano_nascimento= int(input("Digite seu ano de nascimento: "))
while ano_nascimento < 1500 or ano_nascimento > 2025:
    dia_nascimento = int(input("Dia inválido, informe um valor entre 1 e 31: "))

meses_30_dias = [4, 6, 9, 11]

if mes_nascimento == 2:
    while dia_nascimento > 28 or dia_nascimento < 1:
        dia_nascimento = int(input("Dia inválido, o mês informado tem 28 dias insira um valor entre 1 e 28: "))
elif mes_nascimento in meses_30_dias:
    while dia_nascimento > 30 or dia_nascimento < 1:
        dia_nascimento = int(input("Dia inválido, o mês informado tem 28 dias insira um valor entre 1 e 30: "))

anos = 2025 - ano_nascimento 

meses = (2025 - ano_nascimento) * 12 + (11 - mes_nascimento)

contador_bissextos = 0
for ano in range(ano_nascimento, 2025):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        contador_bissextos += 1
    
dias = meses*31 + contador_bissextos

print(f"Você tem {anos} anos! Que seria equivalente a {meses} meses ou {dias} dias!")