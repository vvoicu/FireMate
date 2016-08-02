failures = []


class SoftAssert(object):
    def verfy_equals_true(self, message, expected, actual):
        if expected != actual:
            failures.append(message + "Expected: '" + expected + "' - Actual: '" + actual + "'")

    def verfy_contains_true(self, message, expected, actual):
        if expected not in actual:
            failures.append(message + "Expected: '" + expected + "' - Actual: '" + actual + "'")

    def return_failures_size(self):
        return len(failures)

    def return_failures_list(self):
        return failures


if __name__ == "__main__":
    SoftAssert().verfy_equals_true("message equals not as expected", "something", "other")
    print SoftAssert().return_failures_size()
    print SoftAssert().return_failures_list()
