"""
should get results like:

[1, 3, 2, 1] = false
[1, 3, 2]
[1, 2, 1, 2] = false
[1, 4, 10, 4, 2] = false
[10, 1, 2, 3, 4, 5]
[1, 1, 1, 2, 3] = false
[0, -2, 5, 6]
[1, 2, 3, 4, 5, 3, 5, 6] = false
[40, 50, 60, 10, 20, 30] = false
[1, 1]
[10, 1, 2, 3, 4, 5, 6, 1] = false
[1, 2, 3, 4, 3, 6]
[1, 2, 3, 4, 99, 5, 6]
"""
manynums = [
([1, 3, 2, 1], False),
([1, 3, 2], True),
([1, 2, 1, 2], False),
([1, 4, 10, 4, 2], False),
([10, 1, 2, 3, 4, 5], True),
([1, 1, 1, 2, 3], False),
([0, -2, 5, 6], True),
([1, 2, 3, 4, 5, 3, 5, 6], False),
([40, 50, 60, 10, 20, 30], False),
([1, 1], True),
([10, 1, 2, 3, 4, 5, 6, 1], False),
([1, 2, 3, 4, 3, 6], True),
([1, 2, 3, 4, 99, 5, 6], True)
]


def allgood(nums):
    # return the position of the fault in an ever-ascending list of int
    start = nums[0] - 1
    for pos, n in enumerate(nums):
        if n > start:
            start = n
        else:
            return pos
    return len(nums)

def checker(ns=None, fallson=1):
    """
    ns is a list of integers.
    fallson is what it takes to fail.
    """
    if ns is None:
        ns = [1, 0]

    position = allgood(ns)

    if position != len(ns):
        if ns[max(position - 1, 0)] >= ns[min(position + 1, len(ns) - 1)]:
            ns.pop(max(position - 1, 0))
        else:
            ns.pop(position)
        return allgood(ns) == len(ns)

    return True


def test_checker(tests=manynums):
    for testline, prediction in tests:
        score = "SUCCESS" if checker(ns=testline) == prediction else "FAILED"
        print("for {} => {} on a given {}".format(testline, score, prediction))

test_checker()
