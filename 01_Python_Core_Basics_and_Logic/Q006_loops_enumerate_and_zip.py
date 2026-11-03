# Q006: Enumerate & Zip in Parallel Data Streams
# Problem: Match product names with their unit prices and rank them with row numbers.

products = ["Activa 6G", "Shine 125", "SP 125", "Hornet 2.0"]
prices = [82000, 85000, 91000, 139000]

print("Product Price Register:")
for idx, (prod, price) in enumerate(zip(products, prices), start=1):
    print(f"Rank {idx}: {prod} -> INR {price:,}")
