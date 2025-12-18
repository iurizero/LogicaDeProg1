string1 = str(input("Digite a primeira string: ")).lower()
string2 = str(input("Digite a segunda string: ")).lower()

string_final = " "

for i in string1:
    if i not in string2:
        string_final += i 

for i in string2:
    if i not in string1:
        string_final += i 

print(f"O diabo sorriu e as strings exclusivas formam a string: {string_final}")
