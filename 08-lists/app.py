names = ["Mahdi", "John", "Sam", "Bob"]

names[0] = "Ehsan"

print(names[0]) # first element
print(names[-1]) # first element from end of the list

print(names[0:3]) # slice of list
print(names)


names.append("Ali")
print(names)

names.insert(0, "Mamad")
print(names)

print("Ali" in names)
names.remove("Ali")
print(names)
print("Ali" in names)

names.clear()
print(names)

print(len(names))

numbers = [1, 2, 3, 4, 5]

for item in numbers:
    print(item)

i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1

numbers = range(5) # 0 to 5
print(numbers)

for number in numbers:
    print(number)
    
numbers = range(5, 10) # 5 to 9
print(numbers)

for number in numbers:
    print(number)

numbers = range(5, 10) # 5 to 10 step 2 ==> 5 7 9
print(numbers)

for number in numbers:
    print(number)
