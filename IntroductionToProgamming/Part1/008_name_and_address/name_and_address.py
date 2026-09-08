# Please write a program which asks for the user's name and address. The program should also print out the given information, as follows:

# Sample output
# Given name: Steve
# Family name: Sanders
# Street address: 91 Station Road
# City and postal code: London EC05 6AW

# Steve Sanders
# 91 Station Road
# London EC05 6AW

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
address = input("What is your address? ")
city_and_postal_code = input("What is your city and postal code? ")

print(first_name + " " + last_name)
print(address)
print(city_and_postal_code)
