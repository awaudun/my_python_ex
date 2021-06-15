import random

alpha = .2
numnum = 100
random_numbers = []
for i in range(numnum):
    random_numbers.append(random.random())

random_numbers.sort()
##print(random_numbers)

lower_idx = round(numnum * alpha / 2)
upper_idx = round(numnum * (1 - alpha / 2))

print("low: ", random_numbers[:lower_idx])
print("up: ", random_numbers[upper_idx:])



