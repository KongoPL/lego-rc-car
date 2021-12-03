import sys

sys.path.append("./classes")

CONFIG = {
    "steeringServo": {
        "pin": 15,
        "forwardPulseWidthRange": list(map(lambda x: x / 1000000, (1500, 1000))), # With instant conversion to microseconds
        "backwardPulseWidthRange": list(map(lambda x: x / 1000000, (1500, 2000))),
        "valueShift": -0.05 # Shift pulse width % value
    },
    "driveMotor": {
        "pinForward": 11,
        "pinBackward": 13
    }
}