



choices = ["Population", "Test Cases", "User Input"]

while True:
    print("Here are the options: ")
    print(choices)
    inp = input("Please enter a valid option or \'end\' if you would like to end the program: ")
    if inp == "Population":
        import ontario_example
    elif inp == "Test Cases":
        import test_cases
    elif inp == "User Input":
        import user_input
    elif inp == "end":
        print("Thank you for using the program")
        break
    else:
        print("Please choose a valid option in the list")
        continue

"""
Source Used:

[1]“Read JSON file using Python,” GeeksforGeeks, Dec. 17, 2019. https://www.geeksforgeeks.org/read-json-file-using-python/

[2]“Dijkstra’s Algorithm,” Programiz.com, 2019. https://www.programiz.com/dsa/dijkstra-algorithm

[3]Python Software Foundation, “3.7.3 Documentation,” Python.org, 2019. https://docs.python.org/3/

"""
