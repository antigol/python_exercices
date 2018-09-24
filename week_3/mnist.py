# Simplification of https://github.com/pytorch/examples/tree/master/mnist

import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import matplotlib.pyplot as plt

# check if we can use a GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Download the MNIST dataset
transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor(),  # Convert each image into a torch.FloatTensor
    torchvision.transforms.Normalize((0.1307,), (0.3081,))  # Normalize the data to have zero mean and 1 stdv
])
train_set = torchvision.datasets.MNIST('mnist_data', train=True, download=True, transform=transform)

# train_set[i] with i from 0 to len(train_set) - 1
# returns a tuple (image of a digit, integer on the image)
print("size of the 3rd image in the dataset", train_set[2][0].size())
print("class of the 3rd image in the dataset", train_set[2][1])

# visualize the 3rd image
plt.imshow(train_set[2][0].view(28, 28).numpy(), cmap="gray")
plt.show()

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        # Create one perceptron per class (the classes are the numbers from 0 to 9)
        self.pers = nn.Linear(28 ** 2, 10)

    def forward(self, x):
        x = x.view(x.size(0), -1)  # Reshape the input tensor (N, 1, 28, 28) into (N, 784)
        x = self.pers(x)
        return x


# Initialize the model
model = Net().to(device)

optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# A loader is an object that will split the dataset into batches
# We choose to create randomly (shuffle=True) batches of size 64 (batch_size=64)
loader = torch.utils.data.DataLoader(train_set, batch_size=64, shuffle=True)

# Thanks to loader to implement the magic function __iter__ we can iterate through the batches with a simple for loop
for data, target in loader:
    # data contains the digit images as a FloatTensor of shape (64, 1, 28, 28)
    # target contains the true class of the repsective images, it is a LongTensor of shape (64,)
    data, target = data.to(device), target.to(device)

    output = model(data)
    loss = F.cross_entropy(output, target)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# End of the training




# The following code tests it the model can read the digits on images from the test dataset
# The test dataset has not be used to train the network

test_set = torchvision.datasets.MNIST('data', train=False, transform=transform)

test_loss = 0
correct = 0

for data, target in torch.utils.data.DataLoader(test_set, batch_size=64):
    data, target = data.to(device), target.to(device)
    output = model(data)
    test_loss += F.cross_entropy(output, target, size_average=False).item()  # sum up batch loss
    pred = output.argmax(1)  # get the index of the max log-probability
    correct += pred.eq(target).sum().item()

test_loss /= len(test_set)

print('Test set: Average loss: {:.4f}, Accuracy: {}/{} ({:.1f}%)\n'.format(
    test_loss, correct, len(test_set),
    100. * correct / len(test_set)))
