# 1. Format function 
def format_number(num, format_type):
    result = format(num, format_type)
    return result

formatted = format_number(145, 'o')
#print("Formatted result:", formatted) 

# 2 . Pond area and water capacity
r = 84
pi = 3.14
Area = pi*r**2
#print("Area is:", Area)
water = 1.4*Area
#print("water capacity in the pond:", int(water))

# 3.Speed Distance
distance = 490
time_seconds = 7 * 60

speed_mps = distance / time_seconds

print("Speed (m/s):", int(speed_mps))