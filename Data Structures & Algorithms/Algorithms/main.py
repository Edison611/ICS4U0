# -----------------------------------------------------------------------------
# Name:        Algorithms Assignment
# Purpose:     To create a program based off the Data Structures Assignment
#              and use different algorithms to sort and search for objects in a list
# Course:      ICS4U0
# Author:      Edison Ying
# Created:     11-May-2023
# Updated:     22-May-2023
# -----------------------------------------------------------------------------
from PY.world import World
from sorting import *
from searching import *
import json
import random
from timeit import default_timer as timer

# Creates world object
world = World()

# Loads supplementary info
f = open("Data Files/cities.json")
data = json.load(f)

limit = int(input("Enter the amount of objects needed in the array: "))
count = 0
# Adds all information to the province
for city in data:
    count += 1
    name = city['name']
    country = city['cou_name_en']
    population = city['population']
    if country not in world.get_country_names():
        world.add_country(country)
    world.countries[country].add_city(name)
    world.countries[country].cities[name].population = population
    if count == limit:
        break

f.close()

# -------------------------
# Get cities list
cities = []
countries = world.get_countries()
for country in countries:
    for city in country.cities:
        # print(country.cities[city].name)
        # print(country.cities[city].population)
        cities.append(country.cities[city])

# -------------------------
# Linear Search Before Sorting
# out = open("./Output Files/out-linear-search-before.txt", "a")
out = open("./Output Files/out-linear-search-before-non-existing.txt", "a")
out.write(f"Linear Search Before: ({limit} objects)" + "\n")
out.write("-----------------------" + "\n")
for i in range(25):
    random.shuffle(cities)
    start = timer()
    ind = linear_search(cities, "adjdjkak")
    end = timer()
    out.write(str(end-start) + "\n")
out.write("-----------------------" + "\n")
out.close()
print("Done Searching (Before)")

# -------------------------
# Testing with just numbers

# pop = []
# for city in cities:
#     pop.append(city.get_population())

# start = timer()
# sort = test(pop)
# end = timer()
# #
# print(end-start)
# print(sort)

# -------------------------
# Insertion Sort Algorithm

# out = open("Output Files/output-sort.txt", "a")
#
# out.write(f"Insertion Sort: ({limit} objects)" + "\n")
# out.write("-----------------------" + "\n")
# # Get 25 test cases
# for i in range(25):
#     random.shuffle(cities)
#
#     start = timer()
#     sort = insertionSort(cities)
#     end = timer()
#     out.write(str(end-start) + "\n")
# out.write("-----------------------" + "\n")
# out.close()
# print("DONE")

# Printing first 20 elements to see if it works
# sort.reverse()
# for i in range(1,21):
#     print(f"{i}. {sort[i].get_name()}, {sort[i].get_population()}")

# -------------------------
# Built-In Sorting Algorithm and Searches

# Opening all the files
out = open("./Output Files/out-builtin-sort.txt", "a")
out.write(f"Built-in Sort: ({limit} objects)" + "\n")
out.write("-----------------------" + "\n")

out_search_existing = open("./Output Files/out-linear-search-after.txt", "a")
out_search_existing.write(f"Linear Search After (Existing): ({limit} objects)" + "\n")
out_search_existing.write("-----------------------" + "\n")

out_binarysearch_existing = open("./Output Files/out-binary-search.txt", "a")
out_binarysearch_existing.write(f"Binary Search (Existing): ({limit} objects)" + "\n")
out_binarysearch_existing.write("-----------------------" + "\n")

out_search_nonexisting = open("./Output Files/out-linear-search-after-non-existing.txt", "a")
out_search_nonexisting.write(f"Linear Search After (Non Existing): ({limit} objects)" + "\n")
out_search_nonexisting.write("-----------------------" + "\n")

out_binarysearch_nonexisting = open("./Output Files/out-binary-search-non-existing.txt", "a")
out_binarysearch_nonexisting.write(f"Binary Search (Non Existing): ({limit} objects)" + "\n")
out_binarysearch_nonexisting.write("-----------------------" + "\n")

for i in range(25):
    random.shuffle(cities)

    start = timer()
    sort = sorted(cities, key=lambda x:x.population)
    end = timer()
    out.write(str(end - start) + "\n")

    # Linear Search for Existing Item
    start = timer()
    inds = linear_search(sort, "Sadovoye")
    end = timer()
    out_search_existing.write(str(end - start) + "\n")

    # Binary Search for Existing Item
    start = timer()
    indb = binary_search(sort, 6333)
    end = timer()
    out_binarysearch_existing.write(str(end - start) + "\n")

    # Linear Search for Non-Existing Item
    start = timer()
    indsn = linear_search(sort, "adlkskladkjjd")
    end = timer()
    out_search_nonexisting.write(str(end - start) + "\n")

    # Binary Search for Non-Existing Item
    start = timer()
    indbn = binary_search(sort, -1)
    end = timer()
    out_binarysearch_nonexisting.write(str(end - start) + "\n")

out.write("-----------------------" + "\n")
out_search_existing.write("-----------------------" + "\n")
out_binarysearch_existing.write("-----------------------" + "\n")
out_search_nonexisting.write("-----------------------" + "\n")
out_binarysearch_nonexisting.write("-----------------------" + "\n")

out.close()
out_search_existing.close()
out_binarysearch_existing.close()
out_search_nonexisting.close()
out_binarysearch_nonexisting.close()

print("Done Outputting")

print(f"Linear Search: (Index: {inds}), (Name: {sort[inds].name}), (Population: {sort[inds].population}) ")
print(f"Binary Search: (Index: {indb}), (Name: {sort[indb].name}), (Population: {sort[indb].population}) ")

# Printing first 20 elements to see if it works
sort.reverse()
for i in range(1,20):
    print(f"{i}. {sort[i].get_name()}, {sort[i].get_population()}")
# -------------------------

"""
Sources:

[1] https://github.com/johnfraserss/ICS4U/blob/master/examples/sorting/Insertion%20Sort/Python/main.py

[2] https://www.geeksforgeeks.org/insertion-sort/

[3] https://www.geeksforgeeks.org/binary-search/
"""


