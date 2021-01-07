import numpy as np
#
# a = np.arange(6)
# a2 = a[np.newaxis, :]
# print(a2.shape)

a = np.array([[1,2,3,4,5], [6,7,8,9,0], [1,2,3,4,4]])
a[0] = [1,3,4,5,6]
print(a)
c = np.copy(a)
print(c == a)
# print(hash(a))


b = [0] * 4 * 4
b[1] = b[3] = b[5] = 1
b[3] = 2
print(b)

print(np.zeros((6,1)))


a = [1,2,3]
print(3 > 5 and a[4] == 1 )

state = np.zeros((6, 6) , dtype=object)
print(state)