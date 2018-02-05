cities = ['Adelaide', 'Davon', 'Sydney', 'Alice Springs', 'Melbourne']

with open('cities.txt', 'w') as city_file:
    for city in cities:
        print(city, file=city_file)
