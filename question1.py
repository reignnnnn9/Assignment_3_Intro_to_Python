#Movie Ticket Pricing

name = input("Enter your name: ")
age = int(input("Enter your age: "))
quantity = int(input("How many tickets do you want? "))
print("\n")

print("=== MOVIE TICKET RECEIPT ===")
print(f"Customer: {name}")
#print(f"Ticket Type: {ticket_type}") - was not sure if I needed to use this or what I did was correct
if age < 13:
    print("Ticket Type: Child ($8.00 each)")
    ticket_cost = 8
elif age >= 13 and age < 64:
    print("Ticket Type: Adult ($12.00 each)") 
    ticket_cost = 12
else:
    print("Ticket Type: Senior ($9.00 each)")
    ticket_cost = 9
print(f"Quantity: {quantity}")
print(f"Total Cost: ${ticket_cost * quantity}")
print("Thank you for you purchase!")