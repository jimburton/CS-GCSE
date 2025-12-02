# Answer Key

## Part A: Multiple Choice & Syntax

| Q  |  Topic                  | Correct Answer                     |
|----|-------------------------|------------------------------------|
|1   | Loops (continue)        | D) continue                        |
|2   | Exceptions (finally)    | C) finally                         |
|3   | Classes (__init__)      | C) __init__                        |
|4   | Modules (from...import) | B) from utils import calculate_sum |
|5   | Logging Level           | C) DEBUG                           |
|6   | Custom Exceptions       | C) Exception                       |
|7   | NumPy Array Creation    | B) np.zeros((3, 3))                |
|8   | Pandas Data Structure   | C) DataFrame                       |
|9   | Loop Flow (break)       | B) 1                               |
|10  | Logging Output (Level)  | D) WARNING:root:B, ERROR:root:C    |
|11  | Inheritance (super)     | C) `super().__init__(...)`         |
|12  | Variable scope          | D) Local                           |
|13  | File IO                 | C) 'r'                             |
|14  | Math module             | B) `math.exp(x)`                   |
|15  | Datetime module         | C) `timedelta`                     |

## Part B: Code Interpretation & Debugging 

| Q |  Output                                     | 
|---|---------------------------------------------|
| 1 | Account owned by Jane Doe                   |
|   | Deposit accepted. New balance: 150          |
|   | 150                                         |
| 2 | B                                           |
|   | E                                           |
|   | C: Value cannot be negative                 |
|   | E                                           |
| 3 | (3,)                                        |
|   | [ 4 10 99]                                  |
| 4 | London                                      |
|   | 3                                           |
|   | *(London, Berlin, Rome have pop > 3.0)*     |
| 5 | *Any int between 1 and 10 inclusive*        |
|   | *Any int between 1 and 9 inclusive*         |
|   | `/etc/config/server.conf`                   |
    
## Part C: Code Writing & Application 

1. Custom Exception  

    ```python
    class InsufficientStockError(Exception): # Must inherit from Exception
        """Raised when the desired quantity exceeds available inventory."""
        def __init__(self, msg):         
            super().__init__(msg) 
            # Exception.__init__(msg) is acceptable too.

    def check_stock(inventory, quantity): # Correct function signature
        if quantity > inventory: # Correct condition check
            raise InsufficientStockError(f"Stock of {inventory} is insufficient for {quantity}") # Correctly raises custom exception
    ```
2. Conditional Loop with continue  

    ```python 
    for i in range(1, 11): # Correct range (1 to 10 inclusive)
        if i % 2 == 0: # Correctly checks for even number
            continue # Uses continue
        print(i) # Output: 1, 3, 5, 7, 9
    ```
3. Pandas data and loading

    ```python
    import pandas as pd # Imports pandas

    df = pd.read_csv('sales_data.csv') # Correctly uses read_csv

    print(df.head(5)) # Correctly uses df.head()
    ```
4.  ```python
    class Asset:
        def __init__(self, asset_id, value): # Correct parent __init__
            self.asset_id = asset_id
            self.value = value

    class Electronics(Asset): # Correct inheritance syntax
        def __init__(self, asset_id, value, warranty_months): # Correct child    __init__ signature
            super().__init__(asset_id, value) # Correct use of super()
            # Asset.__init__(asset_id, value) is acceptable too.
            self.warranty_months = warranty_months # New attribute
    ```
5.  ```python
    import math # Import math

    def write_circle_area(radius):
        area = math.pi * (radius ** 2) # Correct calculation using math.pi
        with open('area.txt', 'w') as f: # Correct file opening with 'w' or 'a' mode
            f.write(str(area))
    ```
