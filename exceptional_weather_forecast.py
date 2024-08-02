
def main():
    try:
        temperature_F = int(input("Please enter a temperature in Farenheit:"))
        temperature_C = (temperature_F - 32) * 5/9
    except:
        print("Please Enter a number!")
    else:
        print(f'{temperature_F} degrees farenheit is {temperature_C} in celsius!')
    finally:
        print('Thank you for using the weather app! Have  a great rest of your day')
    
main()