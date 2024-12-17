class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary


    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee):
    
    mgr_count = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = f"{department} - F26"
        
        Manager.mgr_count += 1

    def display_employee(self):
      print("Salary: ", self.salary)


manager1 = Manager("Alex", 5000, "Informatica")


print("Manager display_employee:")
manager1.display_employee()

employee1 = Employee("Maria", 3000)
print("Employee display_employee:")
employee1.display_employee()


print("Total number of employees:", Employee.empCount)
print("Total number of managers:", Manager.mgr_count)
