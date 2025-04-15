import random # to simulate variablity in signal strength

class MockRFDevice: # acts as a fake or simualted device
    def __init__(self):
        self.powered_on = False
        self.signal_strength = 0

    #simulates powering on the device - once powered on it randomly sets the signal strength between 60 and 100   
    def power_on(self):
        self.powered_on = True 
        self.signal_strength = random.randint(60, 100)
    
    #siumaltes a diagnostic test - checks if the device is on. if not it returns a failue message
    def run_diagnostics(self):
        if not self.powered_on:
            return {"status": "Fail", "reason": "device not powered on"}
        #simualte test resultes
        return {
            "status": "PASS" if self.signal_strength > 70 else "FAIL",
            "signal_strength": self.signal_strength
        }
    
    #simulates a reboot - resets device to its default state
    def reset(self):
        self.powered_on = False
        self.signal_strength = 0