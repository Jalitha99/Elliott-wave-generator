import csv
import random
import matplotlib.pyplot as plt

# Specify the file name
file_name = "output.csv"

# Read the 2D array from the CSV file
with open(file_name, mode='r', newline='') as file:
    reader = csv.reader(file)
    data = [list(map(float, row)) for row in reader]

# Get 10 random arrays
random_arrays = random.sample(data, 10)

# Create subplots for the 10 arrays
fig, axes = plt.subplots(2, 5, figsize=(15, 7))
fig.suptitle("Randomly Selected Arrays")

for i, array in enumerate(random_arrays):
    ax = axes[i // 5, i % 5]
    ax.plot(array)
    ax.set_title(f"Array {i + 1}")
    ax.set_xlabel('X-Axis')
    ax.set_ylabel('Y-Axis')

plt.tight_layout()
plt.show()
