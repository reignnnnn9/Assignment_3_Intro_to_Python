#Pet Age Calculator

type = input("Enter pet type (dog/cat/bird/hamster): ").capitalize()
age = (input("Enter your pet's age in human years: "))
if type == "dog":
    if age <= 2:
        pet_age = age * 12
    else:
        pet_age = 24 + (age - 2) * 4
elif type == "cat":
    if age <= 2:
        pet_age = age * 12
    else:
        pet_age = 24 + (age - 2) * 4
elif type == "bird":
    pet_age = age * 9
elif type == "hamster":
    pet_age = age * 25
print("\n")

print("=== PET AGE CONVERSTION ===")
print(f"Pet type: {type}")
print(f"Human Age: {age} years")
print(f"Pet Age: {pet_age} pet years") #can't figure out how to use the pet_age inside if statement in here.
print("\n")

print(f"Fun fact: your {type} is like a {pet_age}-year-old human!")