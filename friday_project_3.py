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

for question, options in questions.items():
    print(question)
    for option, text in options.items():
        print(option + ") " + text)
    answer = input("Your answer: ").upper()
    correct_answer = answers.get(question[0])
    
    if answer == correct_answer:
        print("Correct \n")
        score += 1
    else:
        print("Wrong. The correct answer is:", correct_answer + "\n")

print("Your score is", score)

if score == 5:
    print("Congrats! You won a $10 gift card")
else:
    print("Better luck next time!")

    x = "barbie"