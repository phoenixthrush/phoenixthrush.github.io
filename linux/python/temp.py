# Made by an Asian - Phoenixthrush

def get_temperature():
    while True:
        c = input("Please enter ur Temperature: ")
        try:
            c = float(c)
            return c
        except ValueError:
            print("That is not a Temperature!")

def convert_celsius_to_kelvin(c):
    k = c + 273,15
    return k

def convert_celsius_to_fahrenheit(c):
    f = ((c * 9) / 5) + 32
    return f

def convert_kelvin_to_celsius(c):
    c = c - 273,15
    return c

def convert_fahrenheit_to_celsius(c):
    c = c / 9 * 5 - 32
    return c

def convert_kelvin_to_fahrenheit(c):
    f = c - 273,15
    f = f * 0,556 + 32
    return f

def convert_fahrenheit_to_kelvin(c):
    f = c - 32
    f = f * 0,556 + 273,15
    return f

def celsius_to_kelvin():
    c = get_temperature()
    print()
    print("It would be " + str(convert_celsius_to_kelvin(c)) + " in Kelvin")

def celsius_to_fahrenheit():
    c = get_temperature()
    print()
    print("It would be " + str(convert_celsius_to_fahrenheit(c)) + " in Fahrenheit")

def kelvin_to_celsius():
    c = get_temperature()
    print()
    print("It would be " + str(convert_kelvin_to_celsius(c)) + " in Celsius")

def kelvin_to_fahrenheit():
    c = get_temperature()
    print()
    print("It would be " + str(convert_kelvin_to_fahrenheit(c)) + " in Fahrenheit")

def fahrenheit_to_celsius():
    c = get_temperature()
    print()
    print("It would be " + str(convert_fahrenheit_to_celsius(c)) + " in Celsius")

def fahrenheit_to_kelvin():
    c = get_temperature()
    print()
    print("It would be " + str(convert_fahrenheit_to_kelvin(c)) + " in Kelvin")

def menue():

    print()
    print("1 -- Celsius to Kelvin!")
    print("2 -- Celsius to Fahrenheit")
    print("3 -- Kelvin to Celsius")
    print("4 -- Kelvin to Fahrenheit        [broke]")
    print("5 -- Fahrenheit to Celsius       [broke]")
    print("6 -- Fahrenheit to Kelvin        [broke]")

    print()

    while True:
        x = input("Please enter an option!: ")
        try:
            x = float(x)

            if x == 1:
                celsius_to_kelvin()
                break
            elif x == 2:
                celsius_to_fahrenheit()
                break
            elif x == 3:
                kelvin_to_celsius()
                break
            elif x == 4:
                kelvin_to_fahrenheit()
                break
            elif x == 5:
                fahrenheit_to_celsius()
                break
            elif x == 6:
                fahrenheit_to_kelvin()
                break
            else:
                menue()
                break

        except ValueError:
            print("That is not a number!")

if __name__ == "__main__":
    menue()
