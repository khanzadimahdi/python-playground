
sample = 'learning Python for new opportunity.'
         #01234567

print(sample.upper()) # doesnt change the string and returns a new string
print(sample)

print(sample.find('Python'))
print(sample.find('python')) # -1


print( 'Python' in sample)
print('python' in sample)

print(sample.replace('for', '4'))
print(sample.replace('For', '4')) # nothing is gonna happen
print(sample.replace('x', '4')) # nothing is gonna happen