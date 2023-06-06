from province import Province

import json

# This is a file you can run

# Read the input test data
Ontario = Province("Ontario")
for i in range(1, 4):
    f_name = "inp" + str(i) + ".json"
    f = open("Data Files/" + f_name)

    data = json.load(f)

    province = Province(data["Province"])

    for city in data["Cities"]:
        province.add_city(city)

    for connection in data["Roads"]:
        for road in data["Roads"][connection]:
            province.add_road(connection, road[0], road[1])

    # Finding the shortest path and writing it onto a numbered txt file
    count = 0
    for case in data["Cases"]:
        count += 1
        file_name = "out" + str(i) + "-" + str(count) + ".txt"
        province.shortest_path(case, data["Cases"][case], file_name)


# Example Test Case
"""
Ontario = Province("Ontario")

Ontario.add_city("Mississauga")
Ontario.add_city("Toronto")
Ontario.add_city("Oakville")
Ontario.add_city("Brampton")
Ontario.add_city("Niagara Falls")
Ontario.add_city("Hamilton")

Ontario.add_road("Mississauga", "Toronto", 50.0)
Ontario.add_road("Mississauga", "Oakville", 20.0)
Ontario.add_road("Mississauga", "Brampton", 10.0)
Ontario.add_road("Niagara Falls", "Hamilton", 14.5)

Ontario.shortest_path("Toronto", "Oakville", "out1-1.txt")
Ontario.shortest_path("Toronto", "Niagara Falls", "out1-2.txt")
"""




