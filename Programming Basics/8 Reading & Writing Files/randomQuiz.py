# This is Generating Random Quiz Files Project

import random

# Define the states and their capitals
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
   'New Mexico': 'Santa Fe', 'New York': 'Albany','North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 different quizzes
for quiz_num in range(1, 36):
    # Create quiz and answer key files
    quiz_file = open(f'quiz{quiz_num}.txt', 'w')
    answer_key_file = open(f'quiz{quiz_num}_answers.txt', 'w')

    # Write the header for the quiz
    quiz_file.write(f'Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write(f'State Capitals Quiz #{quiz_num}\n\n')

    # Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    # Generate 50 multiple-choice questions
    for question_num in range(1, 51):
        # Get the correct and wrong answers
        correct_answer = capitals[states[question_num - 1]]
        wrong_answers = list(capitals.values())
        wrong_answers.remove(correct_answer)
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = [correct_answer] + wrong_answers
        random.shuffle(answer_options)

        # Write the question and answer options to the quiz file
        quiz_file.write(f'{question_num}. What is the capital of {states[question_num - 1]}?\n')
        for i in range(4):
            quiz_file.write(f"    {'ABCD'[i]}. {answer_options[i]}\n")
        quiz_file.write('\n')

        # Write the answer key to the answer key file
        answer_key_file.write(f"{question_num}. {'ABCD'[answer_options.index(correct_answer)]}\n")

    # Close the quiz and answer key files
    quiz_file.close()
    answer_key_file.close()