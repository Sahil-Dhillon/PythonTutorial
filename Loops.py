# Loops in Python

print("Different types of loops in Python.")

# for loop
print("1. The 'for' Loop:")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print("I like", x)

# for loop with range
print("2. The 'for' Loop with Range:")
for i in range(1, 6):  # Range(a,b) means from a to b-1
    print("Count:", i)

# while loop
print("3. The 'while' Loop:")
counter = 0
while counter < 5:
    print("Current count:", counter)
    counter += 1  # This is shorthand for counter = counter +1

# Nested loops
print("5. Nested Loops:")
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
