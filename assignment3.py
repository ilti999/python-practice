# Task 1

cafe_info = ("Brew & Bite", "Astana, Mangilik El 1", "Good food, great vibes")

print("=" * 30)
print(cafe_info[0])
print(cafe_info[1])
print(cafe_info[2])
print("=" * 30)

# Task 2

items = []
prices = []

while True:
    item = input("Enter item name (or 'done' to finish): ")

    if item.lower() == "done":
        break

    price = float(input("Enter price: "))

    items.append(item)
    prices.append(price)

print("-" * 30)
print(f"Your order ({len(items)} items):")
print("-" * 30)

for i in range(len(items)):
    print(f"{items[i]} {prices[i]} KZT")

print("-" * 30)

# Task 3

unique_drinks = set()

while True:
    drink = input("Enter drink name (or 'done' to finish): ")

    if drink.lower() == "done":
        break

    unique_drinks.add(drink)

print(f"Unique drinks today: {len(unique_drinks)}")
print(unique_drinks)

# Task 4

customer = input("Enter customer name: ")
hour = int(input("Enter current hour (0-23): "))

subtotal = sum(prices)

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
    print("Cafe is closed")
    exit()

new_total = subtotal - discount
tip = new_total * 0.10
total = new_total + tip

bill = {
    "customer": customer,
    "items": len(items),
    "subtotal": subtotal,
    "discount": discount,
    "tip": tip,
    "total": total
}

print("=" * 30)
print("BILL - Brew & Bite")
print("=" * 30)

print(f"Customer : {bill['customer']}")
print(f"Items : {bill['items']}")

print("-" * 30)

for i in range(len(items)):
    print(f"{items[i]} {prices[i]} KZT")

print("-" * 30)

print(f"Subtotal : {bill['subtotal']} KZT")
print(f"Discount : {bill['discount']} KZT ({discount_label})")
print(f"Tip (10%) : {bill['tip']} KZT")
print(f"Total : {bill['total']} KZT")

print("=" * 30)