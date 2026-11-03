# Q008: Flexible Functions with *args, **kwargs & Lambdas
# Problem: Build a dynamic KPI aggregator that accepts arbitrary sales figures and tags.

def compute_sales_metrics(*revenues, **metadata):
    total = sum(revenues)
    avg = total / len(revenues) if revenues else 0
    return {
        "region": metadata.get("region", "Global"),
        "currency": metadata.get("currency", "USD"),
        "total_revenue": total,
        "average_ticket": round(avg, 2)
    }

# Lambda sort demonstration: sort orders by profit descending
orders = [("Ord_1", 200, 45), ("Ord_2", 500, 120), ("Ord_3", 150, 80)]
orders_sorted_by_profit = sorted(orders, key=lambda x: x[2], reverse=True)

print("KPI Aggregator Result:", compute_sales_metrics(1200, 3400, 5600, region="APAC", currency="INR"))
print("Orders Sorted by Profit:", orders_sorted_by_profit)
