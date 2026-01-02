import threading
import time
import itertools
import sys
from speak import speak
from wish import wishMe
# --------- Loading Animation -----------
def show_loading_animation(flag):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if flag[0]:  # stop when flag is set True
            break
        sys.stdout.write('\r🧠 Starting Jarvis... ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r✅ Jarvis is ready!        \n')

# --------- Use This Instead of wishMe() Directly -----------
def start_with_loading():
    stop_flag = [False]  # shared flag
    t = threading.Thread(target=show_loading_animation, args=(stop_flag,))
    t.start()

    # Now let Jarvis speak greeting
    speak(wishMe())  # or call wishMe() here

    stop_flag[0] = True
    t.join()  # wait for animation thread to stop

# --------- Replace wishMe() with ---------
start_with_loading()
