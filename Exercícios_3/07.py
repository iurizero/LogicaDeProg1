string = str(input("Informe a string desejada: ")).lower()

ja_mostradas = ""

for i in string:
    if i not in ja_mostradas:
        print(f"A letra {i} aparece {string.count(i)} vez!")
        ja_mostradas += i 



