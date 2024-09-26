def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Kilograms to Pounds')
    print('4. Pounds to Kilograms')

def km_miles():
    km = float(input("Please enter distance in kilometers: "))
    miles = km/1.609
    print("Distance in miles: {0}".format(miles))

def miles_km():
    miles = float(input("Please enter distance in miles: "))
    km = miles*1.609
    print("Distance in kilometers: {0}".format(km))

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
        kg_lb()
    if choice == '4':
        lb_kg()