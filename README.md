# 🧑‍💼 OOP Wrapper – Employee Management System

**A beginner-friendly Python OOP project demonstrating core Object-Oriented Programming concepts through a simple console-based Employee Management System.**
---

## 📌 Project Overview

**OOP Wrapper – Employee Management System** is a Python project created to understand and practically implement fundamental **Object-Oriented Programming (OOP)** concepts.

The system allows users to create and manage:

- 👤 Person
- 👨‍💼 Employee
- 👔 Manager
- 👨‍💻 Developer

It provides a simple menu-driven console interface with basic input validation and detail display options.

---

## 🎯 Objective

The main objective of this project is to practically implement fundamental Python OOP concepts using an Employee Management System.

The project demonstrates:

- Classes and Objects
- Constructors and Destructors
- Encapsulation
- Getter and Setter Methods
- Inheritance
- Method Overriding
- Method Overloading using Default Arguments
- `self` Keyword
- `super()` Function
- `issubclass()`
- Polymorphism
- Menu-driven interface
- Basic `if-else` validation

---

## 🧩 OOP Concepts Used

| OOP Concept | Implementation |
|---|---|
| **Class** | `Employee`, `Manager`, `Developer` |
| **Object** | Person, Employee and Manager objects |
| **Constructor** | `__init__()` |
| **Destructor** | `__del__()` |
| **Encapsulation** | Private Employee ID and Salary |
| **Getter** | `get_employee_id()`, `get_salary()` |
| **Setter** | `set_employee_id()`, `set_salary()` |
| **Inheritance** | Manager/Developer inherit Employee |
| **Method Overriding** | `display()` |
| **Method Overloading** | Default constructor arguments |
| **`self`** | Instance reference |
| **`super()`** | Parent constructor call |
| **`issubclass()`** | Inheritance checking |
| **Polymorphism** | Different `display()` implementations |
| **Validation** | Basic `if-else` validation |

---

## 🏗️ Class Structure

```text
                    Employee
                   /        \
                  /          \
             Manager       Developer
```

### Employee – Base Class

The `Employee` class contains common information:

- Name
- Age
- Employee ID
- Salary

Employee ID and Salary are implemented using private attributes for encapsulation.

### Manager – Derived Class

The `Manager` class inherits from `Employee` and adds:

- Department

It also overrides the `display()` method.

### Developer – Derived Class

The `Developer` class inherits from `Employee` and adds:

- Programming Language

It also overrides the `display()` method.

---

## 🖥️ Main Menu

```text
_______________________________________

       EMPLOYEE MANAGEMENT SYSTEM

_______________________________________

--------Choose another operation---------

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit

Enter your choise:
```

---

## ⚙️ Features

- Create a Person
- Create an Employee
- Create a Manager
- Display Person details
- Display Employee details
- Display Manager details
- Basic input validation
- Getter and setter methods
- Inheritance and method overriding
- Menu-driven console interface
- Exit option

---

## ✅ Basic Validation

The project uses simple beginner-level `if-else` validation:

- Name cannot be empty
- Age must be greater than 0
- Employee ID cannot be empty
- Salary cannot be negative
- Department cannot be empty
- Invalid menu choices are handled

---

## 🖼️ Output Preview

See the actual program output:

[![View Output](https://img.shields.io/badge/👀_View_Output-red?style=for-the-badge)](https://github.com/dh-2006/oop_Wrapper/blob/main/output.png)
---

## 🎥 Project Demo

Watch the complete working demonstration:

[![Watch Demo](https://img.shields.io/badge/▶️_Watch_Project_Demo-blue?style=for-the-badge)](https://drive.google.com/file/d/1hJaOdupPayvynsR8bR2cJ1uCcOB7iDF1/view?usp=sharing)

---

## 💻 Source Code

View the complete Python source code:

[![Open Source Code](https://img.shields.io/badge/💻_View_Source_Code-green?style=for-the-badge)](https://github.com/dh-2006/oop_Wrapper/blob/main/oop_Wrapper.py)

---

## ▶️ How to Run

### Requirements

- Python 3.x
- Any Python IDE or Terminal

### Run the program

```bash
python oop_Wrapper.py
```

---

## 📂 Project Structure

```text
OOP_Wrapper/
│
├── oop_Wrapper.py
├── output.png
└── README.md
```

---

## 🎓 Learning Outcomes

After completing this project, a beginner can understand:

- How classes and objects work in Python
- How inheritance works
- How encapsulation protects data
- How getters and setters control data access
- How method overriding works
- How `super()` connects parent and child classes
- How constructors initialize objects
- How menu-driven console applications work
- How basic validation can be implemented using `if-else`

---

## 🔮 Future Improvements

Possible future enhancements include:

- Update employee details
- Delete employee records
- Search employee by ID
- File-based data storage
- SQLite/MySQL database integration
- Graphical User Interface (GUI)
- Login/authentication system
- More employee roles

---

## 👨‍💻 Author

**Dharmi Sonani**

---

⭐ If this project helped you learn Python OOP, consider starring the repository.

---




