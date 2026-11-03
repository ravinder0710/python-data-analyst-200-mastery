# Q004: Sets & Uniqueness in Customer Cohorts
# Problem: Find customers who transacted in Month 1 AND Month 2 (retained), and who left (churned).

month_1_cust = {"C101", "C102", "C103", "C104", "C105"}
month_2_cust = {"C103", "C104", "C105", "C106", "C107"}

retained = month_1_cust.intersection(month_2_cust)
churned = month_1_cust.difference(month_2_cust)
new_acquisitions = month_2_cust.difference(month_1_cust)

print("Retained Customers:", retained)
print("Churned Customers:", churned)
print("New Customers:", new_acquisitions)
