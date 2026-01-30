cities = ["london" , "paris" , "barcelona" , "athens"]

# titled cities

cap_cities = list(map(lambda city : city.title() , cities))
print(cap_cities)


 
for city in cities:
    print(city.title())
    
    
cities_v2 = [city.title() for city in cities]
print(cities_v2)