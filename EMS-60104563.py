class Employee:
    def __init__(self, name, age, id, department):
        self.name = name
        self.age = age
        self.id = id
        self.department = department

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def create_employee(self, name, age, id, department):
        employee = Employee(name, age, id, department)
        self.employees.append(employee)

    def get_employee_by_id(self, id):
        for employee in self.employees:
            if employee.id == id:
                return employee
        return None

    def delete_employee_by_id(self, id):
        for employee in self.employees:
            if employee.id == id:
                self.employees.remove(employee)
                return True
        return False
    
    def update_employee_by_id(self, id, name, age, department):
        for employee in self.employees:
            if employee.id == id:
                employee.name = name
                employee.age = age
                employee.department = department
                return True
        return False

    def show_all_employees(self):
        for employee in self.employees:
            print(f"ID: {employee.id}, Name: {employee.name}, Age: {employee.age}, Department: {employee.department}")

    def main(self):
        while True:
            print("1. Create Employee")
            print("2. Get Employee by ID")
            print("3. Delete Employee by ID")
            print("4. Update Employee by ID")
            print("5. Show All Employees")
            print("6. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                id = int(input("Enter id: "))
                department = input("Enter department: ")
                self.create_employee(name, age, id, department)
            elif choice == 2:
                id = int(input("Enter id: "))
                employee = self.get_employee_by_id(id)
                if employee:
                    print(f"Name: {employee.name}, Age: {employee.age}, Department: {employee.department}")
                else:
                    print("Employee not found")
            elif choice == 3:
                id = int(input("Enter id: "))
                if self.delete_employee_by_id(id):
                    print("Employee deleted successfully")
                else:
                    print("Employee not found")
            elif choice == 4:
                id = int(input("Enter id: "))
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                department = input("Enter department: ")
                if self.update_employee_by_id(id, name, age, department):
                    print("Employee updated successfully")
                else:
                    print("Employee not found")
            elif choice == 5:
                self.show_all_employees()
            elif choice == 6:
                break
            else:
                print("Invalid choice")

ems = EmployeeManagementSystem()
ems.main()