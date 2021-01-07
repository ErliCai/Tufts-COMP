import numpy as np

a = np.array([[1,2,3,4],[2,3,4,5]])
b = 1
c = 1
print(a[:,1])

d = [1,2,3,4,5,5,6,6,6,7,9]
print(d.count(5))
print(d.count(8))

print(list(a[1]).count(2))

while True:
    print('cai')
    break

for i in range(10):
    if i == 4:
        continue
    print(i)