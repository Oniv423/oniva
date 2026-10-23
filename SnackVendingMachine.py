def calculate_change(paid, price):
    change = paid-price
    return change
snack_price = 25
print("======SNACK VENDING MACHINE======")
print(f"this snack costs {snack_price}unit")
total_inserted = 0
coin_inserted  = 0
while True:
    coin = int(input("Insert a coin (5, 10, 15, 20 or 25)"))
    if coin != 5 and coin != 10 and coin != 15 and coin != 20 and coin != 25:
        print("Invalid coin, try again\n")
        continue
    total_inserted += coin
    coin_inserted += 1
    print(f"Inserted{coin}. Total so far: {total_inserted}\n")
    if total_inserted >= snack_price:
        print("Enough money inserted!")
        break
    change_due = calculate_change(total_inserted, snack_price)
    print("dispencing your snack...")
    if change_due == 0:
        pass
    else:
        print(f"Here is your change:{change_due}units")
        print("\n===== PURCHASE SUMMARY =====")
        print("Snack Price:", snack_price)
        print("Coins Inserted:", coin_inserted)
        print("Total Paid:", total_inserted)
        print("Change Given:", change_due)
        print("=============================")
        print("Thanks for your purchase!")