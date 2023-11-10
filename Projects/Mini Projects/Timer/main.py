# Importing the 'time' module for handling time-related functions
import time

# Taking user input for the time duration in seconds
my_time = int(input('Enter the time in seconds: '))

# Looping through the countdown from the user-provided time to 1 (inclusive)
for x in range(my_time, 0, -1):
  # Calculating remaining seconds, minutes, and hours
  seconds = x % 60
  minutes = int(x / 60) % 60
  hours = int(x / 3600)
  
  # Displaying the formatted countdown in HH:MM:SS format
  print(f'{hours:02}:{minutes:02}:{seconds:02}')

  # Pausing the execution for 1 second to create the countdown effect
  time.sleep(1)

# Displaying a message when the countdown reaches zero
print("Time's Up!")