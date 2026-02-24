import sqlite3
import csv
import os

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
                        "INSERT INTO School_Clubs (student_id, club_id) VALUES (?, ?)",
                        (int(row['name']), int(row['extra1']))
                    )
        
        con.commit()
        print("Data loaded successfully!")
        
        # Simple verification query
        cur.execute("""
            SELECT s.student_name, COUNT(sc.club_id) 
            FROM Students s 
            LEFT JOIN School_Clubs sc ON s.student_id = sc.student_id 
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
    # Ensure the database exists by running your original setup if needed
    # (Assuming school_clubs.db is in the same folder)
    load_data("school_clubs.db", "school_data.csv")
