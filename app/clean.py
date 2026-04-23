
# cleaning strings, changing to float etc.

def clean(transactions):
    for k in transactions:
        k["Kwota operacji"] = float(k["Kwota operacji"].replace(" ", "").replace(",", "."))
        to_remove = ["Data waluty", "Nadawca / Odbiorca", "Adres nadawcy / odbiorcy", "Rachunek źródłowy", "Rachunek docelowy", "Tytułem", "Waluta", "Numer referencyjny", "Typ operacji",]
        for r in to_remove:
            k.pop(r)

    return transactions