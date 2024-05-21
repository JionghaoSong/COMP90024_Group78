import unittest

def load_tests(loader, standard_tests, pattern):
    if pattern is None:
        pattern = 'test_*.py'
    print(f"Pattern: {pattern}")
    suite = unittest.TestSuite()
    for all_test_suite in unittest.defaultTestLoader.discover('.', pattern=pattern):
        print(f"All test suite: {all_test_suite}")
        for test_suite in all_test_suite:
            print(f"Test suite: {test_suite}")
            suite.addTests(test_suite)
    return suite

if __name__ == '__main__':
    unittest.main()
