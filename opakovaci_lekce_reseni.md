## Soubor JSON

```py
import json
with open("people.json", encoding="utf-8") as vstup:
    people = json.load(vstup)

"""
V této části pracujeme s daty uživatelky na nulté pozici
"""
# Vypiš jméno a příjmení
jmeno_prijmeni = people[0]["first_name"] + " " + people[0]["last_name"]
# Alternativní způsob výpisu pomocí f-stringů - formátovaných řetězců.
# Pozor na to, že je potřeba střídat uvozovky a apostrofy!
jmeno_prijmeni = f"{people[0]['first_name']} {people[0]['last_name']}"
# Kontroní tisk
print(jmeno_prijmeni)
# Zde si data neuložíme do řetězce, ale do seznamu, takže máme jméno a příjmení zvlášť
jmeno_prijmeni = [people[0]["first_name"], people[0]["last_name"]]
# Kontroní tisk
print(jmeno_prijmeni)
# Vypiš posledního kamaráda (kamarádku)
# Nejprve si kamarádky rozdělíme na seznam řetězců
seznam_kamaradek = people[0]["friends"].split()
posledni_kamaradka = seznam_kamaradek[-1]
# Zbavujeme se mezery na konci.
# Metoda strip odstraní zbytečné mezery (ty na začátku a konci řetězce)
print(posledni_kamaradka.strip())

"""
Nyní pracujeme s celým souborem
"""
# Vytvoření seznamu celých jmen pomocí chroustání seznamů
seznam_jmen = [x["first_name"] + " " + x["last_name"] for x in people]
# Jde to i přes formátované řetězce
seznam_jmen = [f"{x['first_name']} {x['last_name']}" for x in people]
print(seznam_jmen)
# Zde máme dvourozměrný seznam, jméno a příjmení zůstává zvlášť ve vnitřním seznamu
seznam_jmen = [[x["first_name"], x["last_name"]] for x in people]
print(seznam_jmen)

"""
Vytváříme CSV soubor se sloupci:
- jméno
- příjmení
- počet přátel
- město, kde bychom osobu zastihli (preferujeme korespondenční adresu, když není, tak trvalé bydliště)
"""
vystup = []
for person in people:
    jmeno = person["first_name"]
    prijmeni = person["last_name"]
    pocet_pratel = len(person["friends"].split(","))
    if "mail_address" in person:
        adresa = person["mail_address"].split("\n")
        # Výpis obce, kde žije uživatel
        mesto = adresa[-1][7:]
    else:
        adresa = person["permanent_address"].split("\n")
        mesto = adresa[-1][7:]
    radek = f"{jmeno},{prijmeni},{pocet_pratel},{mesto}\n"
    vystup.append(radek)

# Zapíšeme do souboru
with open("people.csv", mode="w", encoding="utf-8") as soubor:
    soubor.writelines(vystup)
# A to je vše, přátelé :-D
```

## Soubor TSV

```py
# Otevřeme soubor
with open("battles.tsv", encoding="utf-8") as soubor:
    radky = soubor.readlines()
# Rozdělíme řetězce na jednotlivé hodnoty - vznikne dvourozměrný seznam
radky = [x.split("\t") for x in radky]
# Zbavíme se řádku se záhlavím
radky = radky[1:]
# Zde máme připravený seznam na evidenci útočníků
utocnici = {}
# Zde máme připravený seznam bitev, kde vyhrála početně menší armáda
mensi_armada_vyhrala = []
for radek in radky:
    # Načítám útočníky
    # V souboru máme 4 sloupce, proto musíme načíst data ze všech sloupců
    utocnik = radek[5]
    if utocnik in utocnici:
        utocnici[utocnik] = utocnici[utocnik] + 1
    else:
        utocnici[utocnik] = 1
    utocnik = radek[6]
    # Útočník může být jen jeden, u dalších sloupců si už kontroluji, zda nejsou prázdné
    if radek[6] != "":
        if utocnik in utocnici:
            utocnici[utocnik] = utocnici[utocnik] + 1
        else:
            utocnici[utocnik] = 1
    if radek[7] != "":
        utocnik = radek[7]
        if utocnik in utocnici:
            utocnici[utocnik] = utocnici[utocnik] + 1
        else:
            utocnici[utocnik] = 1
    if radek[8] != "":
        utocnik = radek[8]
        if utocnik in utocnici:
            utocnici[utocnik] = utocnici[utocnik] + 1
        else:
            utocnici[utocnik] = 1

    """
    Nyní řeším, zda mám velikost obou armád.
    Pokud ano, převedu obě velikosti na číslo a porovnám, zda
    v bitvě vyhrála početně slabší armáda
    """
    if len(radek[17]) > 0 and len(radek[18]):
        attacker_size = float(radek[17])
        defender_size = float(radek[18])
        # Pokud byl útočník početně slabší a vyhrál, uložím si název bitvy
        if attacker_size < defender_size and radek[13] == "win":
            mensi_armada_vyhrala.append(radek[0])
        # Pokud byl útočník početně silnější a prohrál, uložím si název bitvy
        if attacker_size > defender_size and radek[13] == "loss":
            mensi_armada_vyhrala.append(radek[0])
print(utocnici)
print(mensi_armada_vyhrala)


utocnici = {}
for radek in radky:
    # Alternativní řešení - využijeme vnořený cyklus
    for utocnik in radek[5:9]:
        if utocnik != "":
            if utocnik in utocnici:
                utocnici[utocnik] = utocnici[utocnik] + 1
            else:
                utocnici[utocnik] = 1
print(utocnici)
```
