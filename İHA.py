from abc import ABC, abstractmethod

class IHA:

    def __init__(self, name, battery, gps, altitude):
        self.name = name
        self.__battery = battery
        self.__gps = gps
        self.altitude = altitude

    def get_name(self):
        print(self.name)

    def get_battery(self):
        return self.__battery

    def get_gps(self):
        return self.__gps

    def arm(self, battery, gps):
        battery = self.get_battery
        gps = self.get_gps

        if battery >= 22 and gps:
            print("Drone armed")
            return True
        else:
            print("drone couldnt arm")
            return False

    def takeoff(self, arm, height):
        arm = self.arm()
        if arm:
            print(f"Take off started to {height} meters")
            return True
        else:
            print("there is a problem")
            return False

    def fly(self, takeoff):
        takeoff = self.takeoff
        if takeoff:
            print(("drone is flying"))
            return True
        else:
            print("i am on land")
            return False
        
    def land(self, fly):
        fly = self.fly()
        if fly:
            print("landing started")
            return True
        else:
            print("what")
            return False
        
    def disarm(self,land):
        land = self.land()
        if land:
            print("drone disarmed")



    

    


    
