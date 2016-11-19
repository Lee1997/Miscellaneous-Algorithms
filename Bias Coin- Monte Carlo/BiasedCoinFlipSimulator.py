# Finds the probability that the majority of coin tosses will produce heads

import random

print("Input the number of coin tosses: ", end="")
tosses = int(input())
print("Input the probability of getting heads: ", end="")
bias = float(input())

count = 0
simulations = 10000

for i in range(simulations):
    total = 0
    for j in range(tosses):
        if random.uniform(0, 1) < bias / 100:
            total += 1
    if total > tosses / 2.0:
        count += 1
print(round(count*100 / simulations))
