import numpy as np

image = np.array([
    [100, 105, 110, 115],
    [102, 250, 108, 112],
    [98, 103, 107, 111],
    [95, 100, 105, 110]
], dtype=float)

updated = image.copy()

rows, cols = image.shape

for i in range(rows):
    for j in range(cols):

        neighbors = []

        if i > 0:
            neighbors.append(image[i - 1][j])

        if i < rows - 1:
            neighbors.append(image[i + 1][j])

        if j > 0:
            neighbors.append(image[i][j - 1])

        if j < cols - 1:
            neighbors.append(image[i][j + 1])

        updated[i][j] = sum(neighbors) / len(neighbors)

print("Original Image:")
print(image)

print("\nUpdated Image:")
print(np.round(updated, 2))
