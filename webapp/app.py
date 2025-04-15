import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template
from devices.mock_rf_device import MockRFDevice

app = Flask(__name__)
device = MockRFDevice()
log_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logs', 'test_log.txt'))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run-test")
def run_test():
    device.power_on()
    result = device.run_diagnostics()

    # Save result to log
    with open(log_path, "a") as f:
        f.write(f"{result['status']} | Strength: {result['signal_strength']}\n")

    # Read logs
    with open(log_path, "r") as f:
        log_history = f.readlines()

    return render_template("index.html", result=result, log_history=log_history)

if __name__ == "__main__":
    app.run(debug=True)
