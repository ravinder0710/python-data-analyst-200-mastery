# Q005: Dictionary Frequency Counter & Safe Lookup
# Problem: Count transaction frequency by category and query safely with default values.

transactions = ["Grocery", "Electronics", "Grocery", "Clothing", "Grocery", "Electronics"]

# Frequency counter without Counter library
freq_map = {}
for item in transactions:
    freq_map[item] = freq_map.get(item, 0) + 1

# Safe lookup for non-existent category
automotive_count = freq_map.get("Automotive", 0)

print("Category Frequency Map:", freq_map)
print("Automotive Category Count:", automotive_count)
