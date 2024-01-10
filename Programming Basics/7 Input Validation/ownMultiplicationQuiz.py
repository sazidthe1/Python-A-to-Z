# This is Own Multiplication Quiz Project

import time
import random

def multiplication_quiz():
    num_questions = 10
    num_attempts = 3
    time_limit = 8
    
    for i in range(num_questions):
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        correct_answer = num1 * num2
        attempts = 0
        
        print(f"Question {i + 1}: {num1} x {num2} = ?")
        start_time = time.time()
        
        while attempts < num_attempts:
            user_answer = input("Your answer: ")
            
            if time.time() - start_time > time_limit:
                print("Time's up! Moving to the next question.")
                break
            
            try:
                user_answer = int(user_answer)
                if user_answer == correct_answer:
                    print("Correct!")
                    time.sleep(1)
                    break
                else:
                    attempts += 1
                    if attempts < num_attempts:
                        print(f"Incorrect! Try again. Attempts left: {num_attempts - attempts}")
                    else:
                        print(f"Sorry, the correct answer was {correct_answer}. Moving to the next question.")
            except ValueError:
                print("Please enter a valid number.")
        
        time.sleep(1)  # Delay before next question

multiplication_quiz()