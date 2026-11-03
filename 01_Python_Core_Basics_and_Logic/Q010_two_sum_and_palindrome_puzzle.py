# Q010: Classic Interview Coding Puzzles (Two Sum & Palindrome)
# Problem 1: Find two transactions that sum up to target budget.
# Problem 2: Check if transaction reference code is a palindrome.

def two_sum_budget(prices, target):
    seen = {}
    for idx, price in enumerate(prices):
        diff = target - price
        if diff in seen:
            return (seen[diff], idx)
        seen[price] = idx
    return None

def is_palindrome_ref(ref_code):
    clean = "".join(ch.lower() for ch in ref_code if ch.isalnum())
    return clean == clean[::-1]

print("Two Sum Indices for Target 500:", two_sum_budget([120, 200, 380, 150], 500)) # 120 + 380 = 500 -> (0, 2)
print("Palindrome Check ('RADAR'):", is_palindrome_ref("RADAR"))
print("Palindrome Check ('TXN-101-NXT'):", is_palindrome_ref("TXN-101-NXT"))
