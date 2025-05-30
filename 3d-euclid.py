import numpy as np

def min_distance_between_pairs(A1, A2, B1, B2):
    d1 = np.linalg.norm(np.array(A1) - np.array(B1))
    d2 = np.linalg.norm(np.array(A1) - np.array(B2))
    d3 = np.linalg.norm(np.array(A2) - np.array(B1))
    d4 = np.linalg.norm(np.array(A2) - np.array(B2))
    return min(d1, d2, d3, d4)

# Example usage:
A1 = (-0.09383, 0.7892, -0.4256)
A2 = (0.02734, -0.6646, -0.5536)
B1 = (-0.417, 0.102, -0.02646)
B2 = (-0.2269, 0.3091, 0.8874)

print(min_distance_between_pairs(A1, A2, B1, B2))
