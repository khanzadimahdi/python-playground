age = 20
price = 19.95
first_name = "Mahdi"
is_online = True


last_name = 'khanzadi'

print(age, price, first_name, is_online)

name = input("what is your name? ")
birth_year = input("Enter your birth year: ")

count_life_days = 365 * (2021 - int(birth_year))

print("Hello " + name)
print("count life days " + str(count_life_days))
