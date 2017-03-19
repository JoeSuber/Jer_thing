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
([10, 1, 2, 3, 4, 5],True),
([1, 1, 1, 2, 3],False),
([0, -2, 5, 6],True),
([1, 2, 3, 4, 5, 3, 5, 6],False),
([40, 50, 60, 10, 20, 30],False),
([1, 1],True),
([10, 1, 2, 3, 4, 5, 6, 1],False),
([1, 2, 3, 4, 3, 6],True),
([1, 2, 3, 4, 99, 5, 6],True)
]

def checker(ns=None, fallson=1):
    """
    ns is a list of integers.
    fallson is what it takes to fail.
    """
    if ns is None:
        ns = [1,0]

    stumbles, oldnum, target = 0, ns[0], 0
    while stumbles < 2:
        for pos, number in enumerate(ns):
            if number <= oldnum:
                target = pos
                stumbles += 1
                break
            oldnum = number
        else:
            return True
        ns.pop(target)
    return False


def test_checker(tests=manynums):
    for testline, prediction in tests:
        score = "SUCCESS" if checker(ns=testline) == prediction else "FAILED"
        print("for {} => {} on a given {}".format(testline, score, prediction))

test_checker()



