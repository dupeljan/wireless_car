import socket
import sys
from time import sleep
import numpy as np

INTERUPT = 58
from threading import Event

exit = Event()

def main():
	print("Start playing...")
    commands = np.load(sys.argv[1])
    while not exit.is_set():
		for state, delay in commands:
			print(state)
      		exit.wait(delay)

    print("All done!")
    # perform any cleanup here

def quit(signo, _frame):
    print("Interrupted by %d, shutting down" % signo)
    exit.set()

if __name__ == '__main__':

    import signal
    for sig in ('TERM', 'HUP', 'INT'):
        signal.signal(getattr(signal, 'SIG'+sig), quit);

    main()
def main():
	
		sleep(delay)
