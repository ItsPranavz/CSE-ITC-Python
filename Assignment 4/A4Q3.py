# Program for a multiplication game
import random

# generate ten random multiplication questions
for i in range(10):
   # generate two random numbers between 1 and 9
   num1 = random.randint(1, 9)
   num2 = random.randint(1, 9)

   # compute the correct answer
   answer = num1 * num2

   # ask the player to solve the question
   guess = input(f"Question {i+1}: {num1} x {num2} = ")
   guess = int(guess)

   # check if the player's guess is correct
   if guess == answer:
       print("Right!")
   else:
       print(f"Wrong. The answer is {answer}.")
