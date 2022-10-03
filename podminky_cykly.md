# 1

```py
import sys

spravne_heslo = "Czechitas"
if sys.argv[2] == spravne_heslo:
    print("Přístup povolen")
else:
    print("Přístup odepřen")
```

Příklady spuštění programu:

```
python program.py test test
python program.py test Czechitas
```

# 2

```py
import sys

kurz_koruna = 25.03
kurz_euro = 1.02

castka = int(sys.argv[2])

if sys.argv[1] == "czk":
    print(castka / kurz_koruna)
elif sys.argv[1] == "eur":
    print(castka / kurz_euro)
# Další měny by šly přidat stejným způsobem
```

# 3

```py
with open("zustatky.txt", encoding="utf-8") as soubor:
    zustatky = soubor.readlines()

cislo_radku = 1
for radek in zustatky:
    zustatek = float(radek) * 1.025
    if zustatek > 0:
        print(cislo_radku, zustatek)
    cislo_radku += 1
```

# 4

```py
# Příklad vstupního seznamu
seznam = [1, 2, 3, 4, 9]

# Funkce range je vysvětlená v povinných úložkách k lekci První programy
for i in range(1, len(seznam)):
    if seznam[i-1] >= seznam[i]:
        print("Seznam není seřazen vzestupně.")
        exit()
print("Seznam je seřazen vzestupně.")
```

# 5
