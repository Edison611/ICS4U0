import pickle
import json
from province import Province


# This file is something extra that can allow the user to create their own input file
# They will be able to also see their results in a file called user_out.txt
# NOTE: that this is not the best version of this and only contains limited features
# NOTE: ontario_example and test_cases are the 2 main files that should be looked at

while True:
    try:
        with open("Data Files/users_data.pkl", 'rb') as read_file:
            province = pickle.load(read_file)
        file_path = input("Type the path of your json file or \'save\' to save your progress: ")
        if file_path == "save":
            with open("Data Files/users_data.pkl", 'wb') as write_file:
                pickle.dump(province, write_file)
            break
        file = open(file_path)
        data = json.load(file)

        for city in data["Cities"]:
            province.add_city(city)

        for connection in data["Roads"]:
            for road in data["Roads"][connection]:
                province.add_road(connection, road[0], road[1])

        # Finding the shortest path and writing it onto a numbered txt file
        count = 0
        for case in data["Cases"]:
            count += 1
            file_name = "user_out" + str(count) + ".txt"
            province.shortest_path(case, data["Cases"][case], file_name)

    except EOFError:
        try:
            # No user data was found
            file_path = input("Type the path of your json file: ")
            file = open(file_path)
            data = json.load(file)
            province = Province(data["Province"])
            with open("Data Files/users_data.pkl", 'wb') as write_file:
                pickle.dump(province, write_file)
            continue
        except FileNotFoundError:
            print("The file you chose was not found. ")
            continue
    except FileNotFoundError:
        print("The file you chose was not found. ")
        continue

