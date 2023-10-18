def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    guess = None

    for key in questions:
        print("-------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        while guess not in ["A","B","C","D"]:
            guess = input("Enter (A, B, C, or D): ").upper()

        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        guess = None
        question_num += 1

    display_score(correct_guesses, guesses)
    play_again()


def check_answer(answer, guess):
    if answer == guess:
        return 1
    else:
        return 0

def display_score(corrrect_guesses, guesses):
    print("------------------")
    print("RESULTS")
    print("-------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = corrrect_guesses
    print("Your score is:", score)

    passed = int(score/len(questions) * 100)
    if passed > 50:
        print("--------------")
        print("You passed!")
        print("U have "+ str(passed)+"%")
    else:
        print("--------------")
        print("You didn't pass")
        print("U have " + str(passed) + "%")

def play_again():
    response = input("Do you want to play again? (yes or no: ").upper()
    if response == "YES":
        new_game()
    else:
        print("-----------------")
        print("Thank you for playing!!")

questions = {
    "Who created Python?:  ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates","D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000","D.2016"],
           ["A. Lonely Island", "B. Smosh","C. Monty Python", "D. SNL"],
           ["A. True","B. False","C. sometimes", "D. What's Earth?"]]

new_game()

