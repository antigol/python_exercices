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
train_set = torchvision.datasets.MNIST('~/.torchvision/datasets/MNIST', train=True, download=True, transform=transform)

# train_set[i] with i from 0 to len(train_set) - 1
# returns a tuple (image of a digit, integer on the image)
print("size of the 3rd image in the dataset", train_set[2][0].shape)
print("class of the 3rd image in the dataset", train_set[2][1])

# visualize the 3rd image
plt.imshow(train_set[2][0].view(28, 28).numpy(), cmap="gray")
# plt.show()

# load all the trainset into a tensor
train_images = torch.stack([x for x, y in train_set]).to(device=device)
train_labels = torch.tensor([y for x, y in train_set], device=device)

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        # Create one perceptron per class (the classes are the numbers from 0 to 9)
        self.w = nn.Parameter(torch.empty(28 ** 2, 10))
        with torch.no_grad():
            self.w.normal_()

    def forward(self, x):
        x = x.view(x.size(0), -1)  # Reshape the input tensor (N, 1, 28, 28) into (N, 784)
        x = x @ self.w / 28
        return x


# Initialize the model
model = Net().to(device)

optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

for step in range(5000):
    idx = torch.randperm(len(train_images))[:64]
    batch_images = train_images[idx]
    batch_labels = train_labels[idx]

    output = model(batch_images)
    loss = F.cross_entropy(output, batch_labels)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print(loss.item(), end="   \r")

# End of the training




# The following code tests it the model can read the digits on images from the test dataset
# The test dataset has not be used to train the network

test_set = torchvision.datasets.MNIST('~/.torchvision/datasets/MNIST', train=False, transform=transform)

# load all the trainset into a tensor
test_images = torch.stack([x for x, y in test_set]).to(device=device)
test_labels = torch.tensor([y for x, y in test_set], device=device)

test_loss = 0
correct = 0

output = model(test_images)
test_loss = F.cross_entropy(output, test_labels).item()  # sum up batch loss
pred = output.argmax(1)  # get the index of the max log-probability
correct = pred.eq(test_labels).sum().item()

print('Test set: Average loss: {:.4f}, Accuracy: {}/{} ({:.1f}%)\n'.format(
    test_loss, correct, len(test_set),
    100. * correct / len(test_set)))
