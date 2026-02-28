import time

print("Baligya ginagmay dri sa gamay nga system")
time.sleep(0.2)
ngalan = input("Ngalan diay nimo?: ")
time.sleep(0.2)
print(f'Hi {ngalan} welcome diay ka sa among store ')
print("<------------------------------------------------>")
#Price ni dri bai 
Saging = 10
Mangga = 20
Manok = 150
#Output sa baligya bai
time.sleep(0.2)
baligya = int(input(f"""Ang baligya namo diri bai {ngalan} kay\n
1. Saging = $10
2. Mangga = $20
3. Manok = $150\nPili na kay barato pa!: """))
print(f"So gi pili nimo kay {baligya} bai {ngalan}!")

print("<-------------------------------------------------->")
#Bayad niya eh
time.sleep(0.2)
bayad = float(input(f"Syempre mo bayad sa ka bai {ngalan} eh alangan. Bayad: "))
#Logic na dri bai tarunga
try:
    if baligya == 1:
        print(f"Saging imong paliton bai {ngalan}")
        Baligya = Saging
    elif baligya == 2:
        print(f"Mangga diay imong paliton bai {ngalan}")
        Baligya = Mangga
    elif baligya == 3:
        print(f"Manok diay imong paliton bai {ngalan}")
        Baligya = Manok
    else:
        print(f"Invalid mana imong choice bai {ngalan}")
        
    if bayad < baligya:
        print(f"Pamayot sa bai {ngalan}")
        print("Kulang imong kwarta")
        exit()
    else:
        sukli = (bayad - Baligya)
        print(f"Ang sukli nimo kay {sukli}")
    
except Exception as e:
    print("Naay problema bai", e)

time.sleep(0.2)    
print("Salamat sa pag palit sundo napod...")    
                
