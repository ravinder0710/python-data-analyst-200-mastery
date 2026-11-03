# Q001: Data Types, Typecasting & Floating Precision Trap
# Problem: Clean an e-commerce price string, convert to float, and handle IEEE 754 precision issues.

raw_price = " $1,299.95 "
tax_rate = "0.08"

# 1. Cleaning & Typecasting
clean_price = float(raw_price.replace("$", "").replace(",", "").strip())
tax = float(tax_rate)
total = clean_price * (1 + tax)

# 2. Precision handling
print(f"Clean Price: {clean_price:.2f}")
print(f"Total with Tax: {total:.2f}")
print("Precision trap check (0.1 + 0.2 == 0.3):", (0.1 + 0.2) == 0.3)
print("Safe equality check using round():", round(0.1 + 0.2, 2) == 0.3)
