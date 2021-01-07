import torch
import torchvision
import torchvision.transforms as transforms
from tqdm import tqdm
from cnn import ReversiCNN

# ------------------------------------------------------------------------------
# The following code is here for testing purposes only. It is a modified copy
# of the experiment in pytorch documentation that show that ReversiCNN
# can be successfully used for image classification:
# https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html
# ------------------------------------------------------------------------------

# LOADING THE DATASET ----------------------------------------------------------

transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                        download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                          shuffle=True, num_workers=2)

testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                       download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=4,
                                         shuffle=False, num_workers=2)

# TRAINING FOR 2 EPOCHS --------------------------------------------------------

net = ReversiCNN((32, 32), [6, 10], 4, [100, 50, 10])

for epoch in range(2):  # loop over the dataset multiple times

    running_loss = 0.0
    for i, data in tqdm(enumerate(trainloader, 0)):
        # get the inputs; data is a list of [inputs, labels]
        inputs, labels = data
        labels = (labels == 0).float()
        running_loss += net.train_on_batch(inputs, labels)
        if i % 2000 == 1999:    # print every 2000 mini-batches
            print('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 2000))
            running_loss = 0.0

PATH = '../cifar_net.pth'
torch.save(net.state_dict(), PATH)
net.load_state_dict(torch.load(PATH))

# TESTING ----------------------------------------------------------------------

correct = 0
total = 0
tp = 0
fp = 0
fn = 0
tn = 0
with torch.no_grad():
    for data in testloader:
        images, labels = data
        labels = (labels == 0).numpy()
        outputs = net.evaluate(images) > 0.5
        for i in range(len(labels)):
            if labels[i] == outputs[i]:
                if labels[i]:
                    tp += 1
                else:
                    tn += 1
            elif outputs[i]:
                fp += 1
            else:
                fn += 1

precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1 = 2 * precision * recall / (precision + recall)
print("tp: %d, fp: %d, fn: %d, tn: %d, precision: %f, recall: %f, f1: %f" %
      (tp, fp, fn, tn, precision, recall, f1))
