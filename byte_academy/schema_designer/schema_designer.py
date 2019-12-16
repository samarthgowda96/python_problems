import sqlite3

connection = sqlite3.connect('master.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE states(
        state_name TEXT PRIMARY KEY
    );"""
)

cursor.execute(
    """CREATE TABLE cities(
        city_name TEXT PRIMARY KEY,
        state TEXT,
        FOREIGN KEY(state) REFERENCES states(state_name)
    );"""
)

cursor.execute(
    """CREATE TABLE parks(
        park_name TEXT PRIMARY KEY,
        state TEXT,
        FOREIGN KEY(state) REFERENCES states(state_name)
    );"""
)

cursor.execute(
    """CREATE TABLE doctors(
        doctor_name TEXT PRIMARY KEY
    );"""
)

cursor.execute(
    """CREATE TABLE patients(
        patient_name TEXT PRIMARY KEY
    );"""
)

cursor.execute(
    """CREATE TABLE doctors_patients(
        patient TEXT,
        doctor TEXT,
        FOREIGN KEY(patient) REFERENCES patients(patient_name),
        FOREIGN KEY(doctor) REFERENCES doctors(doctor_name)
    );"""
)

cursor.execute(
    """CREATE TABLE users_and_admin(
        name
        username
        password
        email
        phone_number
    );"""


cursor.close()
connection.close()
