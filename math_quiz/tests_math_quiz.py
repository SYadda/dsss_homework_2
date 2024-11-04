import unittest
from math_quiz import get_random_int, get_random_oper, get_problem_and_answer


class TestMathGame(unittest.TestCase):

    def test_get_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_oper(self):
        # Test if random operator is in ['+', '-', '*']
        all_oper = ['+', '-', '*']
        for _ in range(1000):
            rand_oper = get_random_oper()
            self.assertIn(rand_oper, all_oper)
        

    def test_get_problem_and_answer(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '-', '5 - 2', 3),
                (5, 2, '*', '5 * 2', 10),
                (5, 3, '+', '5 + 3', 8),
                (5, 3, '-', '5 - 3', 2),
                (5, 3, '*', '5 * 3', 15),
                (2, 3, '+', '2 + 3', 5),
                (2, 3, '-', '2 - 3', -1),
                (2, 3, '*', '2 * 3', 6)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # Test if the function returns correct answer
                actual_problem, actual_answer = get_problem_and_answer(num1, num2, operator)
                self.assertEqual(actual_problem, expected_problem)
                self.assertEqual(actual_answer, expected_answer)
    
    def test_get_problem_and_answer_invalid_input(self):
        # Test if the function raises ValueError for invalid inputs
        with self.assertRaises(ValueError):
            get_problem_and_answer(1, 2, '/')  # Invalid operator

        with self.assertRaises(TypeError):
            get_problem_and_answer('1', 2, '+') # Invalid num1
        with self.assertRaises(TypeError):
            get_problem_and_answer(1, '2', '+') # Invalid num2
        with self.assertRaises(TypeError):
            get_problem_and_answer('1', '2', '+') # Invalid num1 and num2

        with self.assertRaises(TypeError):
            get_problem_and_answer(1.5, 2, '+') # Invalid num1
        with self.assertRaises(TypeError):
            get_problem_and_answer(1, 2.5, '+') # Invalid num2
        with self.assertRaises(TypeError):
            get_problem_and_answer(1.5, 2.5, '+') # Invalid num1 and num2


if __name__ == "__main__":
    unittest.main()
