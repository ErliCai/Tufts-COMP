import random
import json

speed1 = [4,3]
speed2 = [3,4]
speed3 = [4,1]
position = [0,0]

def Euclidedan_distance(a,b):
    return ((a[0]-b[0])**2 +(a[1]-b[1])**2 ) ** 0.5

def trajectory(s, p):
    trajectory_from_p = []
    for i in range(1, 1 + s[0]):
        vertical_displacement = i * s[1] / s[0]

        if (i * s[1]) % s[0] == 0:
            trajectory_from_p.append([p[0]+i, p[1]+int(vertical_displacement)])
        else:
            trajectory_from_p.append([p[0]+i-1, p[1]+int(vertical_displacement)])
            trajectory_from_p.append([p[0]+i, p[1]+int(vertical_displacement)])

    for i in range(1, 1 + s[1]):
        horizontal_displacement = i * s[0] / s[1]

        if (i * s[0]) % s[1] != 0:
            if [int(p[0]+horizontal_displacement), p[1]+i] not in trajectory_from_p:
                trajectory_from_p.append([int(p[0]+horizontal_displacement), p[1]+i])
            if [int(p[0] + horizontal_displacement), p[1]+i-1] not in trajectory_from_p:
                trajectory_from_p.append([int(p[0]+horizontal_displacement), p[1]+i-1])

    trajectory_from_p.sort(key=lambda x:((x[0]-p[0])**2 +(x[1]-p[1])**2 ) ** 0.5)
    return trajectory_from_p



# print(Euclidedan_distance(position,speed1))
# print(trajectory(speed1, position))
# print(trajectory(speed2, position))
# print(trajectory(speed3, position))
# print (4 > 3 > 2)

# print(random.randrange(2))
# s = [[1,2],1,2,3,4]
# d = {repr(s): 'value'}
# print(d[repr(s)])
# print(d)
# print(random.choice(s))
# print(random.random())

# a = '[123,4,[45,2,3]]'
# print(json.loads(a)[2])

# probs = [0.1, 0.25, 0.6, 0.05]
# r = random.random()
# index = 0
# while(r >= 0 and index < len(probs)):
#   r -= probs[index]
#   index += 1
# print(index-1)