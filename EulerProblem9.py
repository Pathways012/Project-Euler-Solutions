# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000
# Find the product abc

"""
(a + b + c)^2 = 1,000,000
"""
import time
from itertools import permutations

def is_pythagorean_triplet(a, b, c):
    if(a**2 + b**2 == c**2):
        print(f"Pythagorean triplet found: a={a}, b={b}, c={c}")
        return True
    return False

start_time = time.time()
# make a list of numbers 1-999
possible_numbers = list(range(1,1000))
# from that list, make a generator holding permutations of groups of 3 at a time
possible_permutations = permutations(possible_numbers, r=3)

# set a solution_found flag to break the loop
solution_found = False
i = 1

while(solution_found == False):
    # temp is a tuple by default
    temp = (next(possible_permutations))

    if(sum(temp) == 1000):
        if(is_pythagorean_triplet(temp[0], temp[1], temp[2]) == True):
            print(f"Solution found: {temp[0]}, {temp[1]}, {temp[2]}")
            solution_found = True

    print(f"\rFinished iteration {i}", end="")
    i += 1
    
print((temp[0] * temp[1] * temp[2]))

end_time = time.time()
time_to_run = end_time - start_time
print("Time to run: ", time_to_run)
# 200 * 375 * 425 = 31,875,000
# ran in 9654 seconds (~161 minutes)
