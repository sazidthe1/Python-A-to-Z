# This is Typing Test Project

from random import randint
import time

# List of sentences for typing test
sentences = [
    'The quick brown fox jumps over the lazy dog',
    'To be or not to be, that is the question',
    'Honesty is the best policy',
    'Train your mindset for success',
    'Slow and steady wins the race',
    'Create your own kind of happy'
]

# Display the sentence to be typed
print('Get ready to type this sentence: ')
sentence = sentences[randint(0, 4)]
print(sentence)

# Countdown before the typing begins
time.sleep(1)
for count in range(3, 0, -1):
    print(f"{count},", end=' ', flush=True)
    time.sleep(1)
print(' go!')

# Function to calculate words per minute (WPM)
def calculate_wpm(time, words):
    minutes = time / 60
    wpm = len(words) / minutes
    return wpm

# Record start time
start_time = time.time()

# User types the sentence
user_input = input()

# Record end time
end_time = time.time()

# Check if the typed sentence matches the original sentence
if user_input == sentence:
    # Calculate WPM if the input is correct
    words = sentence.split()
    wpm = calculate_wpm(end_time - start_time, words)
    print('Well done! Your typing speed is {:.2f} WPM.'.format(wpm))
else:
    print('Oops! The input does not match the sentence. Try again!')