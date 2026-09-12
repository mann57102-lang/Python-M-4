# PART 1: Create two fruit baskets as sets
basket_a = {"apple", "orange", "papaya", "apple", "cherry"}
basket_b = {"papaya", "watermelon", "orange", "watermelon"}

print("Basket A:", basket_a)
print("Basket B:", basket_b)


# PART 2: Add a new fruit to basket_a
basket_a.add("pineapple")
print("Basket A after adding pineapple:", basket_a)


# PART 3: Find fruits common to both baskets
shared_fruits = basket_a.intersection(basket_b)
print("Fruits available in both baskets:", shared_fruits)


# PART 4: Create an array of fruit counts using the array module
import array as fruit_array

fruit_quantity = fruit_array.array('i', [2, 6, 4, 7])

print("Fruit quantity array:", fruit_quantity)


# PART 5: Add new fruit counts to the array
fruit_quantity.insert(1, 3)
fruit_quantity.append(8)

print("Fruit quantity after adding values:", fruit_quantity)


# PART 6: Count how many times the number 6 appears in the array
count_of_6 = fruit_quantity.count(6)

print("Number of times 6 appears:", count_of_6)


# PART 7: Reverse the order of the fruit counts array
fruit_quantity.reverse()

print("Reversed fruit quantity array:", fruit_quantity)


# PART 8: Print the final class fruit basket organizer summary
print("")
print("===== FRUIT BASKET SUMMARY =====")
print("Basket A:", basket_a)
print("Basket B:", basket_b)
print("Shared fruits:", shared_fruits)
print("Fruit quantities:", fruit_quantity)
print("================================")
