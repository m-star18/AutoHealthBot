import unittest

from src.job import AutoHealthJob


class MyTestCase(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.job = AutoHealthJob(option=True)

    def test(self):
        self.assertEqual(self.job.state, True)


if __name__ == '__main__':
    unittest.main()
