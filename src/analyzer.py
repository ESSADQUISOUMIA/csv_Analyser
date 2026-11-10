def calculate_total_revenue(valid_transactions):
    total_revenue = 0
    for transaction in valid_transactions:
        total_revenue += (int(transaction["quantity"]) * float(transaction["unit_price"]))
    return total_revenue

def count_transactions(valid_transactions):
    return len(valid_transactions)

def count_unique_customers(valid_transactions):
    unique_customers = set()
    # Parcourir les transactions
    for transaction in valid_transactions:
        #  Récupérer customer_id
        customer_id = transaction["customer_id"]
        #Ajouter chaque identifiant au set
        unique_customers.add(customer_id)
    # Retourner le nombre de clients uniques
    return len(unique_customers)

def calculate_average_basket(valid_transactions):
    #  Utiliser calculate_total_revenue()
    total_revenue = calculate_total_revenue(valid_transactions)

    #  Utiliser count_transactions()
    num_transactions = count_transactions(valid_transactions)

    #  Calculer le panier moyen
    if num_transactions > 0:
        average_basket = total_revenue / num_transactions
    else:
        average_basket = 0

    return average_basket

def revenue_by_product(valid_transactions):
    product_revenue = {}

    for transaction in valid_transactions:
        product = transaction["product"]

        quantity = int(transaction["quantity"])
        unit_price = float(transaction["unit_price"])

        revenue = quantity * unit_price

        if product in product_revenue:
            product_revenue[product] += revenue
        else:
            product_revenue[product] = revenue

    return product_revenue

def top_products(product_revenue):
    sorted_products = sorted(product_revenue.items(), key=lambda x: x[1], reverse=True)
    top_3_products = sorted_products[:3]

    return top_3_products

def revenue_by_category(valid_transactions):
    category_revenue = {}

    for transaction in valid_transactions:
        category = transaction["category"]
        revenue = int(transaction["quantity"]) * float(transaction["unit_price"])
        if category in category_revenue:
            category_revenue[category] += revenue
        else:
            category_revenue[category] = revenue

    return category_revenue
