import sqlite3
connection = sqlite3.connect('predmet.db')
cursor = connection.cursor()
#cursor.execute('''CREATE TABLE IF NOT EXISTS predmety (id INTEGER PRIMARY KEY AUTOINCREMENT, predmet TEXT)''')
#cursor.execute('''INSERT INTO predmety (predmet) VALUES  ('Физика')''')
#cursor.execute('''DELETE FROM predmety ''')


cursor.execute(f"SELECT predmet FROM predmety")
rows1 = cursor.fetchall()
list_predmet = []
for row in rows1:
        for x in row:
            list_predmet.append(x)
#print(list_predmet)



cursor.execute(f"SELECT napravlenie FROM predmety WHERE predmet = 'Биология'")
rows_b = cursor.fetchall()[0]
list_bio_mag = []
for row in rows_b[0].split():
        list_bio_mag.append(row)
#print(list_bio_mag)

cursor.execute(f"SELECT napravlenie FROM predmety WHERE predmet = 'Математика'")
rows_math = cursor.fetchall()[0]
list_math = []
for row in rows_math[0].split():
        list_math.append(row)
#print(list_math)

cursor.execute(f"SELECT napravlenie FROM predmety WHERE predmet = 'Физика'")
rows_ph = cursor.fetchall()[0]
list_physics = []
for row in rows_ph[0].split():
        list_physics.append(row)
#print(list_physics)

cursor.execute(f"SELECT napravlenie FROM predmety WHERE predmet = 'Химия'")
rows_chem = cursor.fetchall()[0]
list_chem = []
for row in rows_chem[0].split():
        list_chem.append(row)
#print(list_chem)

connection.commit()
connection.close()


# lst = 'Биология Бакалавриат2020 Хуятика'
# c = any(map(lambda x: x in lst, list_bio_mag))
#print(c)