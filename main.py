#!/usr/bin/env python
import time

def countdown(h, m, s):
    initial_val = h*3600 + m*60 + s
    
    while initial_val:
        time.sleep(1)
        initial_val -= 1
        minutes, seconds = divmod(initial_val, 60)
        hours, minutes = divmod(minutes, 60)
        print("{}:{}:{}".format(hours, minutes, seconds))

if __name__ == '__main__':
    countdown(0, 2, 0)
    print("Work done")
