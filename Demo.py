print("I am studying AI")
x = 5
y = 15 
z =x +y
# f means formatting

print(f"the sum of {x} and {y} = {z}")


import numpy as np
import random

# Step 1: Generate letters a–z
letters = np.array([chr(i) for i in range(97, 123)])  # ['a'...'z']

# Step 2: Generate 100 random numbers (1–100)
numbers = [random.randint(1, 100) for _ in range(100)]

# Step 3: Create 100 groups, each with 4 random numbers from 'numbers'
groups = [random.choices(numbers, k=4) for _ in range(100)]

# Step 4: Map numbers to letters (1–26 → a–z)
# Use modulo so values above 26 still map to valid letters
names = []
for group in groups:
    word = ''.join(letters[(np.array(group) - 1) % 26])
    names.append(word)

# Step 5: Print 100 generated names
for name in names:
    print(name)