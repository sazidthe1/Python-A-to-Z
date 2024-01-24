# This is Typing Test Project

from random import randint
import time

sentences = [
    'The quick borwn fox jumps over the lazy dog',
    'To be or not to be, that is the question',
    'Honesty is the best policy',
    'Train your mindset for sucess',
    'Slow and steady wins the race',
    'Create your own kind of happy'
]

print('Get ready to type this sentence: ')
sentence = sentences[randint(0,4)]
print(sentence)
time.sleep(1)
print('in 3,', end=" ")
time.sleep(1)
print('2,', end=" ")
time.sleep(1)
print('1 go!')

def calculate_wpm(time, words):
    minutes = time / 60
    wpm = len(words) / minutes
    return wpm


start_time = time.time()
user_input = input()
end_time = time.time()

if user_input == sentence:
    # calculate
    words = sentence.split()
    wpm = calculate_wpm(end_time-start_time, words)
    print('Well done! Your typing speed is {:.2f} WPM.'.format(wpm))
else:
    print('Oops! The input does not match the sentence. Try again!')