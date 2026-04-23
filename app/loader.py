import pandas as pd

# loading csv file

def loader (path):
    csv_file = pd.read_csv(path, sep=None, engine="python").head(20)
    transactions = csv_file.to_dict("records")
    return transactions
    