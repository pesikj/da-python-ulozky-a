with open("battles.tsv", encoding="utf-8") as soubor:
    radky = soubor.readlines()

radky = [radek.split("\t") for radek in radky]
slabsi_vyhrali = []
for radek in radky[1:]:
    print(radek[13])
    if len(radek[17].strip()) > 0 and len(radek[18].strip()) > 0:
        if float(radek[17]) > float(radek[18]) and radek[13] == "loss":
            slabsi_vyhrali.append(radek[0])
        if float(radek[17]) < float(radek[18]) and radek[13] == "win":
            slabsi_vyhrali.append(radek[0])
print(slabsi_vyhrali)
