import time
import subprocess
left = 10
while left > 0:
    print(left)
    time.sleep(1)
    left -= 1
subprocess.Popen(['start', 'alarm.wav'], shell=True)
