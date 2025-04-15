import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template
from devices.mock_rf_device import MockRFDevice

app = Flask(__name__)
device = MockRFDevice()

@app.route("/")

def home():
    device.power_on()
    result = device.run_diagnostics()
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)