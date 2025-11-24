Python Proficiency Exam: Intermediate Concepts

For Multiple Choice & Syntax (Part A) select one answer for each question.

For Code Interpretation (Part B), write the exact output. If an error occurs, state the error type and the line number where it would occur.

For Code Writing (Part C), write clear, concise, and functional Python code. Assume all necessary modules (e.g. `numpy`, `pandas`, `logging`) are installed and available for import.

# Part A: Multiple Choice & Syntax (10 Points)

Select the best answer for each question. (1 point each)

1. Loops & Control Flow
   Which keyword is used to skip the rest of the current loop iteration and move to the next iteration?
   A) exit
   B) skip
   C) break
   D) continue

2. Exception Handling
   What block of code always executes, regardless of whether an exception was raised or not?
   A) try
   B) except
   C) finally
   D) else

3. Class Initialization
   Which special method in a Python class is responsible for setting up the initial state (attributes) of an object when it is created?
   A) __new__
   B) __self__
   C) __init__
   D) __create__

4. Module Import
   If you have a module named `utils.py` containing a function `calculate_sum()`, what is the most concise way to import and use the function without needing to prefix it with `utils.`?
   A) `import utils.calculate_sum`
   B) `from utils import calculate_sum`
   C) `include calculate_sum from utils`
   D) `import calculate_sum in utils`

5. Logging Level
   Which logging level is typically used for tracking the step-by-step execution of a program, often used by developers during debugging?
   A) `WARNING`
   B) `INFO`
   C) `DEBUG`
   D) `ERROR`

6. Custom Exception Inheritance
   When creating a custom exception class in Python, which built-in class should it typically inherit from?
   A) `Error`
   B) `BaseException`
   C) `Exception`
   D) `Runtime`

7. NumPy Array Creation
   What is the fastest way in NumPy to create a 3x3 array initialized entirely with zeros?
   A) `np.array(3, 3, zeros=True)`
   B) `np.zeros((3, 3))`
   C) `np.empty((3, 3), fill=0)`
   D) `np.list_to_array([[0]*3]*3)`

8. Pandas Data Structure
   In pandas, what is the name of the two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns)?
   A) `Series`
   B) `NumPy Array`
   C) `DataFrame`
   D) `Dictionary`

9. Loop Flow
   How many times will the number 5 be printed by the following code?
   
   ```python
   for i in range(10):
        if i == 5:
            print(5)
            break
        if i < 5:
            continue
    ```
    A) 0
    B) 1
    C) 5
    D) 10
10. Logging Output
    What will be displayed to the console if the root logger level is set to `WARNING`?
    
    ```python
    import logging
    logging.basicConfig(level=logging.WARNING)
    logging.info("A")
    logging.warning("B")
    logging.error("C")
    ```
    A) B, C
    B) A, B, C
    C) C
    D) WARNING:root:B, ERROR:root:C

11. Class Inheritance
    When a child class needs to explicitly call the initialization method (__init__) of its parent class, which function is the standard and preferred way to do this?
    A) `ParentClass.__init__(self, ...)`
    B) `base.__init__(self, ...)`
    C) `super().__init__(...)`
    D) `self.parent_init(...)`

12. Variable Scope 
    If a variable `x` is assigned a value inside a function `my_func()`, but outside any nested block, what is the scope of `x`?
    A) Global
    B) Built-in
    C) Enclosing (non-local)
    D) Local

13. File I/O Mode
    What is the standard mode parameter passed to the `open()` function if you intend to read the file contents but not modify or append to the file?
    A) 'a'
    B) 'w'
    C) 'r'
    D) 'r+'

14. The math Module
    Which function from the built-in math module is used to calculate the value of 'e' (Euler's number) raised to the power of x ($e^x$)?
    A) `math.pow(e, x)`
    B) `math.exp(x)`
    C) `math.e_power(x)`
    D) `math.pow(math.e, x)`

