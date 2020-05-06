from sys import exit
import random
import time

#
""" 
   The Program enables you to play with the computer. 
   Each one is given a chance to have their turn and
   the one who has
   the highest number is declared the winer
"""

# setting range of numbers for the die

min = 1  # sets the value of min to 1 sinc the die starts its values at 1
max = 6  # sets the value of max to 6 since the die has the range of values up to 6

x = 0  # sets the value of x to 0
y = 0  # sets the value of y to 0


player_name = input("Enter your name please: ") # the player inputs his/her name
Cap = player_name.upper() # sets the variable Cap into the computer opponent

roll_again = "yes" # sets the value of roll_again to yes

while roll_again == "yes": # the while loop executes if the value is "yes"
    if roll_again == "no":
        exit(0)  # the program will end if the input is "no"

    print("Your Turn")

    time.sleep(1)
    print("Rolling the die...")

    time.sleep(2)

    x = random.randint(min, max)  # the computer will generate the rolling of the die and the minimum and maximum value are set
    y = random.randint(min, max)  # the computer will generate the rolling of the die and the minimum and maximum value are set


    def dice(m):  # function simulating the die or for easier visualization
        if m == 1: # if the value of the die is 1
            print(""" 
          _________
         |         |
         |         |  
         |    *    | 
         |         | 
         |_________|  """)

        elif m == 2: # if the value of the die is 2
            print("""
          _________
         |         |
         |     *   |
         |         | 
         |   *     | 
         |_________|  """)

        elif m == 3: # if the value of the die is 3
            print("""
          _________
         |         |
         |      *  |  
         |    *    | 
         |  *      | 
         |_________|  """)

        elif m == 4: # if the value of the die is 4
            print("""
          _________
         |         |
         |  *   *  |  
         |         | 
         |  *   *  | 
         |_________|  """)


        elif m == 5: # if the value of the die is 5
            print(""" 
          _________
         |         |
         |  *   *  |  
         |    *    | 
         |  *   *  | 
         |_________|  """)


        elif m == 6:   # if the value of the die is six
            print("""   
          _________
         |         |
         |  *   *  |  
         |  *   *  | 
         |  *   *  | 
         |_________|  """)


    dice(x)


    time.sleep(1)

    print("Computer's Turn")
    time.sleep(1)

    print("Rolling the die")
    time.sleep(2)

    dice(y)

    time.sleep(1)




    if x == y: # set the condition of draw, both the computer and the player has the same output

        print("It's a draw.")
        time.sleep(1)

        print("Input 'yes' to play again or 'no' to stop playing. Note: The program is case sensitive")


    elif x > y: # sets the condition of win to the player

        print("Congrats! You Won"), Cap
        time.sleep(1)

        print("To play again, input 'yes'. To stop playing, input 'no'. Note: The program is case sensitive")


    elif x < y: # sets the condition of win to the computer and lose to the player

        print("Sorry! You Lost. Try again"), Cap
        time.sleep(1)

        print("To roll again, input 'yes'. To stop playing input 'no'. Note: The program is case sensitive")


    roll_again = input("Roll the die again?")

