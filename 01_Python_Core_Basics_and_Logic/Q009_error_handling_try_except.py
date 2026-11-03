# Q009: Robust Error Handling in Data Pipelines
# Problem: Parse a dirty list of transaction amounts, skip corrupted records, and log errors.

raw_stream = ["1500", "2300.50", "CORRUPTED_VALUE", "890", None, "4500"]
valid_amounts = []
skipped_count = 0

for val in raw_stream:
    try:
        clean_val = float(val)
        valid_amounts.append(clean_val)
    except (ValueError, TypeError):
        skipped_count += 1
        continue

print(f"Processed {len(valid_amounts)} valid transactions: {valid_amounts}")
print(f"Skipped {skipped_count} corrupted records safely.")
