import sqlite3

con = sqlite3.connect("school_clubs.db")
cur = con.cursor()

def setup_db():
    cur.execute("""CREATE TABLE Students(student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   student_name TEXT)""")
    cur.execute("""CREATE TABLE Rooms(room_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   room_name TEXT,
                   capacity INTEGER)""")
    cur.execute("""CREATE TABLE Clubs(club_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   club_name TEXT,
                   leader_id INTEGER,
                   room_id INTEGER,
                   FOREIGN KEY(room_id) REFERENCES Rooms(room_id)
                   FOREIGN KEY(leader_id) REFERENCES Students(student_id))""")
    cur.execute("""CREATE TABLE School_Clubs(sc_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   student_id INTEGER,
                   club_id INTEGER,
                   FOREIGN KEY(student_id) REFERENCES Students(student_id),
                   FOREIGN KEY(club_id) REFERENCES Clubs(club_id))""")

if __name__ == '__main__':
    setup_db()
