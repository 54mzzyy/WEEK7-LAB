import unittest
from EMS_60104563 import Employee, EmployeeManagementSystem

class TestEmployeeManagementSystem(unittest.TestCase):
    def setUp(self):
        self.ems = EmployeeManagementSystem()

    def test_create_employee(self):
        employee = Employee("Elon Musk", 50, 1, "Executive Office")
        self.ems.create_employee(employee.name, employee.age, employee.id, employee.department)
        self.assertEqual(len(self.ems.employees), 1)

    def test_retrieve_employee(self):
        employee = Employee("Jeff Bezos", 57, 2, "Human Resources")
        self.ems.create_employee(employee.name, employee.age, employee.id, employee.department)
        retrieved_employee = self.ems.get_employee_by_id(2)
        self.assertEqual(retrieved_employee.name, employee.name)
        self.assertEqual(retrieved_employee.age, employee.age)
        self.assertEqual(retrieved_employee.id, employee.id)
        self.assertEqual(retrieved_employee.department, employee.department)

    def test_delete_employee(self):
        employee = Employee("Bill Gates", 65, 3, "Board of Directors")
        self.ems.create_employee(employee.name, employee.age, employee.id, employee.department)
        self.ems.delete_employee_by_id(3)
        self.assertEqual(len(self.ems.employees), 0)

    def test_update_employee(self):
        employee = Employee("Mark Zuckerberg", 37, 4, "Research and Development")
        self.ems.create_employee(employee.name, employee.age, employee.id, employee.department)
        self.ems.update_employee_by_id(4, "Mark Zuckerberg", 37, "Head of Research and Development")
        updated_employee = self.ems.get_employee_by_id(4)
        self.assertEqual(updated_employee.name, "Mark Zuckerberg")
        self.assertEqual(updated_employee.age, 37)
        self.assertEqual(updated_employee.department, "Head of Research and Development")

if __name__ == '__main__':
    unittest.main()