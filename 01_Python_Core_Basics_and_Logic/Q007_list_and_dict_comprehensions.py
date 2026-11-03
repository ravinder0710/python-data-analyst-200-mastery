# Q007: List & Dictionary Comprehensions
# Problem: Filter high-margin transactions and create price tier maps in a single line.

sales = [450, 1200, 890, 2300, 150, 3100, 750]

# High ticket (> 1000) with 10% holiday tax applied
high_ticket_with_tax = [round(s * 1.10, 2) for s in sales if s > 1000]

# Dict comprehension: Categorize sales IDs into tiers
sales_tiers = {f"TXN_{i+1}": ("Premium" if s >= 1000 else "Standard") for i, s in enumerate(sales)}

print("High Ticket Transactions with Tax:", high_ticket_with_tax)
print("Sales Tiers:", sales_tiers)
