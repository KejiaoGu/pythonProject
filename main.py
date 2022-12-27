persons = [
    {'name': 'John', 'age': 20},
    {'name': 'Paul', 'age': 19},
    {'name': 'Karl', 'age': 22},
    {'name': 'Helen', 'age': 21}
]

print("name\tage")
for person in persons:
    print('%s\t%d' % (person['name'], person['age']))

age = input("Enter an age to find: ") # returns a string
for person in persons:
    if person['age'] == int(age):
        print('%s\t%d' % (person['name'], person['age']))