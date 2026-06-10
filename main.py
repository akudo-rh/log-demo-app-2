import time
import sys

while True:
    print(f"Hello OpenShift! Current time: {time.ctime()}")
    sys.stdout.flush() # ログをすぐに送信する
    time.sleep(3600)
