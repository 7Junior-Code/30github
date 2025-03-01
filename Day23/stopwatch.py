
import time
import asciiart

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
    print(asciiart.stopwatch_l)
    """ Give Instructions """
    print("Stop key to turn stopwatch off")
    input("Any key to start: ")
    """ Call the function to turn stopwatch on"""
    stopwatch_on()