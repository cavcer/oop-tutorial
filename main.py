from İHA import IHA
from kamikaze import Kamikaze
from kaşifdrone import KaşifDrone
from VTOL import VTOL
from environment import Environment


kamikaze = Kamikaze("kento", 21 , True )
kaşif = KaşifDrone("kaşif", 78 , True)
vtol = VTOL("pasific", 45 , False)
drones = Environment()

def main():
    drones.add_drone(kamikaze)
    drones.add_drone(kaşif)
    drones.add_drone(vtol)


    kaşif.arm()
    kaşif.takeoff(20)
    kaşif.fly()
    kaşif.detect()

    vtol.arm()
    vtol.takeoff(21)
    vtol.fly()
    vtol.release()

    kamikaze.arm()
    kamikaze.fly()
    kamikaze.attack()

    kaşif.land()


    
main()