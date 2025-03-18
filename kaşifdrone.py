from İHA import IHA

class KaşifDrone(IHA):
    def detect(self):
        if self.fly():
            print("detecting")