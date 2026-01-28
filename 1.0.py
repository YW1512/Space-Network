import space_network_lib as snl


class Satellite(snl.SpaceEntity):
    def __init__(self, name, distance_from_earth):
        super().__init__(name, distance_from_earth)


    def receive_signal(self, packet: snl.Packet):
        print(f'[{self.name}] Received: {packet}')


nasa = snl.SpaceNetwork(level=1)

sat1 = Satellite("sat1", 100)
sat2 = Satellite("sat2", 200)

msg1 = snl.Packet("Houston, we have a problem", sat1, sat2)

nasa.send(msg1)