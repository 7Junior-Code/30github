

""" Make the following imports: """
""" For the logo of the project: """
from PIL import Image
""" Logos for other projects: """
import art
""" Time measurements are needed in this project: """
import time
""" Same for dates: """
import datetime
""" Pygame for sounds: """
import pygame

""" Loading Bar function: """
def loading():
    print("                                                     ┍-------------------------------------┑")
    print("                                                     |                                     |")
    print("                                                     ╹‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾╹")
    print("                                                     ╹ ╹ ╹ ╹ ╹ ╹     LOADING     ╹ ╹ ╹ ╹ ╹ ╹")
    time.sleep(2.4)
    print("\n"*50)
    print("                                                    ┍-------------------------------------┑")
    print("                                                    | ||||||                              |")
    print("                                                    ╹‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾╹")
    print("                                                    ╹ ╹ ╹ ╹ ╹ ╹     LOADING     ╹ ╹ ╹ ╹ ╹ ╹")
    time.sleep(3)
    print("\n"*50)
    time.sleep(.5)
    print("                                                    ┍-------------------------------------┑")
    print("                                                    | |||||||||||||||                     |")
    print("                                                    ╹‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾╹")
    print("                                                    ╹ ╹ ╹ ╹ ╹ ╹     LOADING     ╹ ╹ ╹ ╹ ╹ ╹")
    time.sleep(5.28)
    print("\n"*50)
    time.sleep(.5)
    print("                                                    ┍-------------------------------------┑")
    print("                                                    | ||||||||||||||||||||||||||          |")
    print("                                                    ╹‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾╹")
    print("                                                    ╹ ╹ ╹ ╹ ╹ ╹     LOADING     ╹ ╹ ╹ ╹ ╹ ╹")
    time.sleep(4.39)
    print("\n"*50)
    time.sleep(.5)
    print("                                                    ┍-------------------------------------┑")
    print("                                                    | ||||||||||||||||||||||||||||||||    |")
    print("                                                    ╹‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾╹")
    print("                                                    ╹ ╹ ╹ ╹ ╹ ╹     LOADING     ╹ ╹ ╹ ╹ ╹ ╹")
    time.sleep(6.25)
    print("\n"*50)
    time.sleep(.5)
    print("                                                    ┍-------------------------------------┑")
    print("                                                    | ||||||||||||||||||||||||||||||||||| |")
    print("                                                    ╹‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾╹")
    print("                                                    ╹ ╹ ╹ ╹ ╹ ╹     LOADING     ╹ ╹ ╹ ╹ ╹ ╹")
    time.sleep(3)
    print("\n"*50)
    time.sleep(1)
""" Section Functions: """
def alarm():
    def set_alarm(alarm_time):
        print(f"Alarm set for {alarm_time}")
        sound_file = "MorningGlory.mp3"
        is_running = True

        while is_running:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time)
            if current_time == alarm_time:
                print("😴WAKE UP!🧑🏻‍💻")

                pygame.mixer.init()
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    time.sleep(1)

                is_running = False
            time.sleep(1)

    if __name__ == '__main__':
        print(art.sand_clock)
        alarm_time = input("Enter the alarm time (HH:MM:SS): ")
        if len(alarm_time) == 8:
            set_alarm(alarm_time)

        else:
            while not len(alarm_time) == 8:
                print("Should consist of 8 symbols (HH:MM:SS)")
                alarm_time = input("Enter the alarm time (HH:MM:SS): ")
            set_alarm(alarm_time)

def timer():
    def set_timer(timer_time):
        s = timer_time % 60
        m = int(timer_time / 60) % 60
        h = int(timer_time / 3600)
        print(f"Timer set for ({h:02}:{m:02}:{s:02})")
        sound_file = "MorningGlory.mp3"
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        for x in range(timer_time, 0, -1):
            sec = x % 60
            min = int(x / 60) % 60
            hour = int(x / 3600)
            if x == 1:
                print("\n" * 50,
                      "                                                                00  :  00  :  01")
                time.sleep(1)
                print(
                    "\n \n \n \n \n                                                                  😴TIME IS UP!🧑🏻‍💻")
                print(
                    f"                                                                It's {current_time} now. \n \n \n \n \n")
                pygame.mixer.init()
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            else:
                print("\n" * 50,
                      f"                                                                {hour:02}  :  {min:02}  :  {sec:02}")
                time.sleep(1)

    if __name__ == '__main__':
        print(art.sand_clock)
        print("         Welcome to Junior Timer ")
        try:
            timer_time = int(input("   Enter the time for your countdown timer in seconds: "))
        except ValueError:
            print("\n \n                             ERROR 406\n        Message unrecognized")
            timer_time = int(input("   Enter the time for your countdown timer in seconds: "))
        finally:
            set_timer(timer_time)

def stopwatch():
    """ Function to be used for later"""

    def stopwatch_on():
        z = 0
        o = 0
        is_running = True

        while is_running:
            z += (o + .01)
            try:
                time.sleep(.01)
            except KeyboardInterrupt:
                print(f"\n                                                                Time:{z:.2f}")
                is_running = False
            if len(str(z)) == 5:
                o += 1
                float(z)
            else:
                float(z)

    """ Program starts here: """
    if __name__ == '__main__':
        """ Print the logo first"""
        print(art.stopwatch_l)
        """ Give Instructions """
        print("Stop key to turn stopwatch off")
        input("Any key to start: ")
        """ Call the function to turn stopwatch on"""
        stopwatch_on()

def local_time():
    def clock():
        keep_running = True
        while keep_running:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print("\n" * 50,
                  f"                                                                          {current_time}")
            time.sleep(1)

    if __name__ == '__main__':
        print(art.sand_clock)
        input("Any key to Start Timer: ")
        clock()

    def sleep(param):
        return None
""" Calling Loading Bar """
loading()

""" Instructions """
print("The logo will pop out move it to the right!")
time.sleep(5)
print("\n"*50)

""" Logo will be shown in a window"""
image = "Earth_Hour.jpeg"
logo = Image.open(image)
logo.show()

""" Ask the user for entering a specific section """
print(" Sections: \n"
               "Alarm   Timer   Stopwatch   Local time")
option = input(" (A)     (B)       (C)          (D): \n              ").upper()

if option == "A":
    """"""
    alarm()
elif option == "B":
    timer()
elif option == "C":
    stopwatch()
elif option == "D":
    local_time()
else:
    print("Error")

