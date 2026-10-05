print("====================  OOP_Wrapper   ====================")


# ---------------- EMPLOYEE CLASS ----------------

class Employee:

    def __init__(self, name, age, employee_id="", salary=0):

        self.name = name
        self.age = age

        self.__employee_id = employee_id
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id
    
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):

        print("\nEmployee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__employee_id)
        print("Salary:", self.__salary)

    def __del__(self):
        pass


# ---------------- MANAGER CLASS ----------------

class Manager(Employee):

    def __init__(self, name, age, employee_id, salary, department):

        super().__init__(name, age, employee_id, salary)

        self.department = department

    def display(self):

        print("\nManager Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary:", self.get_salary())
        print("Department:", self.department)


# ---------------- DEVELOPER CLASS ----------------

class Developer(Employee):

    def __init__(self, name, age, employee_id, salary,programming_language):

        super().__init__(name, age, employee_id, salary)

        self.programming_language = programming_language

    def display(self):

        print("\nDeveloper Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary:", self.get_salary())
        print("Programming Language:",self.programming_language)
              
employees = []

while True:

    print("\n")
    print("_______________________________________")
    print()
    print("       EMPLOYEE MANAGEMENT SYSTEM")
    print("_______________________________________")
    print()
    print("--------Choose another operation---------")
    print()
    print("Choose an operation:")

    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = input("\nEnter your choise: ")


    if choice == "1":

        print("\nEnter Person Details")

        name = input("Enter Name: ")

        if name == "":
            print("Name cannot be empty.")
        else:

            age = int(input("Enter Age: "))

            if age <= 0:
                print("Age must be greater than 0.")
            else:

                person = Employee(name, age)

                employees.append(person)

                print("\nPerson created with name:", name,
                      "and age:", age, ".")


    elif choice == "2":

        print("\nEnter Employee Details")

        name = input("Enter Name: ")

        if name == "":
            print("Name cannot be empty.")
        else:

            age = int(input("Enter Age: "))

            if age <= 0:
                print("Age must be greater than 0.")
            else:

                employee_id = input("Enter Employee ID: ")

                if employee_id == "":
                    print("Employee ID cannot be empty.")
                else:

                    salary = float(input("Enter Salary: "))

                    if salary < 0:
                        print("Salary cannot be negative.")
                    else:

                        employee = Employee(name,age,employee_id,salary)
                           
                        employees.append(employee)

                        print("\nEmployee created with name:", name,
                              ", age:", age,
                              ", ID:", employee_id,
                              ", and salary: $", salary, ".")


    elif choice == "3":

        print("\nEnter Manager Details")

        name = input("Enter Name: ")

        if name == "":
            print("Name cannot be empty.")
        else:

            age = int(input("Enter Age: "))

            if age <= 0:
                print("Age must be greater than 0.")
            else:

                employee_id = input("Enter Employee ID: ")

                if employee_id == "":
                    print("Employee ID cannot be empty.")
                else:

                    salary = float(input("Enter Salary: "))

                    if salary < 0:
                        print("Salary cannot be negative.")
                    else:

                        department = input("Enter Department: ")

                        if department == "":
                            print("Department cannot be empty.")
                        else:

                            manager = Manager(name,age,employee_id,salary,department)
                               
                            employees.append(manager)

                            print("\nManager created with name:", name,
                                  ", age:", age,
                                  ", ID:", employee_id,
                                  ", salary: $", salary,
                                  ", and department:", department, ".")


    elif choice == "4":

        if len(employees) == 0:

            print("\nNo employee details available.")

        else:

            print("\nChoose details to show:")

            print("1. Person")
            print("2. Employee")
            print("3. Manager")

            detail_choice = input("Enter your choice: ")

            if detail_choice == "1":

                for employee in employees:

                    if employee.get_employee_id() == "":
                        employee.display()


            elif detail_choice == "2":

                for employee in employees:

                    if employee.get_employee_id() != "" and not isinstance(employee, Manager):
                        employee.display()


            elif detail_choice == "3":

                for employee in employees:

                    if isinstance(employee, Manager):
                        employee.display()


            else:

                print("\nInvalid choice.")
                print("Please choose another option.")


    elif choice == "5":

        print("\nExiting the system.")
        print("Goodbye!")

        break

    else:

        print("\nInvalid choice.")
        print("Please choose another option.")