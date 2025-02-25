
import asciiart
import time
import datetime
import pygame

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
            print("\n"*50,
                  "                                                                00  :  00  :  01")
            time.sleep(1)
            print("\n \n \n \n \n                                                                  😴TIME IS UP!🧑🏻‍💻")
            print(f"                                                                It's {current_time} now. \n \n \n \n \n")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
        else:
            print("\n"*50,
                  f"                                                                {hour:02}  :  {min:02}  :  {sec:02}")
            time.sleep(1)

if __name__ == '__main__':
    print(asciiart.sand_clock)
    print("         Welcome to Junior Timer ")
    try:
        timer_time = int(input("   Enter the time for your countdown timer in seconds: "))
    except ValueError:
        print("\n \n                             ERROR 406\n        Message unrecognized")
        timer_time = int(input("   Enter the time for your countdown timer in seconds: "))
    finally:
        set_timer(timer_time)