
import time
import sys
sys.stdout.flush()

print("|    |", end = "")
time.sleep(1)

print("|>   |", end = "", flush=True)
time.sleep(1)

print("|=>  |", flush = True, end = "")
time.sleep(1)
flush = True
print("|==> |")
time.sleep(1)
flush = True
print("|===>|")
time.sleep(1)
flush = True
print("|====|")
time.sleep(1)
print("Done!")
