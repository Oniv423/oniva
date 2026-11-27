basket1 = {"apple","banana","mango","apple","grape"}
basket2 = {"mango","kiwi","banana","kiwi"}
print("Basket 1: ", basket1)
print("Basket 2: ", basket2)
basket1.add("orange")
print("Basket 1 after adding an orange: ", basket1)
common_fruits = basket1.intersection(basket2)
print("Fruits in both baskets: ", common_fruits)
import array as arr
fruit_count = arr.array ('i', [3,5,2,4])
print("Fruit count array: ",fruit_count)
fruit_count.insert(0, 1)
fruit_count.append(6)
print("Fruit count after adding items:", fruit_count)