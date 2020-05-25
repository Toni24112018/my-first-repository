def get_y(m, b, x):
    y = m*x + b
    return y
print(get_y(1, 0, 7) == 7)
print(get_y(5, 10, 3) == 25)
print("Calculating distance")
def calculate_error(m, b, point):
    x_point, y_point = point
    y = m*x_point + b
    distance = abs(y - y_point)
    return distance
print(calculate_error(1, 0, (3, 3)))
print(calculate_error(1, 0, (3, 4)))
print(calculate_error(1, -1, (3, 3)))
print(calculate_error(-1, 1, (3, 3)))
print("Calculating all error")
def calculate_all_error(m, b, points):
    total_error = 0
    for point in datapoints:
        point_error = calculate_error(m, b, point)
        total_error += point_error
    return total_error
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints))
print(calculate_all_error(1, 1, datapoints))
print(calculate_all_error(1, -1, datapoints))
print(calculate_all_error(-1, 1, datapoints))

#ls = list(range(-10, 11))
#print(ls)
#print("printing possible_ms")
possible_ms = [i * 0.1 for i in range(-100, 101)]
#print(possible_ms)

#print("printing possible_bs")
possible_bs = [i * 0.1 for i in range(-200, 201)]
#print(possible_bs)

print("Finding smallest error")

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
best_m = 0
best_b = 0
smallest_error = (float("inf"))
for m in possible_ms:
    for b in possible_bs:
      error = calculate_all_error(m, b, datapoints)
      if error < smallest_error:
          best_m = m
          best_b = b
          smallest_error = error
print(best_m, best_b, smallest_error)

print("What is the bounce height of a ball with width x = 6?") 
xy = best_m*6 + best_b
print(round(xy, 2))
    
