
# This program reads 10 states and capitals
# into a dictionary whose keys are state names
# and whose values are the capital.
# Then propts the user to enter a state
# and prints the corresponding capital values.
# Program stops when user enters: "quit"



# Declares dictionary of 10 valid state names and their capitals.
statesDict = {
    "Colorado" : "Denver",
    "Florida" : "Tallahassee",
    "Kentucky" : "Frankfort",
    "Maryland" : "Annapolis",
    "North Carolina" : "Raleigh",
    "New Hampshire" : "Concord",
    "New Jersey" : "Trenton",
    "New York" : "Albany",
    "Vermont" : "Montpelier",    
    "Wyoming" : "Cheyenne"
}


# Prompts user to enter state name; prints corresponding capital.
def enterStates():

    # Prints list of valid states to the user.
    statesList = ["Colorado","Florida","Kentucky","Maryland","North Carolina","New Hampshire","New Jersey","New York","Vermont","Wyoming"]
    print("States: ")
    print(" ")
    for state in statesList:
        print(state)
    print(" ")
    print("----------")
    print(" ")

    while True:

        # Prompts user to input a state.
        userInput = input("Enter a state from the list to see its capital or enter 'quit' to exit. ")
        # Include code to evaluate with case insensitivity.
        userInputTitle = userInput.title()
        if userInputTitle in statesDict:
            capital = statesDict[userInputTitle]
            print(f"The capital of {userInputTitle} is {capital}. ")
            print(" ")

        # Exits loop with sentinel value;
        # Ensures that "else" will not be read if "quit" condition is met by converting to lower.
        elif userInputTitle.lower() == "quit":
            break
        
        # Catch invalid input and re-prompt user for valid input.        
        else:
            print(" ")
            print("Invalid Input.\n")



enterStates()
