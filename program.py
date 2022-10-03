import sys
poradi = int(sys.argv[1])

cisla = sys.argv[2:]
cisla = [int(cislo) for cislo in cisla]
nejvetsi_cisla = [cisla[0]]

for cislo in cisla[1:]:
    # Číslo je zatím největší, vložíme ho do seznamu největších čísel na začátek
    if cislo > nejvetsi_cisla[0]:
        nejvetsi_cisla = [cislo] + nejvetsi_cisla[:poradi-1]
        print(nejvetsi_cisla)
        # Číslo je již vložené do seznamu, můžeme tedy pokračovat dalším číslem
        continue
    for index in range(0, len(nejvetsi_cisla)):
        # Číslo je větší než některé z čísel v seznamu největších čísel, vložíme ho někam "doprostřed"
        if cislo > nejvetsi_cisla[index]:
            # Seznamy můžu "sčítat" podobně jako řetězce - součet seznamů znamená jejich "slepení" dohromady
            nejvetsi_cisla = nejvetsi_cisla[:index] + [cislo] + nejvetsi_cisla[index:poradi-1]
            print(nejvetsi_cisla)
            # Jakmile vložíme číslo do seznamu, přerušíme běh cyklu pomocí break
            # https://kodim.cz/kurzy/uvod-do-progr-2/bonusy/cykly-2/preruseni-cyklu
            break
    # Číslo je zatím nejmenší, ale seznam největších čísel je zatím příliš krátký, tak číslo vložíme nakonec
    if len(nejvetsi_cisla) < poradi and cislo not in nejvetsi_cisla:
        nejvetsi_cisla.append(cislo)
print(nejvetsi_cisla[-1])            
