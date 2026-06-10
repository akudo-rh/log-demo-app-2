import time
import sys

while True:
    print(f"Hello OpenShift! This is for log-demo-app-2. Current time: {time.ctime()}")
    sys.stdout.flush() # ログをすぐに送信する
    time.sleep(1800)
