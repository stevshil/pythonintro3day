#!/usr/bin/env python

import time, sys

print("Entering continual loop")

while True:
    sys.stdout.write(".")
    sys.stdout.flush()
    time.sleep(2)
    sys.stdout.flush()
    