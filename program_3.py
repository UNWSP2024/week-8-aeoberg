# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).
import random
wrong = 0
correct = 0
randomNumberOfQuestions = 4
states = {"Minnesota":"Saint Paul", "Washington":"Olympia", "New York":"Albany", "Texas":"Austin", "Utah":"Salt Lake City", "South Dakota": "Pierre", "Arizona": "Phoenix", "Florida": "Tallahasse", "Iowa":"Des Moines","Maine":"Augusta" }

for x in range(randomNumberOfQuestions):
    random_key = random.choice(list(states.keys()))

    capital = input(f'What is the capital of {random_key}? ')
    if states[random_key] == capital:
        correct += 1
        print('Correct!')
        print()

    elif capital != states[random_key]:
        wrong += 1
        print(f'Incorrect, the correct answer is {states[random_key]}')
        print()

    else:
        print('Error')

print(f'Correct: {correct}/{randomNumberOfQuestions}')
print(f'Incorrect: {wrong}/{randomNumberOfQuestions}')