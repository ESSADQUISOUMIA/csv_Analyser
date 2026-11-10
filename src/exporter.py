from src.analyzer import calculate_average_basket, calculate_total_revenue, count_transactions, count_unique_customers, revenue_by_category
import json


def build_summary(valid_transactions):
    summary = {}

    summary["total_revenue"] = calculate_total_revenue(valid_transactions)
    summary["total_transactions"] = count_transactions(valid_transactions)
    summary["unique_customers"] = count_unique_customers(valid_transactions)
    summary["average_basket"] = calculate_average_basket(valid_transactions)
    summary["revenue_by_category"] = revenue_by_category(valid_transactions)

    return summary


def save_summary(summary, file_path):

    with open(file_path, mode='w', encoding='utf-8') as f:   
     json.dump(summary, f, indent=4)
