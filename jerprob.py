nums = [3, 1, 2, 5, 4, 6, 7, 10]
morenums = [1,2,4,6,3,9]

def checker(ns=nums, fallson=1):
    """
    ns is a list of integers.
    fallson is what it takes to fail.
    """
    stumbles, oldnum = 0, ns[0]
    for number in ns:
        if number < oldnum:
            stumbles += 1
        if stumbles > fallson:
            return False
        oldnum = number
    return True

print ("for {} the function returns {}".format(nums, checker()))
print ("for {} the function returns {}".format(morenums, checker(ns=morenums)))

