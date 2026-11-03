# Q002: String Cleaning, Splitting and Formatting
# Problem: Clean inconsistent branch and invoice strings extracted from raw telemetry.

raw_record = "  DEL-NCR_DL_NORTH_INV-98234  "

# Strip and extract parts
cleaned = raw_record.strip()
parts = cleaned.split("_")
city = parts[0]
state = parts[1]
zone = parts[2]
invoice = parts[3]

formatted_summary = f"Invoice: {invoice} | Location: {city} ({zone} Zone, {state})"
print(formatted_summary)
