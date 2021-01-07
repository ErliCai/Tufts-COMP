# a = [1,2,3,4,5]
# # a.reverse()
# c = a[2:]
# c.reverse()
# print(a)
# print(c)

d = {320:1, 321:0, 322:3}
a = d.pop(322)
print(a)
print(d)
print(min(d.items(), key=lambda x: x[1]))


a = [1,2,3,4,5]
print(a[:1])
print(a[1:])
print(a[:0] + a[0:])

def item_with_min_value(d):
    return min(d.items(), key=lambda x: x[1])
print(item_with_min_value(d))