
import asciiart
import datetime
import time

def clock():
    keep_running = True
    while keep_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("\n" * 50,
        f"                                                                          {current_time}")
        time.sleep(1)


if __name__ == '__main__':
    print(asciiart.sand_clock)
    input("Any key to Start Timer: ")
    clock()

