from devices.mock_rf_device import MockRFDevice
import time

device = MockRFDevice()
log_path = "logs/test_log.txt"

def log_result(result):
    with open(log_path, "a") as f:
        f.write(f"{time.ctime()} | {result}\n")

def main():
    print("Starting SimuCheck...\n")
    device.power_on()
    print("Device powered on. ")
