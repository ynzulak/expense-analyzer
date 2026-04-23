
# changing keys name to be more open to other banks

def normalize(data):

    PEKAO = {
        "date": "Data księgowania",
        "amount": "Kwota operacji",
        "category": "Kategoria"
    }

    mapping = PEKAO
    new_list = []
    for k in data:
        date = k.get(mapping["date"])
        amount = k.get(mapping["amount"])
        category = k.get(mapping["category"])

        k = {"Date": date, "Amount": amount, "Category": category}
        new_list.append(k)

    return new_list


  