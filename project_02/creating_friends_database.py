import sqlite3

connection = sqlite3.connect("F:\\All_Projs\\Python_Proj\\code_practise\\ds_charts\\project_02\\friends_01.db")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS my_friends")
cursor.execute(
    "CREATE TABLE my_friends(contacts_id VARCHAR(255) PRIMARY KEY NOT NULL, first_name VARCHAR(20) NOT NULL, last_name VARCHAR(30) NOT NULL, profession VARCHAR(50));")
cursor.execute("INSERT INTO my_friends(contacts_id, first_name, last_name) VALUES (1, 'Nikit', 'Poojary'), (2, 'Priyank', 'Mathur'), (3, 'Vishal', 'Swami'), (4, 'Shaun', 'Dias'), (5, 'Rahul', 'Acharya');")

cursor.execute("DROP TABLE IF EXISTS interests")
cursor.execute("CREATE TABLE interests(int_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, interest VARCHAR(50) NOT NULL, contacts_id INT NOT_NULL, CONSTRAINT my_friends_contacts_id_fk FOREIGN KEY (contacts_id) REFERENCES my_friends (contacts_id))")
cursor.execute("INSERT INTO interests(interest, contacts_id) VALUES('Sports'), ('Sports'), ('Exercise'), ('Cooking'), ('Food')")

connection.commit()
connection.close()

