from province import Province

# This is a file you can run

# Opens a file of all canadian cities using a file found online

city_info = open("Data Files/canadacitiescopy.txt", "r")

headings = city_info.readline().replace("\"", "").split(',')

indexes = {}
for i in range(len(headings)):
    indexes[headings[i]] = i

Ontario = Province("")

# Adds all information to the province
for line in city_info:

    line = line.replace("\"", "")
    line = line.split(',')

    if line[indexes['province_name']] != 'Ontario':
        continue

    city_name = line[indexes['city']]
    city_pop = int(float(line[indexes['population']]))

    Ontario.add_city(city_name)
    Ontario.access_city(city_name).set_population(city_pop)

city_info.close()

cities = Ontario.get_cities()
# Allows user to input a city and see that cities population
choice = ""
while choice not in cities:
    choice = input("Please enter a city in Ontario: ")

choice_pop = Ontario.access_city(choice).get_population()

total_pop = Ontario.total_population()

print(choice + "'s population is: " + str(choice_pop))
print("Ontario's total population is: " + str(total_pop))


