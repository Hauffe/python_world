import numpy as np
import threading

days = 13
with open('adventofcode/day_6/input.txt') as f:
    fishes = [int(n) for n in f.readline().split(',')]
    print(fishes)

def change_state(days, fishes):
    for _ in range(days):
        for timer in range(len(fishes)):
            if fishes[timer] == 0:
                fishes[timer] = 6
                fishes.append(8)
            else:
                fishes[timer] -=1
        print(f'{fishes}')

change_state(days, fishes)
