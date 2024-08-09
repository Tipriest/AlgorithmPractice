import math
def sum(*num):
    total = math.trunc(sum(num))
    return total
if __name__ == "__main__":
    import doctest
    doctest.testfile('test_content.txt', verbose = False)
