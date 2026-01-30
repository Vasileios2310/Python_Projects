cities = ["london" , "paris" , "barcelona" , "athens"]

long_city = list(filter(lambda city : len(city) > 5 , cities))

print(f"long cities > 5 characters , {long_city}")