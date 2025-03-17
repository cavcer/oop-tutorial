class IHA:
    def __init__(self,name):
        self.name = name

    def get_name(self):
        print(self.name)
        
    def arm(self):
        print("Drone armed.")

    def takeoff(self, height):
        print(f"Take-off started to {height} meters.")

    def land(self):
        print("Landing started.")

    def disarm(self):
        print("Drone disarmed.")


class KamikazeDrone(IHA):

    def locking(self):
        print("drone locked")

    def execute(self):
        print("Drone started to attack")

class KeşifDrone(IHA):

    def search(self):
        print("Kaşif Drone started to search")

class VTOL(IHA):

    def scanning_area(self):
        print("Scanning is started")

    def release_kamikaze(self,num_drones):
        print(f"{num_drones} Kamikaze drones were dropped")

normal_drone = IHA("drone")
kamikaze = KamikazeDrone("kento")
kaşifdrone = KeşifDrone("kaşif")
VTOL = VTOL("Pasific")

print(kamikaze.name)
print(kaşifdrone.name)

kamikaze.arm()
kamikaze.execute()


kaşifdrone.disarm()
kaşifdrone.search()

VTOL.takeoff(10)
VTOL.release_kamikaze(3)
    



