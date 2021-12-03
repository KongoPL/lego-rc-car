from typing import Tuple
import math

from GpioManager import GpioManager


class GpioServo:
    def __init__(
        self, 
        gpioManager: GpioManager, 
        dataPin: int, 
        forwardPulseWidthRange: Tuple[float, float], 
        backwardPulseWidthRange: Tuple[float, float], 
        pulseWidthShift: float = 0
    ) -> None:
        gpioManager.setPinAsOutput(dataPin)

        self.forwardPulseWidthRange = forwardPulseWidthRange
        self.backwardPulseWidthRange = backwardPulseWidthRange
        self.pulseWidthShift = pulseWidthShift
        self.operatingFrequency = self.__calculateOperatingFrequency()

        self.pinPWM = gpioManager.setupPinForPWM(dataPin, self.operatingFrequency)

    def __calculateOperatingFrequency(self) -> int:
        maxPulseWidthTime = max(self.forwardPulseWidthRange + self.backwardPulseWidthRange)

        return math.ceil(1 / maxPulseWidthTime)

    def rotate(self, direction: float):
        pulseRange = (self.forwardPulseWidthRange if direction > 0 else self.backwardPulseWidthRange)
        pulseTime = (pulseRange[1] - pulseRange[0]) * abs(direction) + pulseRange[0]

        pulseDutyCycleWidth = round((pulseTime / (1 / self.operatingFrequency) + self.pulseWidthShift) * 100)

        # You can't send pulse with width of 100%, as servo won't know whats the signal duration
        if pulseDutyCycleWidth == 100:
            pulseDutyCycleWidth = 99

        self.pinPWM.ChangeDutyCycle(pulseDutyCycleWidth)