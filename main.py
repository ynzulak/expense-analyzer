from app.loader import loader
from app.clean import clean
from app.normalize import normalize
from app.analyzer import analyzer

def main():
    path = "data/operations.csv"
    data = loader(path)
    data = clean(data)
    data = normalize(data)
    data = analyzer(data)
    # print("=================")
    # print(data)



if __name__ == "__main__":
    main()