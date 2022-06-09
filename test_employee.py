import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('SetUpClass')

    @classmethod
    def tearDownClass(cls):
        print('TearDownClass')

    def setUp(self):
        print('setUp function')
        self.emp_1 = Employee('Wazed', 'Khan', 5000)
        self.emp_2 = Employee('Rehan', 'Aman', 5000)

    def tearDown(self):
        print('tearDown Function')

    def test_email(self):
        print('Email')
        self.assertEqual(self.emp_1.email, 'wazed.khan@gmail.com')
        self.assertEqual(self.emp_2.email, 'rehan.aman@gmail.com')

    def test_fullname(self):
        print('Full Name')
        self.assertEqual(self.emp_1.fullname, 'Wazed Khan')

    def test_monthly_schedule(self):
        print('test_monthly_schedule')
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Khan/May')
            self.assertEqual(schedule, 'Success')



if __name__ == "__main__":
    unittest.main()

