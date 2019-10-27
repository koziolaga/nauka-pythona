import pprint


def main():
    koszyk = [
                    {"nazwa": "ziemniaki","cena": 5, "VAT": 23, "unit": "kg"},
                    {"nazwa": "jajka","cena": 1, "VAT": 23, "unit": "szt"},
                    {"nazwa": "marchew","cena": 4, "VAT": 23, "unit": "kg"},
                    {"nazwa": "pietruszka","cena": 20, "VAT": 23, "unit": "kg"},
                    {"nazwa": "seler","cena": 9, "VAT": 23, "unit": "kg"}]


    #pprint.pprint(lista_zakupow)
    f = open("koszyk.csv", "w")
    for poz in koszyk:
        for pole in ['nazwa', 'cena', 'VAT', 'unit']:
            f.write("{0},".format(poz[pole]))
        f.write('\n')
    f.close()

    koszyk2 = []
    print("koszyk2")

    f2 = open("koszyk.csv", "r")
    calosc = f2.read()
    linie = calosc.split('\n')
    for l in linie:
        if len(l) > 0:
            print(l)

if __name__ == "__main__":
    main()
# f = open('koszyk.csv')
