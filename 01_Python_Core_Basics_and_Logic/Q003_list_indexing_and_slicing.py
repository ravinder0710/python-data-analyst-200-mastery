# Q003: List Indexing, Negative Slicing and In-Place Sorting
# Problem: Given monthly transaction figures, extract recent quarters, top figures, and sort.

monthly_sales = [120, 145, 130, 160, 180, 210, 195, 230, 250, 240, 280, 310]

# Last quarter (Q4) sales using negative slicing
q4_sales = monthly_sales[-3:]
# Every alternate month
alternate_months = monthly_sales[::2]
# Top 3 sales months without modifying original list
top_3_months = sorted(monthly_sales, reverse=True)[:3]

print("Q4 Sales:", q4_sales)
print("Alternate Months:", alternate_months)
print("Top 3 Sales Months:", top_3_months)
