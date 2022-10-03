import sys
znamky = sys.argv[1:]

# Je možné použít i proměnné a mít na každou známku proměnnou
# My použijeme seznam
# Na pozici 0 je počet jedniček, na pozici 1 počet dvojek atd
pocet_znamek = [0, 0, 0, 0, 0]

for znamka in znamky:
    znamka = int(znamka)
    # Musím od pozice odečíst 1, protože známky jsou od 1 a Python čísluje od 0
    pocet_znamek[znamka - 1] = pocet_znamek[znamka - 1] + 1
print("Vypisuji počet známek: ")

aktualni_znamka = 1
for pocet in pocet_znamek:
    print("Počet známek", aktualni_znamka, "je", pocet)
    aktualni_znamka = aktualni_znamka + 1
