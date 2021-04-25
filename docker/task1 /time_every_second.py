from datetime import datetime
from time import sleep
import sys


while True:
    sys.stdout.write(f"{datetime.now()}\n")
    sleep(1)
