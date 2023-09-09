import sqlite3

# Ma'lumotlar bazasini yaratish va bog'lanish
conn = sqlite3.connect("likelist.db")
cursor = conn.cursor()

# "like" jadvalni yaratish (agar mavjud bo'lmasa)
cursor.execute('''CREATE TABLE IF NOT EXISTS like (
                    id INTEGER PRIMARY KEY,
                    school INTEGER,
                    count INTEGER
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS user_list (
                    id INTEGER PRIMARY KEY,
                    number INTEGER
                )''')
