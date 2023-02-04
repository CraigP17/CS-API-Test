from flask import Flask, request
from collections import deque
from datetime import datetime


GROUND_IP = "127.0.0.1:5000"

app = Flask(__name__)

ground_data = deque(maxlen=10)
flight_data = deque(maxlen=10)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! - Flight'


@app.route('/get-data')
def get_data():
    return {
        "ground-data": [g for g in ground_data],
        "flight-data": [f for f in flight_data]
    }


@app.route('/set-data-from-ground', methods=['POST'])
def set_data_from_ground():
    json_resp = request.get_json()
    time_sent = json_resp["time_sent"] if "time_sent" in json_resp else None
    count = json_resp["count"] if "count" in json_resp else None
    ground_data.append({
        'count': count,
        'time_sent_from_ground': time_sent,
        'time_received_on_flight_api':
            datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f")
    })
    return "Received"


@app.route('/set-data-from-flight', methods=['POST'])
def set_data_from_flight():
    json_resp = request.get_json()
    time_sent = json_resp["time_sent"] if "time_sent" in json_resp else None
    count = json_resp["count"] if "count" in json_resp else None
    flight_data.append({
        'count': count,
        'time_created_from_script': time_sent,
        'time_received_on_flight_api':
            datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f")
    })
    return "Received"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
