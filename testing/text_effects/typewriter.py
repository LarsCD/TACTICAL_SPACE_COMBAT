import os
import sys
import time
# from playsound import playsound


# sound_file_path = "assets/audio/ui-click-97915.mp3"




def typingPrintFast(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        # playsound(sound_file_path)
        # very precise sleeper
        for i in range(0, 300000):
            pass


def typingInput(text, speed=1000):
    text_finish = f'{text}: '
    for character in text_finish:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(1 / speed)
    value = input()
    return value


input('To START press [ENTER]')
os.system("CLS")
name = typingInput('Enter your name')
age = typingInput('Enter your age')

report_string = f"""----------------------------------------------------
USER FILE REPORT

NAME:  {name}
AGE:   {age}

ASSIGNMENT: SECTOR-2B
OBJECTIVE:  EXTERMINATE
----------------------------------------------------"""

typingPrintFast(report_string)
input('\nTo CLOSE press [ENTER]')
