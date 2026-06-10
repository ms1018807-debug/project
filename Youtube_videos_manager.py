import sqlite3
conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS VIDEOS (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL
    )
''')
def List_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def Add_videos(name ,time):
    cursor.execute("INSERT INTO videos(name ,time) VALUES(?,?)", (name ,time))
    conn.commit()

def Update_videos(Video_id,New_name,time):
    cursor.execute("UPDATE VIDEOS SET  name = ?,time = ? Where ID = ?",(Video_id,New_name, time))
    conn.commit()
    
def Delete_videos(Video_id):
    cursor.execute("DELETE FROM VIDEOS where ID = ?",(Video_id,))
    conn.commit()
def main():
    while True:
        print("\n ======= Youtube Manager App ======")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. EXIT App ")

        choice = int(input("ENTER YOUR CHOICE : "))

        if choice == 1:
            List_videos()

        elif choice == 2:
            name = input("Enter the Video name :")
            time = input("Enter the Video time :")
            Add_videos(name , time)

        elif choice == 3:
            Video_id = input("Enter video ID to UPDATE :")
            name = input("Enter the Video name :")
            time = input("Enter the Video time :")
            Update_videos(Video_id,name ,time)

        elif choice == 4:
            Video_id = input("Enter video ID to DELETE :")
            Delete_videos(Video_id)

        elif choice == 5:
            print("***** THANKYOU! *****")
            print("____HAVE A GOOD DAY!___")
            break
        else:
            print("*** INVALID CHOICE TRY AGAIN ***")
    conn.close()
if __name__ == "__main__":
    main()
            
