import space_network_lib as snl
import time


class RelayPacket(snl.Packet):
    def __init__(self, packet_to_relay, sender, proxy):
        super().__init__(data = packet_to_relay, sender = sender, receiver = proxy)


    def __repr__(self):
        return f'RelayPacket(Relaying[{self.data}] to {self.receiver} from {self.sender})'


class BrokenConnectionError(snl.CommsError):
    pass


class Earth(snl.SpaceEntity):
    def __init__(self, name):
        super().__init__(name = name, distance_from_earth = 0)

    def receive_signal(self, packet):
        print(f"[{self.name}] Signal received (. .. ...).")



class Satellite(snl.SpaceEntity):
    def receive_signal(self, packet: snl.Packet):
        if isinstance(packet, RelayPacket):
            inner_packet = packet.data
            print(self.name, f"Unwrapping and forwarding to {inner_packet.receiver}")
            transmission_attempt(inner_packet)
        else:
            print(self.name, f"Final destination reached: {packet.data}")


def transmission_attempt(packet: snl.Packet):
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


nasa = snl.SpaceNetwork(level=5)
