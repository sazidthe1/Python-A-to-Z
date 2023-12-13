# This is a Coin Flip Streaks Project

import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values
    flips = ['H' if random.randint(0, 1) == 0 else 'T' for _ in range(100)]

    # Code that checks if there is a streak of 6 heads or tails in a row
    flips_str = ''.join(flips)
    if 'HHHHHH' in flips_str or 'TTTTTT' in flips_str:
        numberOfStreaks += 1

print(f'Chance of streak: {numberOfStreaks / 100:.2f}%')