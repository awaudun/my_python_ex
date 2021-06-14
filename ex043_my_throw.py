import math

angle_d = 42##float(input("Angle (degrees): "))
velocity_kmh = 50##float(input("Velocity (km/h): "))
height = 2##float(input("Throw height (m): "))

angle_r = math.radians(angle_d)
velocity_ms = velocity_kmh / 3.6
hor_vel = velocity_ms * math.cos(angle_r)
ver_vel = velocity_ms * math.sin(angle_r)
g = 9.81
airtime = (ver_vel + math.sqrt(ver_vel*ver_vel + 2*g*height)) / g
distance = hor_vel*airtime


print(f"angle_r = {angle_r:.2f}")
print(f"velocity_ms = {velocity_ms:.2f}")
print(f"hor_vel = {hor_vel:.2f}")
print(f"ver_vel = {ver_vel:.2f}")

print(f"airtime = {airtime:.2f}")
print(f"distance = {distance:.2f}")