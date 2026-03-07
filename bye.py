import math 
print("welcome to trigomwetric function")
print("enter the angle in degree")
#get angle from user
angle_degree=float(input("enter the angle in degrees"))
#convert degree to radians:
angle_rad=math.radians(angle_degree)
#calculate trig functtion
sin_value=math.sin(angle_rad)
cos_value=math.cos(angle_rad)
tan_value=math.tan(angle_rad)
#display the results
print(f"sin({angle_degree}°) = {sin_value:.4f}")
print(f"cos({angle_degree}°) = {cos_value:.4f}")
print(f"tan({angle_degree}°) = {tan_value:.4f}")