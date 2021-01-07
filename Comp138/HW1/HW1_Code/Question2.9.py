import Non_Stationary_Bandit
import matplotlib.pyplot as plt
from datetime import datetime

start = datetime.now()
print(Non_Stationary_Bandit.f(1))
# test_values = [1/128, 1/64, 1/32, 1/16, 1/8, 1/4, 1/2, 1]
# average_results = [Non_Stationary_Bandit.f(e) for e in test_values]

print(datetime.now()-start)

# plt.xlabel('Subjects')
# plt.ylabel('Marks')

# fig, ax = plt.subplots()
# ax.set_xscale('log', basex=2)
#
#
# ax.plot(test_values, average_results)
#
# plt.show()
