#Pet Age Calculator

type = input("Enter pet type (dog/cat/bird/hamster): ").capitalize() #after this the type need to be capitalized
age = int(input("Enter your pet's age in human years: "))
pet_age = 0
if type == "Dog":
    if age <= 2:
        pet_age = age * 12
    else:
        pet_age = 24 + (age - 2) * 4
elif type == "Cat":
    if age <= 2:
        pet_age = age * 12
    else:
        pet_age = 24 + (age - 2) * 4
elif type == "Bird":
    pet_age = age * 9
elif type == "Hamster":
    pet_age = age * 25
print("\n")

print("=== PET AGE CONVERSTION ===")
print(f"Pet type: {type}")
print(f"Human Age: {age} years")
print(f"Pet Age: {pet_age} pet years") 
print("\n")

print(f"Fun fact: your {type} is like a {pet_age}-year-old human!")