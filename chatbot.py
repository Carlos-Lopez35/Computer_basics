#ask name
name = input("Hi, what is your name? ")
#ask age
while True:
    try:
        birthyear = int(input(f"Nice to meet you {name}, what was your year of birth? "))
        break
    except ValueError:
        print("Por favor, introduce un número válido.")
birthmonth = input("In which month? ").lower()
while True:
    try:
        birthday = int(input("And which day of the month? "))
        break
    except ValueError:
        print("Por favor, introduce un número válido.")
#calculate age
age = 2024 - birthyear
if birthmonth in ["november", "december"]:
    age -= 1
if birthmonth == "october":
    if birthday >= 22:
        age = age  
        age -= 1
#ask hobbies
int(input(f"So you're {age} years old. And what hobbies do you have? "))
#final answer
print(f"Wow, that's amazing, {name}!")