score = int(input("Enter your score: "))
if score >= 50:
    print("You passed")
else:
    print("You failed")

print("-"*30)
day = input("Enter a day of the week: ").lower()
if day == "saturday" or day == "sunday":
    print("Weekend")
else:
    print("Weekday")

print("-"*30)
i=1
while i<=5:
    print(i)
    i+=1

print("-"*30)
word = input("Enter a word: ")
for letter in word:
    print(letter)

print("-"*30)
word=input("Enter a word: ")
print("Uppercase:", word.upper())
print("Lowercase:", word.lower())

# Task D1 Multiple Orders

customer_name = input("Enter customer name: ")

subtotal = 0
item_count = 0

while True:
    item_name = input("Enter item name (or 'done' to finish): ")

    if item_name.lower() == "done":
        break

    price = float(input("Enter price: "))
    subtotal += price
    item_count += 1

print(f"Customer : {customer_name.upper()}")
print(f"Items : {item_count}")
print(f"Subtotal : {subtotal} KZT")


# Task D2 Time-Based Discount

hour = int(input("Enter current hour (0-23): "))

print("-" * 30)

if 6 <= hour < 12:
    discount_label = "Morning discount"
    discount = subtotal * 0.10

elif 12 <= hour < 17:
    discount_label = "No discount"
    discount = 0

elif 17 <= hour < 22:
    discount_label = "Evening discount"
    discount = subtotal * 0.05

else:
    print("Closed")
    exit()

new_total = subtotal - discount
tip = new_total * 0.10
total = new_total + tip

print(f"Time period : {discount_label}")
print(f"Discount : {discount} KZT")
print(f"Tip (10%) : {tip} KZT")
print(f"Total : {total} KZT")

print("-" * 30)


# Task D3 Name Analysis

print(f"Name uppercase : {customer_name.upper()}")
print(f"Name lowercase : {customer_name.lower()}")
print(f"Name length : {len(customer_name)}")

if customer_name[0].upper() == 'A' or customer_name[0].upper() == 'S':
    print("VIP customer")
else:
    print("Regular customer")