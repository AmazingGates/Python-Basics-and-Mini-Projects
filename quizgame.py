# Quiz Game - In this section we will be creating a Quiz Game
def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("*************************************************")
        print(key)
        for i in options[question_num-1]:  # Here we used a nested for loop
            print(i)
        guess = input("Enter (A, B, C, D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1


    display_score(correct_guesses,guesses)
#**********************************************************************************************

def check_answer(answer, guess):
    if answer == guess:
        print("Awesome!")
        return 1
    else:
        print("Try Again")
        return 0
    
#**************************************************************************************************

def display_score(correct_guesses, guesses):
    print("****************************************")
    print("Results")
    print("****************************************")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int(correct_guesses/len(questions)*100)
    print("Your Score Is: " +str(score)+ "%")


#***************************************************************************************************


def play_again():
    
    response = input("Do You Want To Play Again? (yes/no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


#**************************************************************************************************


questions = {             # Here we used a dict to store our Questions
    "What is the square root of 9 to the 2nd power? ": "A",    
    "How long does an Elephant stay pregnant? ": "B",
    "What is the name of the tallest mountain in the world? ": "C",
    "Whose real name is Kal El? ": "A"
}

options = [                # Here we used a 2D list to store our anwser options
    ["A = 9", "B = 81", "C = 18", "D = 27"],
    ["A = 6 Months", "B = 22 Months", "C = 9 Months", "D = 13 Months"],
    ["A = Mt. Helen", "B = Mt. Olympus", "C = Mt. Everest", "D = Mt. Rushmore"],
    ["A = Superman", "B = Thanos", "C = Goku", "D = The Silver Surfer"]
]

new_game()

while play_again():
    new_game()

print("*****************************************************************************")
print("SEE YOU LATER!!!")