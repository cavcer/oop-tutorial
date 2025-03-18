class Environment:

    def __init__(self):
        self.drone_list = []

    def add_drone(self, drone):
        self.drone_list.append(drone)
        print("drone added")

    def list_drones(self):
        print("Active İHAs:")
        for drone in self.drone_list:
            print("ben dronum") 

   




