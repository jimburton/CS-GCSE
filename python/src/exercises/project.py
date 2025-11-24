import sqlite3
from typing import List, Dict, Optional, Tuple
from datetime import datetime

class DatabaseManager:
    """
    Manages the connection and operations for the SQLite Price Tracker database.
    """
    def __init__(self, db_path: str = "price_tracker.db"):
        """
        Initializes the database connection and ensures tables exist.
        """
        self.db_path = db_path
        print(f"Connecting to database: {self.db_path}")
        self._create_tables()

    def _get_connection(self) -> sqlite3.Connection:
        """
        Creates and returns a database connection using a context manager.
        """
        # Isolation level is set to None for autocommit mode, which is simpler for most commands.
        return sqlite3.connect(self.db_path, isolation_level=None)

    def _create_tables(self):
        """
        Creates the necessary tables if they don't already exist.
        """
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                
                # 1. Products Table (The items we are tracking)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        url TEXT UNIQUE NOT NULL,
                        target_price REAL NOT NULL,
                        last_checked TEXT 
                    );
                """)
                
                # 2. Price History Table (The historical log of prices)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS price_history (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        product_id INTEGER NOT NULL,
                        price REAL NOT NULL,
                        timestamp TEXT NOT NULL,
                        FOREIGN KEY (product_id) REFERENCES products(id)
                    );
                """)
                conn.commit()
            print("Database tables initialized successfully.")
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def add_product(self, name: str, url: str, target_price: float) -> Optional[int]:
        """
        Adds a new product to the 'products' table. Returns the new product ID.
        """
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    INSERT INTO products (name, url, target_price) 
                    VALUES (?, ?, ?)
                    """, 
                    (name, url, target_price)
                )
                conn.commit()
                product_id = cursor.lastrowid
                print(f"Successfully added product '{name}' with ID: {product_id}")
                return product_id
        except sqlite3.IntegrityError:
            print(f"Error: Product with URL '{url}' already exists.")
            return None
        except sqlite3.Error as e:
            print(f"Error adding product: {e}")
            return None

    def get_all_products(self) -> List[Dict]:
        """
        Retrieves all products currently being tracked.
        """
        products = []
        try:
            with self._get_connection() as conn:
                # Set row_factory to sqlite3.Row to allow accessing columns by name (like a dictionary)
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT id, name, url, target_price FROM products")
                
                for row in cursor.fetchall():
                    # Convert sqlite3.Row object to a standard dictionary
                    products.append(dict(row))
            print(f"Retrieved {len(products)} products from the database.")
            return products
        except sqlite3.Error as e:
            print(f"Error retrieving products: {e}")
            return []

    def log_price(self, product_id: int, price: float):
        """
        Logs the price found for a specific product and updates its last checked time.
        """
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                
                # 1. Insert into history
                cursor.execute(
                    """
                    INSERT INTO price_history (product_id, price, timestamp) 
                    VALUES (?, ?, ?)
                    """, 
                    (product_id, price, current_time)
                )

                # 2. Update the last_checked time on the product
                cursor.execute(
                    """
                    UPDATE products SET last_checked = ? WHERE id = ?
                    """,
                    (current_time, product_id)
                )
                conn.commit()
                print(f"Logged price ${price:.2f} for product ID {product_id}.")
        except sqlite3.Error as e:
            print(f"Error logging price: {e}")


# --- DEMONSTRATION USAGE ---

if __name__ == "__main__":
    # Create the manager instance. This will create the 'price_tracker.db' file
    # and set up the tables if it's the first run.
    db_manager = DatabaseManager()

    # --- 1. Add some products ---
    print("\n--- Adding Products ---")
    db_manager.add_product("Python Guide Book", "https://example.com/book", 35.00)
    db_manager.add_product("Wireless Mouse Pro", "https://example.com/mouse", 50.00)
    db_manager.add_product("Headphones X", "https://example.com/headphones", 199.99)
    
    # Try adding a duplicate product (will fail due to UNIQUE constraint)
    db_manager.add_product("Python Guide Book", "https://example.com/book", 30.00)

    # --- 2. Retrieve all products ---
    print("\n--- Listing All Tracked Products ---")
    tracked_items = db_manager.get_all_products()
    for item in tracked_items:
        print(f"ID: {item['id']}, Name: {item['name']}, Target: ${item['target_price']:.2f}")

    # --- 3. Log prices for the first two products ---
    print("\n--- Logging Price Data ---")
    
    if tracked_items:
        # Assuming the first item has ID 1 and second has ID 2
        id_1 = tracked_items[0]['id']
        id_2 = tracked_items[1]['id']
        
        db_manager.log_price(id_1, 29.50) # Price below target
        db_manager.log_price(id_1, 30.05) # Price above target
        db_manager.log_price(id_2, 51.99) # Price above target

    # --- 4. Verify History (Optional check) ---
    print("\n--- Verifying Price History for Product ID 1 ---")
    with db_manager._get_connection() as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        if tracked_items:
            cursor.execute("SELECT * FROM price_history WHERE product_id = ? ORDER BY timestamp DESC", (id_1,))
            history = cursor.fetchall()
            for entry in history:
                print(f"  Time: {entry['timestamp']}, Price: ${entry['price']:.2f}")