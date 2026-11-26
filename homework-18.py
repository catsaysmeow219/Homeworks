#1-rapsirma

jasi = int(input("Jasindi kiritin': "))

if jasi >= 18:
    print("Siz erjetkensiz")
else:
    print("Siz erjetpegensiz!")

#2-tapsirma
parol = input("Paroldi kirigizin': ")
if parol == "python123":
    print("Xosh keldin'iz!")
else:
    print("Porol naduris")

#3-tapsirma
bahasi = int(input("Mahsulot narxini kiriting: "))
print(f"Chegrma: {bahasi} so'm")
if bahasi > 50_000:
    print(f"Umumiy narx: {int(bahasi * 0.90)} so'm")
else:
    print(f"Umumiy narx: {bahasi} som")

#4-tapsirma
km = int(input("Araliq kiritn'iz: "))

if km > 10:
    print(f"1 km bahasi: 3000 sum")
    print(f"Uliwma bahasi: {km * 3000} sum")
else:
    print(f"1 km bahasi: 2000 sum")
    print(f"Uliwma bahasi: {km * 2000} sum")

#5-tapsirma
bahasi = int(input("Buyrtpa bahasi: "))


if bahasi > 100_000:
    print("Jetkerip beriw biypul!")
else:
    print(f"Jetkerip beriw: 15 000 sum")
    print(f"Ja'mi to'lem: {bahasi + 15000} sum")

#6-tapsirma
ball = int(input("Ballingizdi kiriting: "))

if 90 <= ball <= 100:
    print("A'lo")
elif 75 <= ball <= 89:
    print("Yaqshi")
elif 60 <= ball <= 74:
    print("Qoniqarli")
elif 0 <= ball <= 59:
    print("Qonqarsiz")
else:
    print(f"0 dan 100 gacha")

#7-tapsirma
transportlar = ["Avtobus", "Metro", "Taksi", "Velosiped"]
bahasi = [2000, 1700, 15000, 1000]
print("==== TRANSPORT TANLAW ====")
for i in range(len(transportlar)):
    print(f"{int(i) + 1} {transportlar[i]}")

transport = int(input("Transport tanlan': "))

if transport == 1:
    print(f"Siz {transportlar[transport - 1]} transportin tanladin'iz")
    print(f"Bahasi: {bahasi[transport - 1]}")
elif transport == 2:
    print(f"Siz {transportlar[transport - 1]} transportin tanladin'iz")
    print(f"Bahasi: {bahasi[transport - 1]}")
elif transport == 3:
    print(f"Siz {transportlar[transport - 1]} transportin tanladin'iz")
    print(f"Bahasi: {bahasi[transport - 1]}")
elif transport == 4:
    print(f"Siz {transportlar[transport - 1]} transportin tanladin'iz")
    print(f"Bahasi: {bahasi[transport - 1]}")
else:
    print("Bunday transfort joq")


#8-tapsirma
miyweler = ["alma", "banan", "juzim", "anar", "shaftali"]
kiritiw = input("Miywe atin kiritin'iz: ")

if kiritiw in miyweler:
    print(f"{kiritiw} royxatta bar!")
else:
    print(f"{kiritiw} royxatta joq!")

#9-tapsirma
oqiwshilar = ["Ali", "Vali", "Sardor", "Malika", "Madina"]
ati = input("Oqiwshi atin kirigizin': ")

if ati in oqiwshilar:
    print("Oqiwshi royxatta bar!")
    print(f"Birinshi harifi: {ati[0]}")
else:
    print("Bul oqiwshi royxatta joq!")

#10-tapsirma
numbers = [12, 5, 8, 17, 20, 3, 10, 7]

for number in numbers:
    if number % 2 == 0:
        print(f"{number} - jup san")
    else:
        print(f"{number} - taq san")

# 11-tapsirma

numbers = [2, 5, 8, 11, 14, 17]


for i in range(len(numbers)):
    if numbers[i] <= 10:
        numbers[i] = numbers[i] * 2
    else:
        numbers[i] = numbers[i] + 5

print(numbers)

#12-tapsirma
products = ["Go'sh", "Nan", "Sut", "Mayek", "Gurish"]
prices = [90000, 4000, 12000, 1800, 15000]

for i in range(len(products)):
    print(f"{int(i) + 1}. {products[i]} - {prices[i]}")

mahsulot = int(input("Qanday mahsulot kerek? ")) - 1
soni = int(input(f"{products[mahsulot]} neshtasi kerek? "))
summasi = prices[mahsulot] * soni

print(f"Mahsulot: {products[mahsulot]}")
print(f"Soni: {soni}")
print(f"Umumiy summasi: {summasi}")

#13-tapsirma
products = ["Nan", "Sut", "Go'sh", "Alma", "Banan"]
prices = [4000, 12000, 90000, 8000, 15000]

tavor = input("Qanday mahsulot kerek? ")
for i in range(1):
    if tavor in products:
        a = int(input(f"{tavor} neshtasi kerak? "))
        b = products.index(tavor)
        print(f"Umumiy summa: {prices[b] * a}")
    else:
        print("Unaqa mahsulot yoq!")

#14-tapsirma
grades = [
        [5, 4, 3],
        [4, 5, 5],
        [3, 2, 4]
    ]

    for i in range(len(grades)):
        for a in range(len(grades[i])):
            grades[0][0] = 4
            grades[1][1] = 4
            grades[1][2] = 4
            grades[2][1] = 3

    print(grades)   
    #15-tapsirma
    products = [
            ["Nan", 4000, 10],
            ["Sut", 12000, 5],
            ["Go'sh", 90000, 2],
            ["Alma", 8000, 0]
        ]

        for product in products:
            tavor_nomi = product[0]
            bahosi = product[1]
            soni = product[2]

            if soni < 5:
                print(f"{tavor_nomi}: ({soni} dana)")
                print("Status: Az qalǵan")
            else:
                print(f"{tavor_nomi}: ({soni} dana)")
                print("Status: Jetkilikli")")")
    ]
]")"))")")")"))")")")")")")")")")
