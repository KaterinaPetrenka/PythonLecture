#lecture_1

vek = input("Zadej vek: ")

try:
    vek = int(vek)

    if vek > 12 and vek < 20:
        print("jsi teenager")
    else: 
        print("Nejses teenager")

except:
    print('neplatna hodnota')

