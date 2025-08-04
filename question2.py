#Restaurant Order System

print("=== RESTAURANT MENU ===")
print("1. Pizza - $15.99")
print("2. Burger - $12.50")
print("3. Salad - $9.99")
print("4. Pasta - $13.75")
print("\n")

choice = int(input("Enter your choice (1-4): "))
drink = input("Would you like a drink? (+$2.50) (yes/no): ").lower()
print("\n")

print("=== YOUR ORDER ===")
if choice == 1:
    print("Food: Pizza - $15.99")
    price = 15.99
elif choice == 2:
    print("Food: Burger - $12.50")
    price = 12.50
elif choice == 3:
    print("food Salad - $9.99")
    price = 9.99
elif choice == 4:
    print("Food: Pasta - $13.75")
    price = 13.75

if drink == "yes":
    print("Drink: Yes - $2.50")
    dprice = 2.5
if drink == "no":
    print("Drink: No")
    dprice = 0

subtotal = float(price + dprice)
tax = float(subtotal * .08)

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax(8%): ${tax:.2f}")
print(f"Total: ${subtotal + tax:.2f}")