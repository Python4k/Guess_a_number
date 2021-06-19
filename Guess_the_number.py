# Project name: "Guess the number"
# Comment:"WHY ONLY 600 CHARACTERS?"
# Full code:
import time
import random


generated_number = random.randint(1,100)
attempts = 7

print("Guess the number\n\nIn this game you have to guess the number from 1 to 100\nYou have 7 attempts for guess a number")

# Main loop 
while attempts > 0:
    

    # Player input number
    player_number = int(input("Input your number: "))

    # Comparing numbers
    if attempts == 1 and player_number != generated_number:
        print(f"You lose... Generated number: {generated_number}")
        break

    elif player_number < generated_number:
        print(f"Your number is small. You have {attempts - 1} attempts")

    elif attempts == 1:
        print(f"Your number is high. You have {attempts - 1} attempts")
    
    else:
        print(f"Сongratulations! You win. Generated number: {generated_number}")
    
    # Decrement 
    attempts -= 1
    
time.sleep(5)
