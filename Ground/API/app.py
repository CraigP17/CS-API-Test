import requests
from flask import Flask, render_template, redirect
from datetime import datetime


app = Flask(__name__)
FLIGHT_IP = "127.0.0.1:8000"


class Count:
    def __init__(self):
        self.count = 0

    def get_count(self):
        return self.count

    def increase_count(self):
        self.count += 1


counter = Count()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! - Ground'


@app.route('/get-data-from-flight', methods=['GET'])
def get_data_from_flight():
    response = requests.get(f"http://{FLIGHT_IP}/get-data")
    data_received = response.json()
    return render_template('home.html', data=data_received)


@app.route('/send-data-to-flight', methods=['POST'])
def send_data_to_flight():
    json_data = {
        "count": counter.get_count(),
        "time_sent": datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f")
    }
    requests.post(f"http://{FLIGHT_IP}/set-data-from-ground", json=json_data)
    counter.increase_count()
    return redirect('/get-data-from-flight')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
