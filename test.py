#
#with open('zdjecia/data.txt', 'r') as fi:
#    for line in fi:
#        pass
#    last_line = line
#last_line = line.split(".")[1]
#print(last_line)

import sys
import traceback
import time
import keyboard

i = 0
while True:

    try:
        i += 1
        print(i)
        time.sleep(1)
        keyboard.on_press_key("1", lambda _:print("You pressed 1"))

        keyboard.on_press_key("2", lambda _:print("You pressed 2"))

    except:
        break
