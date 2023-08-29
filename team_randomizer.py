import random

valid3 = False

while not valid3:

    il_zaw = "-1"
    il_dru = "-1"
    valid1 = False

    while not valid1:
        try:
            il_zaw = int(input("Ilość zawodników: "))
            if il_zaw <= 0:
                print("wprowadź liczbę całkowitą")
                continue
            valid1 = True
        except ValueError:
            print("wprowadź liczbę całkowitą")

    valid2 = False

    while not valid2:
        try:
            il_dru = int(input("Ilość drużyn: "))
            if il_dru <= 0:
                print("wprowadź liczbę całkowitą")
                continue
            valid2 = True
        except ValueError:
            print("wprowadź liczbę całkowitą")

    if il_zaw//il_dru > 1 and il_zaw%il_dru == 0:
        valid3 = True

zawodnicy=[]
druzyny=[]
zaw_na_dru = il_zaw//il_dru

print("\n+-----------------------------------------------+\nPodaj imiona zawodników:")
for i in range(int(il_zaw)):
    zawodnicy.append(input(f'{i+1}. '))

def losowanie_skladow():
    zawodnicy_temp=zawodnicy.copy()
    druzyny_temp=druzyny.copy()
    for j in range(0, il_dru):
        druzyny_temp.append([])
        for k in range(0, zaw_na_dru):
            ran = random.randint(0, len(zawodnicy_temp)-1)
            druzyny_temp[j].append(zawodnicy_temp.pop(ran))

    for indeks_1, druzyna in enumerate(druzyny_temp):
        print()
        print(f"Drużyna {indeks_1+1}")
        for indeks_2, player in enumerate(druzyna):
            print(f"{indeks_2+1}. {player}")
    print()
    print()
    print()
losowanie_skladow()

while True:
    button = input("Wylosować ponownie?\n-TAK ==> T\n-NIE ==> N\nDecyzja: ")
    if button == "T":
        losowanie_skladow()
    else:
        break