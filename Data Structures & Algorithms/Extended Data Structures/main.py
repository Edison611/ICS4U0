# -----------------------------------------------------------------------------
# Name:        Extending Data Structures Assignment
# Purpose:     To create a small program based off the Data Structures Assignment
#              with the use of inheritance and extending its features using different
#              levels of Government
# Course:      ICS4U0
# Author:      Edison Ying
# Created:     25-Apr-2023
# Updated:     3-May-2023
# -----------------------------------------------------------------------------
import subprocess

# Choices that user can make
choices = ["Cities", "Test Cases"]

# Loops through so user can choose function that they desire
while True:
    print("Here are the options: ")
    print(choices)
    inp = input("Please enter a valid option or \'end\' if you would like to end the program: ")
    if inp == "Cities":
        import canada
    elif inp == "Test Cases":
        import test_cases
        # subprocess.run(["python", "./Executables/test_cases.py"])
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

[4] w3schools, https://www.w3schools.com/
"""
