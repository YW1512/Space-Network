import space_network_lib as snl
import time

class Satellite(snl.SpaceEntity):
    def receive_signal(self, packet: snl.Packet):
        print(f'[{self.name}] Received: {packet}')

def  transmission_attempt(packet: snl.Packet):
    while True:
        try:
            return nasa.send(packet)

        except snl.TemporalInterferenceError:
            time.sleep(2)

        except snl.DataCorruptedError:
            pass



nasa = snl.SpaceNetwork(level=2)
