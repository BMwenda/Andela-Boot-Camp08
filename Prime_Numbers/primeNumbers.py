''' Function to get the first n prime numbers '''
# An infinite loop -while True- is needed.
# Because we need it to iterate infinitely, until we
# can break out of it. A while True loop is fantastic
# if you want to break out of a loop.


def get_primes(n):
    lst = [2]
    testNum = 3
    if n == 1:
        return [lst[0]]
    elif n == 0:
        return []
    elif n < 0:
        raise Exception("Negative numbers are not allowed")
    elif type(n) is not int:
        raise TypeError("Only integers are allowed")

    while True:
        prime = True
        for item in lst:
            if testNum % item == 0:
                prime = False
                break
                testNum += 1
        if prime:
            lst.append(testNum)
        testNum += 1
        if len(lst) == n:
            break
    return lst
