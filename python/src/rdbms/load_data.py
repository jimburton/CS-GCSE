import sqlite3
import csv
import os

def setup_db(db_name):
    # Connect to the existing database
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Students")
    cur.execute("DROP TABLE IF EXISTS Rooms")
    cur.execute("DROP TABLE IF EXISTS Clubs")
    cur.execute("DROP TABLE IF EXISTS Memberships")
    cur.execute("""CREATE TABLE
                   Students(student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   student_name TEXT)""")
    cur.execute("""CREATE TABLE
                   Rooms(room_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   room_name TEXT,
                   capacity INTEGER)""")
    cur.execute("""CREATE TABLE
                   Clubs(club_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   club_name TEXT,
                   leader_id INTEGER,
                   room_id INTEGER,
                   FOREIGN KEY(room_id) REFERENCES Rooms(room_id)
                   FOREIGN KEY(leader_id) REFERENCES Students(student_id))""")
    cur.execute("""CREATE TABLE
                   Memberships(membership_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   student_id INTEGER,
                   club_id INTEGER,
                   FOREIGN KEY(student_id) REFERENCES Students(student_id),
                   FOREIGN KEY(club_id) REFERENCES Clubs(club_id))""")

def load_data(db_name, csv_file):
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found.")
        return

    # Connect to the existing database
    con = sqlite3.connect(db_name)
    cur = con.cursor()

    try:
        with open(csv_file, mode='r') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                entry_type = row['type']
                
                if entry_type == 'room':
                    cur.execute(
                        "INSERT INTO Rooms (room_name, capacity) VALUES (?, ?)",
                        (row['name'], int(row['extra1']))
                    )
                
                elif entry_type == 'student':
                    cur.execute(
                        "INSERT INTO Students (student_name) VALUES (?)",
                        (row['name'],)
                    )
                
                elif entry_type == 'club':
                    # extra1 = leader_id, extra2 = room_id
                    cur.execute(
                        "INSERT INTO Clubs (club_name, leader_id, room_id) VALUES (?, ?, ?)",
                        (row['name'], int(row['extra1']), int(row['extra2']))
                    )
                
                elif entry_type == 'membership':
                    # name = student_id, extra1 = club_id
                    cur.execute(
                        "INSERT INTO Memberships (student_id, club_id) VALUES (?, ?)",
                        (int(row['name']), int(row['extra1']))
                    )
        
        con.commit()
        print("Data loaded successfully!")
        
        # Simple verification query
        cur.execute("""
            SELECT s.student_name, COUNT(m.club_id) 
            FROM Students s 
            LEFT JOIN Memberships m ON s.student_id = m.student_id 
            GROUP BY s.student_id
        """)
        print("\nStudent Club Counts:")
        for name, count in cur.fetchall():
            print(f"{name}: {count} clubs")

    except Exception as e:
        print(f"An error occurred: {e}")
        con.rollback()
    finally:
        con.close()

if __name__ == '__main__':
    setup_db("school_clubs.db")
    # Ensure the database exists by running your original setup if needed
    # (Assuming school_clubs.db is in the same folder)
    load_data("school_clubs.db", "school_data.csv")
