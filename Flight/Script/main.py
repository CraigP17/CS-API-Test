from datetime import datetime
import time
import requests

if __name__ == '__main__':
    count = 0
    while True:
        time.sleep(20)
        resp = requests.post("http://127.0.0.1:8000/set-data-from-flight",
                      json={
                          'count': count,
                          'time_sent': datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f")
                      })
        print(f"Sent: {resp.status_code}")
        count += 1
