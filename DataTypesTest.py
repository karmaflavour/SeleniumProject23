import random

x = "Aidan"

print(type(x))
print(isinstance(x, str))

dict = {'key1': 'geeks', 'key2': 'for'}
print("Current Dict is: ", dict)


def randomNumberGenerator(start, end):
    randomResult = random.randrange(start, end, 10)
    return randomResult


g = randomNumberGenerator(0, 100)
print(g)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()

testString = "Separating the integer and decimal from the input number."

stringSplit = testString.split(' ')

print(testString)

for x in stringSplit:
    print(x)

d1 = {
    "Name": ["Aidan", "Johnny", "Depp"],
    "Age": 30

}

d2 = {

    "location": "Germany",
    "fruits:": {
        "Name": ["Apple", "Banana", "Orange"], "Price": 100}
}

print("--------")

print(d1)

print("--------")

for c in d1.items():
    print(c)

print("--------")

d2 = {

    "location": "Germany",
    "fruits": {
        "Name": ["Apple", "Banana", "Orange"], "Price": 100}
}

# print(d2["fruits"]["Name"][1])

print(d2.get("fruits").get("Name"))
