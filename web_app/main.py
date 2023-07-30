from flask import Flask
import socket
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_timestamp_and_hostname():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    hostname = socket.gethostname()
    return f"Timestamp: {timestamp}\nHostname: {hostname}\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
