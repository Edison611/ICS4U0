# -----------------------------------------------------------------------------
# Name:        Review and New
# Purpose:     Reviewing programming concepts from Grade 11 and
#              encouraging ethical uses of computers
#
# Author:      Edison Ying
# Created:     08-Feb-2023
# Updated:     20-Feb-2023
# -----------------------------------------------------------------------------

import random
import time

# Begin the timer
total_start_time = time.time()


class System:
    """ Handles statistics """
    def __init__(self, start_time, topics):
        """ initializes the object """
        self.start_time = start_time
        self.topics = list(topics)
        # topics is passed by reference, so we change it to its own value

    def get_topics(self):
        """ Returns the original topic list """
        return self.topics

    def time_calc(self, task):
        """
        Calculates the time a user has spent on a specific part of the program
        Outputs those results in a print statement

        Parameters
        ----------
        task : str
            the task we are doing the time calculation for
        """
        current_time = time.time() - self.start_time
        current_min = int(current_time // 60)
        current_sec = int(current_time % 60)
        print("You have spent " + str(current_min) + " minutes and " + str(current_sec) + " seconds on this " + task)

    def perc_calc(self, numerator, denominator):
        """
        Calculates the percentage of a fraction

        Parameters
        ----------
        numerator : int, float
            numerator of a fraction
        denominator : int, float
            denominator of a fraction

        Returns
        -------
        percent_complete : int
            the fraction in terms of a percent
        """
        percent_complete = int(100 * numerator / denominator)
        return percent_complete


def choosing_phase(topics):
    """
    Allows user to choose their ethical topic

    Lists out all ethical paths, user selects a number as their choice.
    Then it will output the topic that the user chose.

    Parameters
    ----------
    topics : list
        All the topics that are available

    Returns
    ----------
    string
        The topic that the user chose

    Raises
    ----------
    ValueError
        When user choice is not a number within range
        When user choice is not an integer (Can also be classified as TypeError)
    """
    print("Choose a number to explore that aspect of ethics in computer science")
    print("If you would not like to continue, please type the word \"end\"")
    print("0. (Select to see your statistics)")
    for i in range(len(topics)):
        topic = topics[i]
        topic_num = str(i+1)
        print(topic_num + ". " + topic)

    while True:
        flag = False
        try:
            choice = input("Type your choice here: ")
            if choice == "end":
                flag = True
                break
            choice = int(choice)
            if choice > len(topics) or choice < 0:
                print("Please choose one of the numbers in the list")
                continue
            break
        except ValueError:
            print("Please choose a number")
    if flag:
        topic = "end"
    elif choice == 0:
        topic = "stats"
    else:
        topic = topics[choice-1]
    return topic


def allow_continue():
    """ Leaves blank spaces, user must press enter to continue """
    cont = " "
    while cont != "":
        print("")
        cont = input("Please press enter to continue...")
        print("")
    return


def intellectual_property():
    """ The ethical intellectual property path in the program """

    print("Just like how there are owners to property on the land on Earth,")
    print("There are also owners to documents, designs, licenses etc. that are found online.")
    print("Some that are free to use, but also some that you have to pay for.")
    print("This is what's known as intellectual property.")
    allow_continue()
    print("Take that movie you watched on Netflix, you paid a monthly subscription to have access to all those shows.")
    print("However, there are now many illegal pirated websites where you can watch those shows for free")
    print("Those websites are major violations in computer ethics")
    print("They are stealing money away from the producers who worked so hard to create the show")
    print("So keep in mind that you should not go on any pirated websites to watch movies or shows")
    allow_continue()
    print("Now take that assignment about encouraging ethical computer uses.")
    print("If you used a website to research, you must cite that source.")
    print("For example: https://www.comptia.org/blog/ethical-problems-in-computing")
    print("If you don't cite your sources you can face massive consequences.")
    allow_continue()
    return


def cyberbullying():
    """ The cyberbullying prevention path in the program """
    pronouns = [
        "I Am ",
        "You Are "
    ]
    adjectives = [
        "Unstoppable",
        "A Leader",
        "Awesome",
        "Amazing",
        "Fantastic",
        "Dazzling",
        "Beautiful"
    ]
    print("In recent days, it has been very easy to communicate with others because of the internet.")
    print("However, some people decide to abuse that power and bully others online.")
    print("This is called cyberbullying.")
    print("Both at work and at school, we want to live in a positive environment.")
    print("So let's get into the positive mindset so that you can spread that positivity!")
    # User repeats 3 positive phrases semi-randomly chosen using a number that they choose
    for i in range(3):
        while True:
            try:
                choice = int(input("Choose any positive number: "))
                if choice <= 0:
                    print("To be positive you must choose a positive number")
                    print("Let's try again")
                    continue
                break
            except ValueError:
                print("Please choose a valid Integer")
        print("Repeat the following sentence (EXACTLY)")
        pronoun_choice = random.randint(0, 1)
        adj_choice = choice % len(adjectives)
        sentence = pronouns[pronoun_choice] + adjectives[adj_choice]
        print(sentence)

        # Checks if user input matches the actual sentence
        user_input = ""
        while user_input != sentence:
            user_input = input()

    print("Great job!")
    print("Cyberbullying is just as bad as real life bullying")
    print("Everything you say online will affect your digital footprint")
    print("If you don't know if something is true, then do not presume it is true")
    print("Misinformation can lead also lead into cyberbullying.")
    print("Now after you complete this activity, you can go around and spread positivity online!")
    allow_continue()
    return


def privacy():
    """ The privacy path in the program """

    special_char = ["!", "@", "#", "$", "%", "^", "&", "*", "`", "~", "+", "="]
    nums = [str(i) for i in range(10)]
    # Gets users name
    while True:
        flag = False
        name = input("Let's start off by getting your Name:")
        for letter in name:
            if letter in special_char:
                print("Please do not include special characters in your name")
                flag = True
                break
            if letter in nums:
                print("Please do not include numbers in your name")
                flag = True
                break

        if flag:
            continue
        print("Please remove numbers from your name")
        print("Well well well, let's remember " + name + " that giving out your name is not a good practice online")
        print("Storing personal data without a person's agreement is an ethical violation")
        print("So remember, when creating your own service,")
        print("DO NOT store, use or sell a user's personal data without their consent.")
        print("If you do plan to keep a user's personal information,")
        print("Remember to get their permission first by having them agree to your terms of service.")
        allow_continue()
        break


def hacking():
    """ The ethical hacking section of the program """

    print("There are different types of hackers in our world:")
    print("We call the good ones White Hat Hackers")
    print("We call the bad ones Black Hat Hackers")
    print('And we call the ones in between good and bad the Grey Hat Hackers')
    allow_continue()
    print("Hacking refers to gaining unauthorized access to data in a computer")
    print("Ethical hacking is when you are hired to try to break into a security system")
    print("By doing so, security flaws can be found within a system")
    print("This will prevent unethical hackers from actually stealing data from a computer")
    allow_continue()

    # Gives user a random password of a length that they request
    print("Here, we will give you password so that you can keep yourself safe online")
    while True:
        try:
            password_length = int(input("How long would you like your password to be? "))
            if password_length <= 0:
                print("Please type a positive integer value")
                continue
            break
        except ValueError:
            print("Please type in a valid Integer number")
    user_password = password_generator(password_length)
    print(user_password)

    allow_continue()
    print("So with your knowledge in computer science, consider pursuing a career as a White Hat Hacker")
    print("Help prevent unethical hackers from harming others")
    print("Remember, always make sure what you are doing is legal")
    print("Sign the proper documents to become an ethical hacker")
    allow_continue()
    return


def password_generator(length):
    """
    Generates a random password of input length

    Generates all alphabet letters in a list,
    then randomly add letters or numbers until input length is reached

    Parameters
    ----------
    length : int
        The length of the password required

    Returns
    ----------
    string
        The password that was generated

    Raises
    ----------
    TypeError
        When user choice is not an integer (Can also be classified as ValueError)
    """
    try:
        if not isinstance(length, int):
            raise TypeError("Please provide a valid integer")
    except TypeError:
        print("Please provide a valid integer")
        return

    password = ""
    # Generate all alphabet values in a list
    alphabet = []
    for i in range(65, 91):
        alphabet.append(chr(i))
        # Uses ASCII numbers to generate a list with all capital letters
        # Basically converts numbers into letters/characters

    # Generate an N (length) character long random string
    for i in range(length):
        character = random.randint(1, 2)
        if character % 2 == 0:
            password = password + random.choice(alphabet)
        else:
            password = password + str(random.randint(0, 9))
    return password


all_topics = ["Intellectual Property", "Cyberbullying", "Privacy", "Hacking"]

current_session = System(total_start_time, all_topics)

# Introduction Phase
print("Welcome, today we are going to cover ethical computing practices!")
print("")
print("Before we get started, let us go through the term of ethics:")
print("Ethics are moral principles and guidelines that should be followed when conducting an activity.")
print("")
print("Now let's get started!")
allow_continue()

# Choosing the category
path = ""
while path != "end":
    if len(all_topics) == 0:
        break
    path = choosing_phase(all_topics)

    if path == "Intellectual Property":
        intellectual_property()
    elif path == "Cyberbullying":
        cyberbullying()
    elif path == "Privacy":
        privacy()
    elif path == "Hacking":
        hacking()
    elif path == "stats":
        completed = len(current_session.get_topics()) - len(all_topics)
        percentage_complete = current_session.perc_calc(completed, len(current_session.get_topics()))
        print("You have completed " + str(percentage_complete) + "% of the lessons")
        current_session.time_calc("activity")
        allow_continue()
        continue
    else:
        break
    all_topics.remove(path)

# Quiz will begin after this
print("Now that you've learned about ethical computing practices")
print("Let's quiz you on what you have learned!")
print("Please answer all questions using lower case letters")
allow_continue()

# Questions can be added, without any actual change to the program
questions = {
    "What color are good hackers?": "white",
    "true or false, you cannot store personal information without a user's consent.": "true",
    "What is the form of online bullying called": "cyberbullying",
    "true or false, you can take information you find online and say that its your own work": "false",
    "What word best describes the unauthorized access to data in a computer": "hacking",
    "true or false, your digital footprint can easily be erased": "false",
    "Fill in the blank, ____________ property is intangible property that can be found online": "intellectual",
    "Fill in the blank, ethics are _____ principles and guidelines that should be followed when conducting an activity": "moral"
}
total = 0

# Begin quiz, keep track of their score and time
start = time.time()
quiz_stats = System(start, all_topics)
# Go through each question and see if user's answer matches correct answer
for question in questions:
    answer = questions[question]
    print(question)
    response = input()
    if response == answer:
        print('Correct!')
        total += 1
    else:
        print("Sorry, that is incorrect!")
        print("The correct answer was: " + answer)
    print("")

end = time.time()
total_end_time = time.time()

# Calculate their score and time it took using integer division and modulus

accuracy = quiz_stats.perc_calc(total, len(questions))
print("You answered " + str(total) + " out of " + str(len(questions)) + " correctly!")
print("Your accuracy was " + str(accuracy) + "%")
quiz_stats.time_calc("quiz")
current_session.time_calc("activity")

allow_continue()

# Concluding sentences
print("Well that's it for today!")
print("I hope you will continue to perform ethical computing practices at home, at school, and at work!")
print("Goodbye!")
