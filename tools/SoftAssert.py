
failures = []
class SoftAssert(object):
    def verfy_equals_true(self, message, expected, actual):
        if expected != actual:
            failures.append(message)

    def verfy_contains_true(self, message, expected, actual):
        if expected not in actual:
            failures.append(message)

    def return_failures_size(self):
        return len(failures)

    def return_failures_list(self):
        return failures