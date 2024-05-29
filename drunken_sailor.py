import random
import math

def take_step(x, y):
    random_radian = random.uniform(0, 2 * math.pi)# Step 2: Calculate the change in x (cosine of the angle)
    delta_x = math.cos(random_radian)
    delta_y = math.sin(random_radian)
    return x + delta_x, y + delta_y

steps = int(input("How many steps would you like to take? "))
x = 0
y = 0

for i in range(0, steps):
    x, y = take_step(x, y)

actual = math.sqrt(math.pow(x,2) + math.pow(y,2))
expected = math.sqrt(steps)

# Use math.isclose() to check if actual is approximately equal to expected
assert math.isclose(actual, expected, rel_tol=steps*0.05), f"Expected {expected}, but got {actual}"

print(f"Assertion passed! The drunken sailor get sqrt({steps}) steps away from 0")