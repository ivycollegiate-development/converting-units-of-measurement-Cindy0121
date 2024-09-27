def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Celsius to fahrenheit')
    print('4. fahrenheit to celsius')
    print('5. Kilograms to Pounds')
    print('6. Pounds to Kilograms')

def km_miles():
    km = float(input("Please enter distance in kilometers: "))
    miles = km/1.609
    print("Distance in miles: {0}".format(miles))

def miles_km():
    miles = float(input("Please enter distance in miles: "))
    km = miles*1.609
    print("Distance in kilometers: {0}".format(km))

def celsius_fahrenheit():
    celsius = float(input("Please enter the temperature in celsius: "))
    fahrenheit = celsius*9/5+32
    print("Temperature in fahrenheit: {0}".format(fahrenheit))

def fahrenheit_celsius():
    fahrenheit = float(input("Please enter the temperature in fahrenheit: "))
    celsius = (fahrenheit-32)*5/9
    print("Temperature in celsius: {0}".format(celsius))

def kg_lb():
    kg = float(input("Please enter weight in kilograms: "))
    pounds = kg/2.20462262
    print("Weight in pounds: {0}".format(pounds))

def lb_kg():
    pounds = float(input("Please enter weight in pounds: "))
    kg = pounds*2.20462262
    print("weight in kilograms: {0}".format(kg))

if __name__ == '__main__':
    print_menu()
    choice = input("Which conversion would you like to do today?: ")
    if choice == '1':
        km_miles()
    if choice == '2':
        miles_km()
    if choice == '3':
        celsius_fahrenheit()
    if choice == '4':
        fahrenheit_celsius()
    if choice == '5':
        kg_lb()
    if choice == '6':
        lb_kg()