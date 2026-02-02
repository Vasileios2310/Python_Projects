cities = ["london" , "paris" , "barcelona" , "athens"]

# filter city names ( longer than 5 characters)
long_city = list(filter(lambda city : len(city) > 5 , cities))
print(f"long cities > 5 characters , {long_city}")

# capitalized cities
cap_cities = list(map(lambda city : city.title() , cities))
print(f"cap cities : {cap_cities}")


# capitilized all long cities
cap_long_cities = list(map(lambda city : city.title() , long_city))
print(f"cap long cities  : {cap_long_cities}")


cap_length_cities = list(map(lambda city : city.title() , filter(lambda city : len(city) > 5 , cities)))
print(f"cap long cities  : {cap_length_cities}")