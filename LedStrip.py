import RPi.GPIO as GPIO
import time
from Color import Color

class LedStrip(object):
    
    def __init__(self, red, green, blue):
        self.__defaultMhz = 100
        self.__redPin = red
        self.__greenPin = green
        self.__bluePin = blue

        self.__redPinValue = 0
        self.__greenPinValue = 0
        self.__bluePinValue = 0
        self.__intensity = 100
        self.__name = "none"

        self.__pwmR = None
        self.__pwmG = None
        self.__pwmB = None

        self.__steps = 50
        self.__duration = 2

        self.setupGPIO()
    
    def setupGPIO(self):
        print("Setting up Rpi GPIO")
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        GPIO.setup(self.redPin, GPIO.OUT)
        GPIO.setup(self.greenPin, GPIO.OUT)
        GPIO.setup(self.bluePin, GPIO.OUT)        
        
        self.__pwmR = GPIO.PWM(self.redPin, self.__defaultMhz)
        self.__pwmG = GPIO.PWM(self.greenPin, self.__defaultMhz)
        self.__pwmB = GPIO.PWM(self.bluePin, self.__defaultMhz)

        self.__startPWM()
        
        print("GPIO setup finished...")

    def __startPWM(self):
        self.__pwmR.start(0)
        self.__pwmG.start(0)
        self.__pwmB.start(0)
        print("GPIO PWM started")
    
    def __stopPWM(self):
        #GPIO.cleanup()
        self.__pwmR.stop()
        self.__pwmG.stop()
        self.__pwmB.stop()
        print("GPIO PWM stopped...")

    def __restartPWM(self):
        self.__stopPWM()
        self.__startPWM()

    def setColor(self, name, intensity = 100):
        self.__restartPWM()
        color = Color()        
        color.fromHex(name)
        self.redPinValue = color.red
        self.greenPinValue = color.green
        self.bluePinValue = color.blue
        redPwm = self.redPinValue / float(255)
        greenPwm = self.greenPinValue / float(255)
        bluePwm = self.bluePinValue / float(255)
        self.__pwmR.ChangeDutyCycle(redPwm * intensity)
        self.__pwmG.ChangeDutyCycle(greenPwm * intensity)
        self.__pwmB.ChangeDutyCycle(bluePwm * intensity)
        print("LedStrip color updated...")

    def setIntensity(self, intensity):
        redPwm = self.redPinValue / float(255)
        greenPwm = self.greenPinValue / float(255)
        bluePwm = self.bluePinValue / float(255)
        self.__pwmR.ChangeDutyCycle(redPwm * intensity)
        self.__pwmG.ChangeDutyCycle(greenPwm * intensity)
        self.__pwmB.ChangeDutyCycle(bluePwm * intensity)
        print("LedStrip color intensity updated...")

    def close(self):
        self.__stopPWM()
    
    def fadeOut(self):
        count = 0
        intensity = self.__intensity
        stepSize = self.__intensity / self.__steps
        while count < self.__steps:
            count += 1
            intensity = intensity - stepSize
            self.setIntensity(intensity)
            time.sleep(self.__steps / self.__duration / float(1000))

    def fadeIn(self):
        count = 0
        intensity = 0
        self.setIntensity(100)
        stepSize = self.__intensity / self.__steps
        while count < self.__steps:
            count += 1
            intensity = intensity + stepSize
            self.setIntensity(intensity)
            time.sleep(self.__steps / self.__duration / float(1000))

    def __getname(self):
        return self.__name

    def __setname(self, name):
        self.__name = name + "Settted"

    def __getredPin(self):
        return self.__redPin
    
    def __setredPin(self, value):
        self.__redPin = value
        GPIO.setup(value, GPIO.OUT)
        GPIO.output(value, GPIO.LOW)
    
    def _get_greenPin(self):
        return self.__greenPin
    
    def _set_greenPin(self, value):
        self.__greenPin = value
        GPIO.setup(value, GPIO.OUT)
        GPIO.output(value, GPIO.LOW)
    
    def _get_bluePin(self):
        return self.__bluePin
    
    def _set_bluePin(self, value):
        self.__bluePin = value
        GPIO.setup(value, GPIO.OUT)
        GPIO.output(value, GPIO.LOW)

    def __getredPinValue(self):
        return self.__redPinValue
    
    def __setredPinValue(self, value):
        self.__redPinValue = value

    def _get_greenPinValue(self):
        return self.__greenPinValue
    
    def _set_greenPinValue(self, value):
        self.__greenPinValue = value

    def _get_bluePinValue(self):
        return self.__bluePinValue
    
    def _set_bluePinValue(self, value):
        self.__bluePinValue = value
    
    def __getIntensity(self):
        return self.__intensity

    def __setIntensity(self, value):
        self.__intensity = value
    
    def __getDuration(self):
        return self.__duration
    
    def __setDuration(self, value):
        self.__duration = value

    def __getSteps(self):
        return self.__steps
    
    def __setSteps(self, value):
        self.__steps = value

    name = property(__getname, __setname)

    redPin = property(__getredPin, __setredPin)

    redPinValue = property(__getredPinValue, __setredPinValue)

    greenPin = property(_get_greenPin, _set_greenPin)

    greenPinValue = property(_get_greenPinValue, _set_greenPinValue)

    bluePin = property(_get_bluePin, _set_bluePin)

    bluePinValue = property(_get_bluePinValue, _set_bluePinValue)

    duration = property(__getDuration, __setDuration)

    intensity = property(__getIntensity, __setIntensity)

    steps = property(__getSteps, __setSteps)