

def validate_transaction(transaction):

    try:
        transaction_id=transaction["transaction_id"].strip()
        if transaction_id=="" :
            raise ValueError("L'ID de transaction doit être unique et non vide")
        quantity=int(transaction["quantity"])
        if quantity <= 0:
            raise ValueError("La quantité ne peut pas être négative")
        unit_price=float(transaction["unit_price"])
        if unit_price < 0:
            raise ValueError("Le prix ne peut pas être négatif")
    except (ValueError, TypeError,KeyError) as e:
        print(f"Erreur de validation pour la transaction {transaction}: {e}")
        return False
    return True

def clean_transactions(transactions):
    valid_transactions = []
    invalid_transactions = []
    seen_ids = set()
    for transaction in transactions:
        if validate_transaction(transaction) and transaction["transaction_id"] not in seen_ids:
            valid_transactions.append(transaction)
            seen_ids.add(transaction["transaction_id"])
        else:
            invalid_transactions.append(transaction)
    return valid_transactions, invalid_transactions
