from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def show_device(self, name):
        print('Device name', name)
    

    @abstractmethod
    def turn_on(self):
        pass


class SmartTV(SmartDevice):
    def turn_on(self):
        print('Smart tv is now ON')


class SmartLights(SmartDevice):
    def turn_on(self):
        print('All the lights in the house are now ON')


class SmartStove(SmartDevice):
    def turn_on(self):
        print('The Smart stove is now ON')


tv = SmartTV()
lights = SmartLights()
stove = SmartStove()

tv.show_device('Living Room TV')
tv.turn_on()

lights.show_device('Lights')
lights.turn_on()

stove.show_device('The cooking stove')
stove.turn_on()


class SecurityCam:
    def check_status(self):
        print('The security cam is now watching the Smart Stove')


class DoorLock:
    def check_status(self):
        print('The door lock is secure and locked')


devices = [SecurityCam(), DoorLock()]
 
print("")
print("===== SMART DEVICE STATUS =====")
 
for device in devices:
    device.check_status()
 
print("===============================")


# I am sorry about the last project i will try to fix it and i can not re post it on codingal but it will update on github so please check there mrs thank you