15. The datetime Module
    Which object from the datetime module is primarily used to represent a duration, or the difference between two date/time points?
    A) `date`
    B) `time`
    C) `timedelta`
    D) `timeperiod`

# Part B: Code Interpretation & Debugging (20 Points)

Analyze the following code fragments and provide the exact output. (5 points each)

1. Class Interaction and Attributes

    ```python
    class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance # Protected attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposit accepted. New balance: {self._balance}"
        return "Invalid amount."

    def __str__(self):
        return f"Account owned by {self.owner}"

    acct = Account("Jane Doe", 100)
    print(acct)
    print(acct.deposit(50))
    print(acct._balance)
    ```
Output: [Write your output here]

2. Exception Flow and finally

    ```python
    def process_data(value):
        try:
            if value < 0:
                raise ValueError("Value cannot be negative")
            result = 100 / value
            print("A")
        except ZeroDivisionError:
            print("B")
        except ValueError as e:
            print(f"C: {e}")
        except Exception:
            print("D")
        finally:
            print("E")
    
    process_data(0)
    process_data(-1)
    ```
    Output:[Write your output here]

3. NumPy Array Manipulation

    ```python
    import numpy as np

    # Create an array
    data = np.array([2, 5, 8, 10])

    # Operations
    data = data * 2
    data[data > 15] = 99
    data = data[0:3]

    print(data.shape)
    print(data)
    ```
    Output:[Write your output here]

4. Pandas Data Selection

    ```python
    import pandas as pd

    # Create a simple DataFrame
    data = {'City': ['London', 'Paris', 'Berlin', 'Rome'],
            'Population': [8.9, 2.1, 3.7, 2.8],
            'Country': ['UK', 'France', 'Germany', 'Italy']}
    df = pd.DataFrame(data)

    # Filtering and selecting
    filtered_cities = df[df['Population'] > 3.0]['City'].reset_index(drop=True)

    print(filtered_cities[0])
    print(len(filtered_cities))
    ```

    Output:[Write your output here]

5. Standard Modules: random and os

    ```python
    import random
    import os

    # Assume the current directory is /home/user/project

    def get_config_path(filename):
        base_dir = '/etc/config'
        return os.path.join(base_dir, filename)

    random.seed(42)
    print(random.randint(1, 10))
    print(random.randrange(1, 10))
    print(get_config_path('server.conf'))
    ```

    Output:[Write your output here]

## Part C: Code Writing & Application (10 Points)

Write the Python code fragment necessary to achieve the following tasks. (Marks indicated for each question.)

1. Custom Exception (4 Points)
   Write a custom exception class named `InsufficientStockError`. 
   Then, write a function `check_stock(inventory, quantity)` that takes a stock level (integer) and a desired quantity (integer) and raises `InsufficientStockError` if quantity is greater than inventory.
   
   Code: [Write your code for Task 1 here]

2. Conditional Loop with continue (3 Points)
   Write a `for` loop that iterates through the numbers 1 to 10 (inclusive). If a number is even, use continue to skip printing that number. Only odd numbers should be printed to the console.
   
   Code: [Write your code for Task 2 here]

3. Pandas Data Loading and Inspection (3 Points)
   Write the Python code to load a file named `sales_data.csv` into a pandas `DataFrame` and then print the first 5 rows of the loaded `DataFrame`.
   
   Code: [Write your code for Task 3 here]

4.  Class Inheritance (5 Points)
    Create a parent class `Asset` with an `__init__` method that accepts `asset_id` (string) and `value` (float).

    Create a child class `Electronics` that inherits from `Asset`. The `Electronics` class must add an attribute `warranty_months` (integer) and override the `__init__` method to initialize all three attributes.

5.  File I/O and Standard Module (math) (3 Points)
    Write a function `write_circle_area(radius)` that calculates the area of a circle ($A = \pi r^2$) and writes the result to a file named `area.txt`. You must use the math module for $\pi$.
