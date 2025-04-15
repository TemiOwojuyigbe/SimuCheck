from devices.mock_rf_device import MockRFDevice
import time #timestop logs 

device = MockRFDevice()
log_path = "logs/test_log.txt" #defines the path of my log file where the test results will be saved

#Replicates how automated test equipemtn logs diagnositics to a file for review or auditing - function logs test results to test_log.txt wiith the current timestamp
def log_result(result):
    with open(log_path, "a") as f:
        f.write(f"{time.ctime()} | {result}\n")

def main():
    print("Starting SimuCheck...\n")
    device.power_on()
    print("Device powered on. ")

    result = device.run_diagnostics()
    print("Running diagnostics...")
    
    #analyzes the diagnostic result
    if result["status"] == "PASS":
        print("Test Passed")
    else:
        print(f"Test Failed - {result.get('reason', 'Signal too weak')}")

    log_result(result)

if __name__ == "__main__":
    main()