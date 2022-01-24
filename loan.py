# Get the loan details
money_owed = float(input("How much money do you owe, in dollars?\n")) # 50000
apr = float(input("What is the annual percentage rate?\n")) # 3
payment = float(input("What will your monthly payment be, in dollars?\n")) # $1000
months = int(input("How many months do you want to see results for?\n")) # 24

monthly_rate = apr/100/12

interest_paid = money_owed * monthly_rate
money_owed = money_owed + interest_paid
money_owed = money_owed - payment

print("Paid", payment, "of which", interest_paid, "was interest,", end=' ')
print("Now I owed", money_owed)