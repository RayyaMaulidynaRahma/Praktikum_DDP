total = 0

for angka in range(1, 20, 2):
    total += angka
    
    if angka == 19:
        print(angka ,end="=")
        
    else:
        print(angka, end="+")
        
print(total)