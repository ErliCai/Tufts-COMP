
f = open("pdf.txt", "r")

pdf_bird = f.readline()
pdf_aircraft = f.readline()
pdf_bird = [float(i) for i in pdf_bird.split(",")]
pdf_aircraft = [float(i) for i in pdf_aircraft.split(",")]
f.close()

print("Difference between maximum speed and minimum speed:")
g = open("data.txt", "r")
objects = []
for i in range(10):
    l = g.readline().rstrip("\n").split(",")
    l = list(filter(lambda x: x != "NaN", l))
    objects.append(list(float(i) for i in l if i is not "NaN"))
    print(i+1, ":  ", max(objects[i]) - min(objects[i]))
g.close()


# printing out the difference between maximum speed and minimum speed for each object,
# we see that all birds have a large difference while all aircraft (except Object 8) has a small difference

# I think this is because the aircraft will need to sustain a speed to reduce the turbulence
# while birds might

# So the extra feature I am going to use is the difference between maximum speed and minimum speed
# We keep track of the difference
# If difference is less than 5,
# we give it a larger probability to transition from bird to airplane and from airplane to airplane
# Abd if difference is less than 5,
# we give it a smaller probability to transition from bird to airplane and from airplane to airplane



for n in range(10):
    data = objects[n]
    i = data[0]
    i = int(i*2 // 1)
    b = list()
    b.append(pdf_bird[i]*0.5)
    b.append(pdf_aircraft[i]*0.5)
    b = [b[0]/(b[0]+b[1]), b[1]/(b[0]+b[1])]
    max_difference = 0
    for t in range(len(data)-1):
        max_difference = max(max_difference, data[t+1]-data[t])
        i = data[t+1]
        i = int(i * 2 // 1)
        if max_difference < 5:
            tp = 0.1
        else:
            tp = 0.9
        b = [pdf_bird[i] * (tp*b[0] + tp*b[1]), pdf_aircraft[i] * ((1-tp)*b[1] + (1-tp)*b[0])]
        b = [b[0] / (b[0] + b[1]), b[1] / (b[0] + b[1])]

    print("Obejct ", n+1, ": ",  b)
    print("probability of being a bird is ", b[0], "and probability of being an aircraft is ", b[1])
    if b[0] > 0.5:
        print("The object should be a bird")
    else:
        print("The object should be an aircraft")
    print()

