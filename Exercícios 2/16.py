cigarros_por_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos_fumo = int(input("Digite há quantos anos você fuma: "))


minutos_por_cigarro = 10
minutos_em_um_dia = 24 * 60

total_cigarros = anos_fumo * 365 * cigarros_por_dia
total_minutos_perdidos = total_cigarros * minutos_por_cigarro
dias_perdidos = total_minutos_perdidos / minutos_em_um_dia

print(f"Você perdeu aproximadamente {dias_perdidos:.0f} dias de vida.")
