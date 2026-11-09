from src.reader import load_transactions


def main():
    transactions = load_transactions("data/raw/sales.csv")

    print(f"Nombre de transactions : {len(transactions)}")
    print("3 premières lignes :")
    for t in transactions[:3]:
        print(t)

    # Observation demandée par l'indice 3 : le type des valeurs
    print(type(transactions[0]["quantity"]))   # <class 'str'>


if __name__ == "__main__":
    main()