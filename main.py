from src.reader import load_transactions
from src.validator import clean_transactions
from src.exporter import build_summary, save_summary

def main():
    transactions = load_transactions("data/raw/sales.csv")
    valid_transactions, invalid_transactions = clean_transactions(transactions)

    summary = build_summary(valid_transactions)

    save_summary(summary, "reports/summary.json")

    print(f"Nombre de transactions valides : {len(valid_transactions)}")
    print(f"Nombre de transactions invalides : {len(invalid_transactions)}")

if __name__ == "__main__":
    main()
