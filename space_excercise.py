import space_network_lib as snl
import time

class BrokenConnectionError(snl.CommsError):
    pass
class Satellite(snl.SpaceEntity):
    def receive_signal(self, packet: snl.Packet):
        print(f'[{self.name}] Received: {packet}')

def  transmission_attempt(packet: snl.Packet):
    while True:
        try:
            return nasa.send(packet)

        except snl.TemporalInterferenceError:
            print("Interference, waiting...")
            time.sleep(2)

        except snl.DataCorruptedError:
            continue

        except snl.LinkTerminatedError:
            print("Link lost")
            raise BrokenConnectionError("Don't try again!")

        except snl.OutOfRangeError:
            print("Target out of range")
            raise BrokenConnectionError("Don't try again!")


nasa = snl.SpaceNetwork(level=3)
