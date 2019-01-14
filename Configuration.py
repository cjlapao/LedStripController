import json
import io
import os
from LedStrip import LedStrip
from LightSensor import LightSensor
from MotionSensor import MotionSensor
from Colors import Colors

class Configuration(object):

    def __init__(self, *args, **kwargs):
        self.__items = object
        self.__ledStrips = []
        self.__lightSensor = LightSensor
        self.__motionSensor = MotionSensor
        self.__colors = Colors()
        self.loadSettings()

    def loadSettings(self):
        exist = os.path.isfile("settings.json")
        if exist:
            with open("settings.json") as f:
                self.__items = json.load(f)
                if "ledStrips" in self.__items:
                    ledStripsLen = len(self.__items["ledStrips"])
                    if (ledStripsLen > 0):
                        for ledStrip in self.__items["ledStrips"]:
                            led = LedStrip(ledStrip["redPin"],ledStrip["greenPin"],ledStrip["bluePin"])
                            led.name = str(ledStrip["name"])
                            led.setColor(ledStrip["currentColor"])
                            led.intensity = (ledStrip["currentIntensity"])                                    
                            self.__ledStrips.append(led)
                    print("Ledstrip settings loaded...")
                if "lightSensor" in self.__items:
                    self.__lightSensor = LightSensor(int(self.__items["lightSensor"]["pin"]))
                    print("Light sensor settings loaded")
                if "motionSensor" in self.__items:
                    self.__motionSensor = MotionSensor(int(self.__items["motionSensor"]["pin"]))
                    self.__motionSensor.movementThreshold = int(self.__items["motionSensor"]["movementThreshold"])
                    self.__motionSensor.readingDelay = int(self.__items["motionSensor"]["readingDelay"])
                    print("motion sensor settings loaded")
    
    def getColor(self, name):
        for color in self.__colors.items:
            if color.name.lower() == name:
                return color.web
        return None

    def __getLedstripCount(self):
        return len(self.__ledStrips)

    def _get_items(self):
        return self.__items
    
    def _set_items(self, value):
        self.__items = value 
    
    def _get_lightSensor(self):
        return self.__lightSensor
    
    def _set_lightSensor(self, value):
        self.__lightSensor = value
    
    def _get_LedStrips(self):
        return self.__ledStrips
    
    def _set_ledStrips(self, value):
        self.__ledStrips = value

    def __get_colors(self):
        return self.__colors
    
    def __set_colors(self, value):
        self.__colors = value

    def  __getMotionSensor(self):
        return self.__motionSensor
   
    def printLedStrips(self):
        for ledStrip in self.__ledStrips:
            print("name: " + ledStrip.name)
    
    ledStripsCount = property(__getLedstripCount)

    items = property(_get_items, _set_items)

    ledStrips = property(_get_LedStrips, _set_ledStrips)

    lightSensor = property(_get_lightSensor, _set_lightSensor, type(LightSensor))

    colors = property(__get_colors, __set_colors)

    motionSensor = property(__getMotionSensor)