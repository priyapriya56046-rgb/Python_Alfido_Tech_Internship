#Temperature Converter

print("Welcome to Temperature Converter!")
temp = float(input("Enter temperature: "))
unit = input("Enter unit of the temperature (C, F, K): ").upper()

if unit == 'C':
    fahrenheit = (temp * 9/5) + 32
    kelvin = temp + 273.15
    print(f"{temp}°C = {fahrenheit}°F = {kelvin}K")
elif unit == 'F':
    celsius = (temp - 32) * 5/9
    kelvin = celsius + 273.15
    print(f"{temp}°F = {celsius}°C = {kelvin}K")
elif unit == 'K':
    celsius = temp - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print(f"{temp}K = {celsius}°C = {fahrenheit}°F")
else:
    print("Invalid unit! Please enter C, F, or K.")
