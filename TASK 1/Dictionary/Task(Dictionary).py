#1st Sub Task
num_friends = int(input("How many friends do you have? "))

friends = []
for i in range(num_friends):
    name = input(f"Enter name of friend {i+1}: ")
    friends.append(name)

friends_with_length = [(name, len(name)) for name in friends]
print("Friends with name lengths:", friends_with_length)

print()  
#2nd Sub Task
your_expenses = {
    "Flight": 15000,
    "Hotel": 12000,
    "Food": 5000,
    "Shopping": 75000,
    "Activities": 6000
}

partner_expenses = {
    "Flight": 14500,
    "Hotel": 11000,
    "Food": 5500,
    "Shopping": 91000,
    "Activities": 5000
}

# Calculate totals
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("Your total expenses:", your_total)
print("Partner's total expenses:", partner_total)

# Who spent more
if your_total > partner_total:
    print("You spent more.")
elif partner_total > your_total:
    print("Your partner spent more.")
else:
    print("You both spent the same.")

# Biggest spending difference
max_diff_category = None
max_diff_amount = 0

for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    if diff > max_diff_amount:
        max_diff_amount = diff
        max_diff_category = category

print(f"Biggest spending difference is in '{max_diff_category}' with {max_diff_amount} units.")