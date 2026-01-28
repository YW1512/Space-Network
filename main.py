import space_excercise as s_e

sat1 = s_e.Satellite("sat1", 100)
sat2 = s_e.Satellite("sat2", 200)

msg1 = s_e.snl.Packet("Houston, we have a problem", sat1, sat2)

try:
    s_e.transmission_attempt(msg1)

except:
    print("Transmission failed")
# s_e.nasa.send(msg1)