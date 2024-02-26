Tutorial for each previous 3 projects

Project 1

    a_large_object = input("Enter a large object: "): This line prompts the user to enter a large object and assigns the input value to the variable a_large_object.

    large_objects_plural = input("Enter a large object (plural): "): This line prompts the user to enter a plural form of a large object and assigns the input value to the variable large_objects_plural.

    an_adjective = input("Enter an adjective: "): This line prompts the user to enter an adjective and assigns the input value to the variable an_adjective.

    a_body_part = input("Enter a body part: "): This line prompts the user to enter a body part and assigns the input value to the variable a_body_part.

    a_restaurant = input("Enter a restaurant: "): This line prompts the user to enter a restaurant name and assigns the input value to the variable a_restaurant.

    a_food = input("Enter a food: "): This line prompts the user to enter a type of food and assigns the input value to the variable a_food.

    another_food = input("Enter another food: "): This line prompts the user to enter another type of food and assigns the input value to the variable another_food.

    madlib = f'''...''': This line creates a formatted string (f-string) called madlib which contains placeholders for the variables entered by the user.

    print(madlib): This line prints out the madlib string, which contains the user's inputs interpolated into the text.

Project 2

    import math: This line imports the math module, which provides mathematical functions.

    import random: This line imports the random module, which provides functions for generating random numbers.

    powerball = input("Welcome to the PowerBall number generator. \nWould you like some Powerball number? (yes/no): "): This line prompts the user with a message and waits for input. The input value is stored in the variable powerball.

    if powerball == "yes":: This line starts an if statement to check if the user's input stored in powerball is equal to "yes".

    number_1 = random.randint(1, 69): This line generates a random integer between 1 and 69 (inclusive) and assigns it to the variable number_1.

    number_2 = random.randint(1, 69): This line generates a random integer between 1 and 69 (inclusive) and assigns it to the variable number_2.

    number_3 = random.randint(1, 69): This line generates a random integer between 1 and 69 (inclusive) and assigns it to the variable number_3.

    number_4 = random.randint(1, 69): This line generates a random integer between 1 and 69 (inclusive) and assigns it to the variable number_4.

    number_5 = random.randint(1, 69): This line generates a random integer between 1 and 69 (inclusive) and assigns it to the variable number_5.

    number_6 = random.randint(1, 26): This line generates a random integer between 1 and 26 (inclusive) and assigns it to the variable number_6.

    print(): This line prints an empty line for spacing.

    print("Your numbers are " + str(number_1) + " " + str(number_2) + " " + str(number_3) + " " + str(number_4) + " " + str(number_5) + " " + str(number_6)): This line prints out the generated numbers concatenated with strings to form a message.

    print("Thank you, come again"): This line prints a closing message.

    else:: This line starts the else block, which executes if the condition in the if statement (if powerball == "yes") is not met.

    print ("buy high sell low!"): This line prints a message advising to "buy high sell low!" if the user did not want to generate PowerBall numbers.

Project 3

questions = {
    "1. How long do you think Swift & Kelce relationship will last?": {"A": "leave them alone", "B": "1-5 years", "C": ">5 years"},
    "2. What is the average ROI of S&P 500 annually?": {"A": "30%", "B": "20%", "C": "10%"},
    "3. Does rich dad poor dad best selling finance book still relevant today?": {"A": "Yes", "B": "No"},
    "4. When is the best time to start investing for the retirement?": {"A": "as early as possible", "B": "Once having a job", "C": "After paid off all debt"},
    "5. What is the capital city of London?": {"A": "St. Peterburg", "B": "Cape town", "C": "Amsterdam", "D": "none of the choices"}
}

answers = {
    "1": "A",
    "2": "C",
    "3": "A",
    "4": "A",
    "5": "D"
}

score = 0

print("Hello! finish this quiz to win a $10 gift card \n")

# Loop through each question and its options
for question, options in questions.items():
    print(question)  # Print the question
    for option, text in options.items():
        print(option + ") " + text)  # Print each option
    answer = input("Your answer: ").upper()  # Get the user's answer and convert it to uppercase
    correct_answer = answers.get(question[0])  # Get the correct answer from the 'answers' dictionary based on the question number
    
    # Check if the user's answer is correct
    if answer == correct_answer:
        print("Correct \n")
        score += 1  # Increment the score if the answer is correct
    else:
        print("Wrong. The correct answer is:", correct_answer + "\n")  # Print the correct answer if the user's answer is wrong

print("Your score is", score)  # Print the user's final score

# Check if the user scored full marks
if score == 5:
    print("Congrats! You won a $10 gift card")  # Print a congratulatory message if the user scored full marks
else:
    print("Better luck next time!")  # Print a message if the user didn't score full marks