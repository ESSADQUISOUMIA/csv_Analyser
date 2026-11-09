

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