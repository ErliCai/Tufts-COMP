
f = open("pdf.txt", "r")

pdf_bird = f.readline()
pdf_aircraft = f.readline()
pdf_bird = [float(i) for i in pdf_bird.split(",")]
pdf_aircraft = [float(i) for i in pdf_aircraft.split(",")]
f.close()

g = open("data.txt", "r")
objects = []
for i in range(10):
    l = g.readline().rstrip("\n").split(",")
    l = list(filter(lambda x: x != "NaN", l))
    objects.append(list(float(i) for i in l if i is not "NaN"))
    #print(i+1, ":  ", max(objects[i]) - min(objects[i]))
g.close()

tp = 0.9
for n in range(10):
    data = objects[n]
    i = data[0]
    i = int(i*2 // 1)
    b = list()
    b.append(pdf_bird[i]*0.5)
    b.append(pdf_aircraft[i]*0.5)
    b = [b[0]/(b[0]+b[1]), b[1]/(b[0]+b[1])]
    for t in range(len(data)-1):
        i = data[t+1]
        i = int(i * 2 // 1)
        b = [pdf_bird[i] *(tp*b[0] + (1-tp)*b[1]), pdf_aircraft[i] *(tp*b[1] + (1-tp)*b[0])]
        b = [b[0] / (b[0] + b[1]), b[1] / (b[0] + b[1])]

    print("Obejct ", n+1, ": ",  b)
    print("probability of being a bird is ", b[0], "and probability of being an aircraft is ", b[1])
    if b[0] > 0.5:
        print("The object should be a bird")
    else:
        print("The object should be an aircraft")
    print()






# g = open("data.txt", "r")
# objects = []
# for i in range(10):
#     l = g.readline().rstrip("\n").split(",")
#     if "NaN" in l:
#         print(i+1)
# g.close()



# a = [1,2,3,3,4]
# print(list(filter((3).__ne__, a)))
# print(a)

# g = open("data.txt", "r")
# l = g.readline()
# l = g.readline()
# l = g.readline()
# l = g.readline()
# l = g.readline()
# g.close()
#
# l = l.rstrip("\n")
# print(l)
# l = l.split(",")
# print(len(l))
#
# l = list(filter(lambda x: x != "NaN", l))
# print(l)
# print(len(l))

