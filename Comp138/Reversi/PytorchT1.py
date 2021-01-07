from __future__ import print_function
import torch

# x = torch.empty(5, 3)
# print(x)

x = torch.rand(5,3)
x = torch.zeros(5,3,dtype = torch.int)
x = torch.tensor([5.5,3])
print(x)
print(x.size())
