# Code modified from GeeksforGeeks and numpy.org reference; code debugged using Claude.ai
import numpy as np

# Set random seed
np.random.seed(21)
N = 66
A = np.random.uniform(-1, 1, (N, N))
b = np.ones(N)

# Method 1: Using numpy's linear algebra solver
x_numpy = np.linalg.solve(A, b)

# Method 2: Gauss-Jordan elimination
def gauss_jordan(A, b):
    # Create augmented matrix [A|b]
    n = len(b)
    augmented = np.column_stack((A.copy(), b.copy()))
    
    # Gauss-Jordan elimination
    for i in range(n):
        # Find pivot
        max_index = np.argmax(abs(augmented[i:, i])) + i
        
        # Swap rows
        if max_index != i:
            augmented[[i, max_index]] = augmented[[max_index, i]]
        
        # Check for singularity
        pivot = augmented[i, i]
        if abs(pivot) < 1e-10:
            print(f"Warning: Small pivot encountered at row {i}: {pivot:.6e}")
            # Use a small number instead of exact zero to continue
            pivot = 1e-10 if pivot >= 0 else -1e-10
        
        # Normalize 
        augmented[i] = augmented[i] / pivot
        
        # Eliminate 
        for j in range(n):
            if j != i:
                factor = augmented[j, i]
                augmented[j] = augmented[j] - factor * augmented[i]
    
    # Solution vector
    return augmented[:, n]

x_gauss_jordan = gauss_jordan(A, b)
numpy_residual = np.linalg.norm(A @ x_numpy - b)
gauss_jordan_residual = np.linalg.norm(A @ x_gauss_jordan - b)
print(f"Residual using numpy.linalg.solve: {numpy_residual:.6e}")
print(f"Residual using Gauss-Jordan elimination: {gauss_jordan_residual:.6e}")
print(f"Difference between solutions: {np.linalg.norm(x_numpy - x_gauss_jordan):.6e}")

# Check condition number of A
cond_number = np.linalg.cond(A)
print(f"\nCondition number of matrix A: {cond_number:.6e}")

# Print elements of the solution vector
print("\nElements of the solution vector:")
for i in range(min(66, N)):
    print(f"x[{i}] = {x_numpy[i]:.10f}")