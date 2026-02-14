def fahrenheit_to_celcius(temp):
    return round((temp - 32) * 5 / 9 , 2)
    
def main():
    fahrenheit_list = [32 , 67 , 90 , 102 , 75 , 68 , 55]
    print("Fahrenheit : ",fahrenheit_list)
    
    # Convert temperatures using list comprehension
    celcius_temps_list = [fahrenheit_to_celcius(temp) for temp in fahrenheit_list]
    print("Celsius : " , celcius_temps_list)
    
    
    # Convert temperatures usinggenerator expression
    celcius_temps_gen = [fahrenheit_to_celcius(temp) for temp in fahrenheit_list]
    print("Celsius : " , celcius_temps_gen)
    
    for celc in celcius_temps_gen:
        print(celc , end=" ")
    print()
    
    print("-" *30)
    
    for celc in celcius_temps_gen:
        print(celc , end=" ")
    print()
    
if __name__ == "__main__":
    main()