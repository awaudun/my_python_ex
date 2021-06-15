import math
import numpy
g = 9.81
more = bool(True)
throw_array = numpy.array([])
while more:
    angle_d = float(input("Angle (degrees): "))
    velocity_kmh = float(input("Velocity (km/h): "))
    height = float(input("Throw height (m): "))
    throw_array = numpy.append(throw_array, [angle_d, velocity_kmh, height])
    more = input("Add more? ").lower() in {"yes", "true", "ok", "y", "yeah", "bring it on"}
print(throw_array)
for n in throw_array:
    angle_r = math.radians(throw_array[n][0]) ## angle_d
    velocity_ms = throw_array[n][1] / 3.6 ## velocity_kmh
    hor_vel = velocity_ms * math.cos(throw_array[n][0])
    ver_vel = velocity_ms * math.sin(throw_array[n][0])
    airtime = (ver_vel + math.sqrt(ver_vel*ver_vel + 2*g*throw_array[n][2])) / g ## height
    distance = hor_vel*airtime

    print(f"angle_r = {angle_r:.2f}")
    print(f"velocity_ms = {velocity_ms:.2f}")
    print(f"hor_vel = {hor_vel:.2f}")
    print(f"ver_vel = {ver_vel:.2f}")

    print(f"airtime = {airtime:.2f}")
    print(f"distance = {distance:.2f}\n")