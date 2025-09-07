
# from book_generator import EBook, Book


# book = Book(title="Runner", author="James", genre="Fiction")

# print(book.describe_book())


# ebook = EBook(title="New Way", author="Huyen", genre="Fiction", format_="ebook", filesize=10)
# print(ebook.describe_book())


# class Vehicle:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year

#     def __str__(self):
#         return f"{self.year} {self.name}"


# class Car(Vehicle):
#     def __init__(self, name, year, mileage):
#         super().__init__(name, year)
#         self.mileage = mileage

#     def __str__(self):
#         return f"{super().__str__} with {self.mileage} miles"
    


# print(issubclass(Vehicle,object))
# print(issubclass(Car, object))

# print(Vehicle.__bases__)

# print(Car.__bases__)


# print('=========================')

# from random import randint
# from random import choice

# items = ['apple', 'banana', 'mangoes']

# def rand_fruit(fruits):
#     if not fruits:
#         return "The fruit list is empty"
#     return choice(fruits)

# print(randint(a=2, b=9))

# fruit = rand_fruit(items)
# print(fruit)

# print("=======================")
# from datetime import datetime, timedelta
# now = datetime.now()
# print(f"Current date and time is {now}")

# future_date = now + timedelta(days=10)
# print(f"Data 10 days from  now: {future_date}")
# formatted_date = now.strftime("%d/%m/%Y, %H:%M:%S")
# print(formatted_date)


from pathlib import Path

# p = Path(".")

# path = Path('./python_basics/example.txt')
# if path.exists():
#     contents = path.read_text()
#     print(contents)
# else:
#     print("File doesn't exist")

# st = path.name
# print(st)

# content = "Paulo is writing code.\n"
# content += "And you like to write Python code as well.\n"
# content +="It's a lovely thing.\n"


# # Create a Path object and open the file in write mode
# with Path('example.txt').open('w') as file:
#     contents =  file.write("This is an example text.")  
#     print(contents)

# from pathlib import Path

# with Path.open("example.txt", "w") as file:
#     contents = file.write("This is all new to me!!")

#     print(contents)

# Exceptions


# try:
#     print(12/2)
# except ZeroDivisionError as e:
#     print(f"Error ocurred: {e}")
# else:
#     print("All is well here")
# finally:
#     print("Always go to this")


# from pathlib import Path

# path = Path('example.txt')

# try:
#     content = path.read_text()
#     print(content)
    
# except FileNotFoundError as e:
#     print(f"File not found: {e}")


# names = ["Paulo","James"]

# try:
#     print(names[9])
# except IndexError as e:
#     print(f"Index error : {e}")


# class MyCustomError(Exception):
#     pass

# class ValueTooSmallError(MyCustomError):
#     pass

# class ValueTooLargeError(MyCustomError):
#     pass

# def check_value(number):
#     if number < 5:
#         raise ValueTooSmallError(f"The number {number} is too small.")

#     elif number > 15:
#         raise ValueTooLargeError(f"This number {number}  is too large.")
#     else:
#         print(f"The number {number} is betweeen allowed range")


# try:
#     user_input = int(input("Enter a number: "))
#     check_value(user_input)
# except ValueTooSmallError as e:
#     print(e)

# except ValueTooLargeError as e:
#     print(e)

# import json
# from pathlib import Path
# names = ["James", "Ruth", "Mary"]
             
# names_json = json.dumps(names)

# print(names)
# print("\n")
# print(names_json)

# with Path.open('names.json','w') as file:
#     contents = json.dumps(names)
#     file.write(contents)

# with Path.open("names.json",'r') as file:
#     contents = json.load(file)
#     print(contents)  

import json
from pathlib import Path

def save_to_json(data, filename="countries.json"):
    """Save the list of countries to a JSON file"""
    with Path.open(filename, 'w') as f:
        json.dump(data, f)

def read_from_json(filename="countries.json"):
    with Path.open(filename, 'r') as f:
        return json.load(f)
    

def main():
    countries = []
    print("Enter country name. Type 'quit' to finish")

    while True:
        country = input("Country: ")
        if country.lower() == 'quit':
            break
        countries.append(country)

        #Save the list of countries to a JSON file
        save_to_json(countries)
        # Read the contents from the JSON file and display

        saved_countries = read_from_json()
        print("\nYou've added the following countries:")
        for country in saved_countries:
            print(country)

if __name__ == "__main__":
    main()