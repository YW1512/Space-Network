import space_excercise as s_e

sat1 = s_e.Satellite("sat1", 100)
sat2 = s_e.Satellite("sat2", 200)
ground_station = s_e.Earth("Houston")

msg1 = s_e.snl.Packet("Houston, we have a problem", sat1, sat2)

final_p = s_e.snl.Packet(" Hello from Earth!!", sat1, sat2)
p_earth_to_sat1 = s_e.RelayPacket(final_p, ground_station, sat1)

try:
    s_e.transmission_attempt(p_earth_to_sat1)
except:
    print("Transmission failed")
# s_e.nasa.send(msg1)