import math
import random

powerball = input("Welcome to the PowerBall number generator. \nWould you like some Powerball number? (yes/no): ")

if powerball == "yes":
    number_1 = random.randint(1, 69)
    number_2 = random.randint(1, 69)
    number_3 = random.randint(1, 69)
    number_4 = random.randint(1, 69)
    number_5 = random.randint(1, 69)
    number_6 = random.randint(1, 26)

    print()

    print("Your numbers are " + str(number_1) + "  " + str(number_2) + "  " + str(number_3)  + "  " + str(number_4) + "  " + str(number_5) + "    " + str(number_6))

    print("Thank you, come again")

else:
  print ("buy high sell low!")