from abc import ABC, abstractmethod

class IHA(ABC):
    def __init__(self,name, battery, gps):
        self.name = name
        self._battery = battery #protected
        self.__gps = gps  #priviate

    def get_name(self):
        print(self.name)

    def get_battery(self):
        print(self._battery)

    def get_gps(self):
        if self.__gps:
            print("gps var")

    @abstractmethod
    def arm(self):
        pass

    @abstractmethod
    def takeoff(self, height):
        pass

    @abstractmethod
    def land(self):
        pass


class KamikazeDrone(IHA):

    def arm(self):
        print("Armed on VTOL")

    def takeoff(self,height):
        print("kamikaze dont take off")

    def land(self):
        print("kamikaze dont land")

    def locking(self):
        print("drone locked")

    def execute(self):
        print("Drone started to attack")

class KeşifDrone(IHA):

    def arm(self):
        print("drone armed")
    
    def takeoff(self, height):
        print(f"kaşifdrone took of to {height} meters")

    def search(self):
        print("Kaşif Drone started to search")

    def land(self):  
        print("Keşif drone is landing safely")

class VTOL(IHA):

    def takeoff(self, height):
        print(f"vtol took of to {height} meters verticually")    

    def scanning_area(self):
        print("Scanning is started")

    def release_kamikaze(self,num_drones):
        print(f"{num_drones} Kamikaze drones were dropped")
    def land(self):
        print("VTOL is landing...")
    def arm(self):
        print("VTOL armed")


kamikaze = KamikazeDrone("kento",7,True)
kaşifdrone = KeşifDrone("kaşif",5,False)
VTOL = VTOL("Pasific",8,True)

kamikaze.get_name()
kaşifdrone.get_name()
VTOL.get_name()


kamikaze.arm()
kamikaze.execute()


kaşifdrone.takeoff(10)
kaşifdrone.search()

VTOL.takeoff(10)
VTOL.release_kamikaze(3)

kaşifdrone.get_battery()
kamikaze.get_gps()

#print(VTOL.battery)
print(VTOL.name)
print(VTOL.__gps)
