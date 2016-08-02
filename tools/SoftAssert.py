failures = []


class SoftAssert(object):
    def verfy_equals_true(self, message, expected, actual):
        if expected != actual:
            failures.append(message + "Expected: '" + format(expected) + "' - Actual: '" + format(actual) + "'")

    def verfy_contains_true(self, message, expected, actual):
        if expected not in actual:
            failures.append(message + "Expected: '" + expected + "' - Actual: '" + actual + "'")

    def failures_size(self):
        return len(failures)

    def failures_list(self):
        return failures


if __name__ == "__main__":
    #ex1
    listA = []
    listA.append("f")
    listA.append("e")
    listA.append("h")
    listA.append("t")
    

    listB = []
    listB.append("f")
    listB.append("h")
    listB.append("e")
    listB.append("t")
    SoftAssert().verfy_equals_true("message equals not as expected", listA, listB)

    #ex 2
    SoftAssert().verfy_equals_true("message equals not as expected", "something", "other")
    print SoftAssert().failures_size()
    print SoftAssert().failures_list()
