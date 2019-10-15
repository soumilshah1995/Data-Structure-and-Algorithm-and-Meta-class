

class Sensor(object):
    def __init__(self):
        pass

    def sensorOn(self):
        print("Sensor is on")

    def sendorOff(self):
        print("Sensor Off")


class Smoke(object):
    def __init__(self):
        pass

    def smokeOn(self):
        print("Smoke on")

    def smokeOff(self):
        print("Smoke if off")


class Lights(object):
    def __init__(self):
        pass

    def lightOn(self):
        print("Lights On")

    def LightOff(self):
        print("Lights Off")


class Meta(type):

    _instance = {}      # class Variable


    def __call__(cls, *args, **kwargs):

        """ if instance already exist dont create one  """

        if cls not in cls._instance:
            cls._instance[cls] = super(Meta, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class Facade(metaclass=Meta):

    def __init__(self):
        self._sensor = Sensor()
        self._smoke = Smoke()
        self._light = Lights()

    def Emergency(self):
        self._sensor.sensorOn()
        self._light.lightOn()
        self._smoke.smokeOn()

    def NoEmergency(self):
        self._sensor.sendorOff()
        self._light.LightOff()
        self._smoke.smokeOff()


if __name__ == "__main__":
    facade = Facade()
    print(facade)
    ob1 = Facade()
    print(ob1)
    sensor = 22

    # if sensor >60:
    #     facade.Emergency()
    # else:
    #     facade.NoEmergency()