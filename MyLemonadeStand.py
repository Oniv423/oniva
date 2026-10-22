def greet_customer():
    print("Welcome to my Lemonade Stand!")
    print("Fresh lemonade made just for you.")
greet_customer()
price_per_cup = float(input("Enter the price per cup in dollars: "))
cups_sold = int(input("Enter the number of cups sold: "))
def calclate_total(price, cups):
    total = price * cups
    return total
def calculat_change(paid, total):
    change = paid - total
    return change
change_due = calculat_change(amount_paid, calculate_total)
rounded_change = round(change_due, 2)
total_cost = calculate_total(price_per_cup, cups_sold)
rounded_total = round(total_cost, 2)
print("Total Cost:", rounded_total)