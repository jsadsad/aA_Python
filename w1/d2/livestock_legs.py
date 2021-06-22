# In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species, chickens have two legs, cows have four legs, and pigs have four legs. The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a function that returns the total number of legs of all the animals

# Write your function, here.
# Parameters are in this order: chickens, cows, pigs
def how_many_legs(num_1, num_2, num_3):
    chicken_legs = num_1 * 2
    cow_legs = num_2 * 4
    pig_legs = num_3 * 4
    return chicken_legs + cow_legs + pig_legs


print(how_many_legs(2, 3, 5))  # > 36
print(how_many_legs(1, 2, 3))  # > 22
print(how_many_legs(5, 2, 8))  # > 50
