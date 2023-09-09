# import sqlite3

# def update_school_count(school, count):
#     # Ma'lumotlar bazasiga ulanish
#     conn = sqlite3.connect("likelist.db")
#     cursor = conn.cursor()

#     # Ma'lumotlarni o'qish
#     cursor.execute("SELECT school, count FROM like WHERE school=?", (school,))
#     result = cursor.fetchone()

#     if result is not None:
#         # Ma'lumot mavjud, uning count'ini yangilash
#         existing_count = result[1]
#         new_count = existing_count + count
#         cursor.execute("UPDATE like SET count=? WHERE school=?", (new_count, school))
#     else:
#         # Ma'lumot mavjud emas, yangi ma'lumotni qo'shish
#         cursor.execute("INSERT INTO like (school, count) VALUES (?, ?)", (school, count))

#     conn.commit()

#     # Ma'lumotlar bazasini yopish
#     conn.close()

# # Test qilish
# update_school_count(0, -5)  # "Maktab 1" ni 5 ga qo'shadi
# update_school_count(1, 8)  # "Maktab 2" ni 8 ga qo'shadi


import sqlite3

def get_school_counts():
    # Ma'lumotlar bazasiga ulanish
    conn = sqlite3.connect("likelist.db")
    cursor = conn.cursor()

    # Barcha ma'lumotlarni o'qish
    cursor.execute("SELECT school, count FROM like")
    results = cursor.fetchall()

    # Ma'lumotlarni string ko'rinishida yig'ish
    school_count_text = []
    for result in results:
        school, count = result
        school_count_text.append(f"{school}-{count} count")

    # Ma'lumotlar bazasini yopish
    conn.close()

    # Ma'lumotlarni qaytarish
    return ", ".join(school_count_text)

# O'qib olish funksiyasini chaqirish va natijani chiqarish
result = get_school_counts()
print(result)  # Masalan: "Maktab 1-12 count, Maktab 2-8 count, Maktab 3-15 count"

