# -*- coding: utf-8 -*-

# from collections import defaultdict

# students_by_class = defaultdict(list)

# students_by_class["10A"].append("Sahil")
# students_by_class["10A"].append("Rahul")
# students_by_class["10B"].append("Mrinmoy")

# print(students_by_class)
# print(dict(students_by_class))
# print(students_by_class["10C"]) # Accessing a missing key creates it
# print(dict(students_by_class))


#############################################################################


# from collections import defaultdict

# sales = [
#     ("saree", 1200),
#     ("kurti", 700),
#     ("saree", 1500),
#     ("dupatta", 300),
#     ("kurti", 800),
# ]

# total_sales = defaultdict(int)

# for item, amount in sales:
#     total_sales[item] += amount

# print(dict(total_sales))

##############################################################################
# from collections import defaultdict

# trades = [
#     ("NIFTY", 100.5),
#     ("BANKNIFTY", 200.0),
#     ("NIFTY", 50.25),
#     ("RELIANCE", 80.0),
#     ("BANKNIFTY", 25.5),
# ]

# brokerage_by_symbol = defaultdict(float)

# for symbol, brokerage in trades:
#     brokerage_by_symbol[symbol] += brokerage

# print(dict(brokerage_by_symbol))




############################################################################

'''
defaultdict(set)

Use this when you want unique values per key.

'''

# from collections import defaultdict

# records = [
#     ("Sahil", "CS"),
#     ("Sahil", "Math"),
#     ("Rahul", "CS"),
#     ("Sahil", "CS"),
# ]

# subjects_by_student = defaultdict(set)

# for student, subject in records:
#     subjects_by_student[student].add(subject)

# print(dict(subjects_by_student))



########################################################

# from collections import defaultdict

# orders = [
#     ("Priya", "saree"),
#     ("Priya", "kurti"),
#     ("Asha", "saree"),
#     ("Priya", "saree"),
#     ("Asha", "dupatta"),
# ]

# items_by_customer = defaultdict(set)

# for customer, item in orders:
#     items_by_customer[customer].add(item)

# print(dict(items_by_customer))



'''
defaultdict(list)   # group many values
defaultdict(int)    # count / integer totals
defaultdict(float)  # decimal totals
defaultdict(set)    # unique grouped values

'''

##############################################################################


# Mini project: sales report using defaultdict

from collections import defaultdict

sales = [
    ("Priya", "saree", 1200),
    ("Asha", "kurti", 700),
    ("Priya", "dupatta", 300),
    ("Priya", "saree", 1500),
    ("Asha", "saree", 1300),
    ("Rina", "kurti", 800),
]

total_sales_by_customer = defaultdict(int)
items_by_customer = defaultdict(set)


for name, cloth_type, amount in sales:
    total_sales_by_customer[name] += amount
    items_by_customer[name].add(cloth_type)
    
print(dict(total_sales_by_customer))
print(dict(items_by_customer))


##############################################################################






















