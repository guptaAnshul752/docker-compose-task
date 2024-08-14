# Flask code for running a local host server with metrics displayed on /metrics endpoint

import os
import time
from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/metrics')
def get_metrics():
    metrics = {
        'cpu_percent': psutil.cpu_percent(interval=1),
        'memory_percent': psutil.virtual_memory().percent
        }
    return jsonify(metrics)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

