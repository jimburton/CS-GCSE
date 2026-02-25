import sqlite3

con = sqlite3.connect("school_clubs.db")
cur = con.cursor()

def get_students_by_club(club_name):
    """Get the name of all students in the  given club."""
    cur.execute("""SELECT student_name
                   FROM Students s
                   INNER JOIN Memberships m USING (student_id)
                   INNER JOIN Clubs c
                   WHERE c.club_name = ?;""", (club_name,))
    return cur.fetchall()

def get_all_students():
    """List all student names in alphabetical order."""
    pass

def get_large_rooms():
    """Find the name and capacity of all rooms that can hold more than 25 people."""
    pass

def get_coding_club():
    """Find the id and name of the club named 'Coding Club'."""
    pass

def get_clubs_and_rooms():
    """Display a list of all club names and the rooms they meet in."""
    pass

def get_clubs_and_leaders():
    """List every club name alongside the name of the student who leads it."""
    pass

def get_art_club_members():
    """List all students who are members of the "Art Club". (Requires joining students, school_clubs, and clubs)."""
    pass

def add_miles():
    """Insert a new student named 'Miles Morales'. Make them into a member of the
    Coding Club."""
    pass

def move_drama():
    """The Drama Club is moving to Room 402. Update the clubs table to reflect this."""
    pass

def move_club(club_name, room_name):
    """Move the given club to the given room."""
    pass

def remove():
    """Alice Smith (ID: 1) has graduated. Remove her student record. Note that you
    must remove her memberships before doing this. WHY IS THAT?"""
    pass


