# import numpy as np

# # Sample data
# x = [1, 2, 3, 4, 5]
# y = [1, 2, 3, 4, 5]

# # Calculate correlation coefficient r
# r = np.corrcoef(x, y)[0, 1]

# # Calculate R squared
# r_squared = r ** 2

# print(f"Correlation coefficient (r): {r}")
# print(f"Coefficient of determination (R²): {r_squared}")


def mean(values):
    return sum(values) / len(values)

def calculate_r_and_r_squared(x, y):
    n = len(x)
    if n != len(y):
        raise ValueError("Both lists must have the same number of elements.")

    x_mean = mean(x)
    y_mean = mean(y)

    # Calculate the numerator and denominators for r
    numerator = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
    denominator_x = sum((x[i] - x_mean) ** 2 for i in range(n))
    denominator_y = sum((y[i] - y_mean) ** 2 for i in range(n))

    # Avoid division by zero
    if denominator_x == 0 or denominator_y == 0:
        raise ValueError("Denominator is zero. Cannot calculate correlation.")

    r = numerator / (denominator_x**0.5 * denominator_y**0.5)
    r_squared = r ** 2

    return r, r_squared

# Example usage
x = [1, 2, 3, 4, 5]
y = [-1,-2,-3,-4,-5]

r, r_squared = calculate_r_and_r_squared(x, y)

print(f"Correlation coefficient (r): {r}")
print(f"Coefficient of determination (R²): {r_squared}")
