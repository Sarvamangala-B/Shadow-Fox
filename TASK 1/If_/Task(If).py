#1st Sub Task
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)

if bmi >= 30:
    print("Obesity")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal")
else:
    print("Underweight")

print()

#2nd Sub Task
australia = ["sydney", "melbourne", "brisbane", "perth"]
uae = ["dubai", "abu dhabi", "sharjah", "ajman"]
india = ["mumbai", "bangalore", "chennai", "delhi"]

city = input("Enter a city name: ").strip().lower()

if city in australia:
    print(f"{city.title()} is in Australia")
elif city in uae:
    print(f"{city.title()} is in UAE")
elif city in india:
    print(f"{city.title()} is in India")
else:
    print(f"{city.title()} is not in the given country list")

print()

#3rd Sub Task 

city1 = input("Enter the first city: ").strip().lower()
city2 = input("Enter the second city: ").strip().lower()

if city1 in australia and city2 in australia:
    print("Both cities are in Australia")
elif city1 in uae and city2 in uae:
    print("Both cities are in UAE")
elif city1 in india and city2 in india:
    print("Both cities are in India")
else:
    print("They don't belong to the same country")