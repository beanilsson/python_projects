import random
min = 1
max = 20

roll_again = "yes"
pool_status = 0
purse_status = 0

print "How much money do you bring to the table?"
purse_status = int(input())

while roll_again == "yes" or roll_again == "y":
    print "What numbers do you want to bet on? (1-20)"
    first_number = int(input())
    second_number = int(input())
    print "Purse status: ", purse_status
    print "How much do you want to bet?"
    bet = int(input())
    while bet > purse_status:
        print "You don't have that kind of money, try again"
        bet = int(input())
    print "Rolling the dices ..."
    print "The values are ..."
    dice_one = random.randint(min, max)
    dice_two = random.randint(min, max)
    if first_number == dice_one and second_number == dice_two:
      print dice_one, " ", dice_two
      print "Congratulations! You aced both numbers"
      purse_status += bet
    elif first_number == dice_one and second_number != dice_two:
      print dice_one, " ", dice_two
      print "Good job! You guessed the first number"
      purse_status += bet/2
    elif first_number != dice_one and second_number == dice_two:
      print dice_one, " ", dice_two
      print "Good job! You guessed the second number"
      purse_status += bet/2
    else:
      print dice_one, " ", dice_two
      print "Bad luck, you didn't guess any number right"
      purse_status -= bet

    if purse_status > 0:
      print "Purse status: ", purse_status
      roll_again = raw_input("Roll again? (yes/y) ")
    elif purse_status <= 0:
      print "Sorry, you're out of funds. Thanks for playing"
      exit()
    else:
      print "Thanks for playing!"
