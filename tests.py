from io import StringIO
import sys, unittest
import hello_world

def stub_stdin(testcase_inst, inputs):
    stdin = sys.stdin

    def cleanup():
        sys.stdin = stdin

    testcase_inst.addCleanup(cleanup)
    sys.stdin = StringIO(inputs)


def stub_stdouts(testcase_inst):
    stderr = sys.stderr
    stdout = sys.stdout

    def cleanup():
        sys.stderr = stderr
        sys.stdout = stdout

    testcase_inst.addCleanup(cleanup)
    sys.stderr = StringIO()
    sys.stdout = StringIO()


def warp_test_suite(testcase_classes):
    """Load tests from a specific set of TestCase classes."""
    suite = unittest.TestSuite()
    for testcase_class in testcase_classes:
        tests = unittest.defaultTestLoader.loadTestsFromTestCase(testcase_class)
        suite.addTest(tests)
    return suite

class TestStep1(unittest.TestCase):

    def test_hello(self):
        """Tests \"Hello\" in output"""
        stub_stdouts(self)

        hello_world.main()
        output = sys.stdout.getvalue().strip()
        assert "Hello" in output, \
            "Program output does not include \"Hello\".\n"

    def test_hello_world(self):
        """Tests output is \"Hello World\""""
        stub_stdouts(self)

        hello_world.main()
        output = sys.stdout.getvalue().strip()
        assert output == "Hello World", \
            "Program does not output \"Hello World\".\n" \
                + "Expected: {}\n".format("Hello World") \
                + "Actual: {}\n".format(output)
