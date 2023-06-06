from federal import Federal
import json
# Allows user to choose a city and province in Canada to find its statistics

# Opens a file of all canadian cities using a file found online
city_info = open("./Data Files/canadacitiescopy.txt", "r")

headings = city_info.readline().replace("\"", "").split(',')

indexes = {}
for i in range(len(headings)):
    indexes[headings[i]] = i

# Creates federal object
Canada = Federal("Canada", "Justin Trudeau", 5, 1988000000, 1.29)

# Loads supplementary info
f = open("./Data Files/taxAmounts.json")
data = json.load(f)

# Adds all information to the province
for line in city_info:

    line = line.replace("\"", "")
    line = line.split(',')

    p_name = line[indexes['province_name']]

    if p_name not in Canada.get_province_names():
        Canada.add_province(p_name)
        if p_name in data:
            Canada.provinces[p_name].set_tax(data[p_name])

    city_name = line[indexes['city']]
    city_pop = int(float(line[indexes['population']]))
    city_dense = float(line[indexes['density']])
    city_time = line[indexes['timezone']]

    Canada.provinces[p_name].add_city(city_name)
    Canada.provinces[p_name].cities[city_name].get_info().set_population(city_pop)
    Canada.provinces[p_name].cities[city_name].get_info().set_density(city_dense)
    Canada.provinces[p_name].cities[city_name].get_info().set_timezone(city_time)

city_info.close()

# Allows user to input a province city and see its population and other statistics
print(f"The population of Canada is: {Canada.get_info().get_population(Canada.get_provinces())}")
print(f"The percent defense spending of its gdp is: {Canada.get_defense_spending()}%")
print(f"The amount of money that is equal to is: ${Canada.get_defense_spending()*Canada.get_gdp()*0.01}")

# Gets name of all provinces
provinces = []
for province in Canada.provinces:
    provinces.append(Canada.provinces[province].get_name())

print("Here are the provinces to choose from: ")
print(provinces)
prov_choice = ""
while prov_choice not in provinces:
    prov_choice = input("Choose a province: ")
    if prov_choice not in provinces:
        print("Please choose a valid province")

# print(Canada.provinces[prov_choice].get_type())

print(f"Here is the population of {prov_choice}: {Canada.provinces[prov_choice].get_info().get_population(Canada.provinces[prov_choice].get_cities())}")
print(f"You would pay {Canada.get_tax() + Canada.provinces[prov_choice].get_tax()}% in sales tax in this province")

# Gets all the cities within the province chosen
print("Here are the cities in the province to choose from: ")
print(Canada.provinces[prov_choice].get_city_names())

cities = Canada.provinces[prov_choice].get_city_names()
city_choice = ""
while city_choice not in cities:
    city_choice = input("Choose a city: ")
    if city_choice not in cities:
        print("Please choose a valid city")

print(f"Here is the population of {city_choice}: {Canada.provinces[prov_choice].cities[city_choice].get_info().get_population()}")
print(f"The density of {city_choice} is {Canada.provinces[prov_choice].cities[city_choice].get_info().get_density()}")
print(f"The timezone in {city_choice} is {Canada.provinces[prov_choice].cities[city_choice].get_info().get_timezone()}")

