import csv

transactions = []
def load_transactions(file_path):

    with open(file_path, mode='r',newline='', encoding='utf-8') as f :
        reader = csv.DictReader(f)
        for row in reader:
            transactions.append(row)
    return transactions
        