import sqlite3 as sq

# Connexion à la base de données
conn = sq.connect('database.db')
cursor = conn.cursor()

# Création des tables
cursor.execute('''
   CREATE TABLE IF NOT EXISTS users (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       username TEXT UNIQUE,
       user_id INTEGER,
       password TEXT,
       first_name TEXT,
       last_name TEXT,
       trial_start_date DATE
   )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS payments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        amount REAL,
        payment_method TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
''')

# Commit et fermeture de la connexion
conn.commit()

# Vérification des utilisateurs existants
recup = "SELECT * FROM users;"
cursor.execute(recup)
data = cursor.fetchall()
print(data)

# Fermeture de la connexion
conn.close()
