import random

# for i in range(40):
#     print(random.randint(0,10))
#
#
# a = [1,2,3,4]
# b = a.copy()
# a[1] = 3
# print(a)
# print(b)

# T = [1,2,5,8,4,6,7]
# print(sorted(T))
# print(T)
#
# def Takesecond(i):
#     return i[1]
# T2 = [[1,2],[5,6],[2,10],[12,1]]
# t2 = sorted(T2, key=Takesecond)
# print(t2[2:])

# print((-2)// (-2))
# print((2)// (-2))


# a = [1,2]
# print(a is [1,2])
# print(a == [1,2])



def turnleft(direction):
    if direction == [1, 0]:
        return [0, 1]
    if direction == [0, 1]:
        return [-1, 0]
    if direction == [-1, 0]:
        return [0, -1]
    if direction == [0, -1]:
        return [1, 0]


def turnright(direction):
    if direction == [1, 0]:
        return [0, -1]
    if direction == [0, 1]:
        return [1, 0]
    if direction == [-1, 0]:
        return [0, 1]
    if direction == [0, -1]:
        return [-1, 0]


def flr(directions):
    coords = [0, 0]
    d = [1, 0]

    for i in directions:
        if i == "L":
            d = turnleft(d)
        if i == "R":
            d = turnright(d)

        if i == "F":
            coords[0] += d[0]
            coords[1] += d[1]

    if coords[0] == 0 and coords[1] == 0:
        return 0
    elif coords[0] == 0:
        distance = abs(coords[1])
        if abs(d[0]) == 1:
            return distance + 1
        elif coords[1] * d[1] > 0:
            return distance + 2
        else:
            return distance
    elif coords[1] == 0:
        distance = abs(coords[0])
        if abs(d[1]) == 1:
            return distance + 1
        elif coords[0] * d[0] > 0:
            return distance + 2
        else:
            return distance
    else:
        distance = abs(coords[0]) + abs(coords[1])
        if d[1] == 0:
            if d[0] * coords[0] > 0:
                return distance + 1
            else:
                return distance
        else:
            if d[1] * coords[1] > 0:
                return distance + 1
            else:
                return distance


def flr(directions):
    coords = [0, 0]
    d = [1, 0]

    for i in directions:
        if i == "F":
            coords[0] += d[0]
            coords[1] += d[1]
        elif i == "R":
            d = [d[1], -d[0]]
        elif i == "L":
            d = [-d[1], d[0]]

    print(coords, d)

    if coords[0] == 0 and coords[1] == 0:
        return 0
    elif coords[1] == 0:
        return abs(coords[0]) + abs(d[1]) + ((d[0] * coords[0] / abs(coords[0]) + 1) // 2) * 2
    elif coords[0] == 0:
        return abs(coords[1]) + abs(d[0]) + ((d[1] * coords[1] / abs(coords[1]) + 1) // 2) * 2
    else:
        return (abs(coords[0]) + abs(coords[1]) +
                (1 + d[0] * coords[0] / abs(coords[0]) + d[1] * coords[1] / abs(coords[1])) / 2)


a = "  "
print(flr(a))