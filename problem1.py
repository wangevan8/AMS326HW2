# Code modified from GeeksforGeeks and numpy.org reference; code debugged using Claude.ai

import numpy as np

def inside_kidney(x, y):
    # Check if point (x,y) is inside the kidney curve
    left_side = (x**2 + y**2)**2
    right_side = x**3 + y**3
    return left_side <= right_side

def inside_disc(x, y):
    # Check if point (x,y) is inside the disc
    return (x - 0.25)**2 + (y - 0.25)**2 <= 0.125

def inside_region(x, y):
    # Check if point is in kidney but not in disc
    return inside_kidney(x, y) and not inside_disc(x, y)

def rectangle(n):

    # Find bounds of the kidney curve
    x_min, x_max = -0.6, 1.2 
    y_min, y_max = -0.6, 1.2
    
    # Grid spacing
    dx = (x_max - x_min) / n
    dy = (y_max - y_min) / n
    
    # Area of each rectangle
    area_element = dx * dy
    
    # Count points inside the region
    count = 0
    for i in range(n):
        x = x_min + (i + 0.5) * dx  # Center of rectangle
        for j in range(n):
            y = y_min + (j + 0.5) * dy  # Center of rectangle
            if inside_region(x, y):
                count += 1
    
    # Total area
    area = count * area_element
    return area

def trapezoidal(n_x=200, n_y=200):
    x_min, x_max = -0.6, 1.2
    y_min, y_max = -0.6, 1.2
    
    dx = (x_max - x_min) / n_x
    dy = (y_max - y_min) / n_y
    
    area = 0.0
    
    for i in range(n_x):
        x = x_min + i * dx
        x_next = x_min + (i + 1) * dx
        x_mid = (x + x_next) / 2
        
        # Process each vertical slice
        for j in range(n_y):
            y = y_min + j * dy
            y_next = y_min + (j + 1) * dy
            y_mid = (y + y_next) / 2
            
            # Check if the center of the cell is in the region
            if inside_region(x_mid, y_mid):
                area += dx * dy
    
    return area

resolution = 1000
area1 = rectangle(resolution)
print(f"Area of kidney minus disc (rectangle method): {area1:.4f}")

area2 = trapezoidal(resolution, resolution)
print(f"Area of kidney minus disc (improved trapezoidal): {area2:.4f}")