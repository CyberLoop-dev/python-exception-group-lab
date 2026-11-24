import unittest
from exception_group_lab import run_demo

class ExceptionGroupLabTests(unittest.TestCase):
    def test_except_star_receives_matching_types(self):
        result={row["handler"]:row for row in run_demo()}
        self.assertEqual(result["ValueError"]["count"],2)
        self.assertEqual(result["TypeError"]["count"],1)
        self.assertEqual(result["OSError"]["count"],1)

if __name__=="__main__": unittest.main()
