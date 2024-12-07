import sqlite3
import pandas as pd

# A) Develop SQL code to create the entire database schema
conn = sqlite3.connect('assignment.db')
cursor = conn.cursor()

# Drop tables if they exist to avoid conflicts during repeated runs
cursor.execute("DROP TABLE IF EXISTS Clinic")
cursor.execute("DROP TABLE IF EXISTS Staff")
cursor.execute("DROP TABLE IF EXISTS Owner")
cursor.execute("DROP TABLE IF EXISTS Pet")
cursor.execute("DROP TABLE IF EXISTS Examination")

# Create the tables
cursor.execute('''
    CREATE TABLE Clinic (
        clinicNo INT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        address VARCHAR(255) NOT NULL,
        telephone VARCHAR(15) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE Staff (
        staffNo INT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        address VARCHAR(255) NOT NULL,
        telephone VARCHAR(15) NOT NULL,
        DOB DATE NOT NULL,
        position VARCHAR(50),
        salary DECIMAL(10, 2),
        clinicNo INT,
        skillCode INT,
        deptName VARCHAR(50),
        FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo)
    )
''')

cursor.execute('''
    CREATE TABLE Owner (
        ownerNo INT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        address VARCHAR(255) NOT NULL,
        telephone VARCHAR(15) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE Pet (
        petNo INT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        DOB DATE NOT NULL,
        species VARCHAR(50) NOT NULL,
        breed VARCHAR(50),
        color VARCHAR(50),
        ownerNo INT NOT NULL,
        clinicNo INT NOT NULL,
        FOREIGN KEY (ownerNo) REFERENCES Owner(ownerNo),
        FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo)
    )
''')

cursor.execute('''
    CREATE TABLE Examination (
        examNo INT PRIMARY KEY,
        chiefComplaint VARCHAR(255) NOT NULL,
        description VARCHAR(200) NOT NULL,
        dateSeen DATE NOT NULL,
        actionsTaken VARCHAR(200),
        petNo INT NOT NULL,
        staffNo INT,
        FOREIGN KEY (petNo) REFERENCES Pet(petNo),
        FOREIGN KEY (staffNo) REFERENCES Staff(staffNo)
    )
''')

# 1. Add a new clinic
cursor.execute("""
INSERT INTO Clinic (clinicNo, name, address, telephone)
VALUES (1, 'Gables Clinic', 'Miracle Mile, Coreal Gables', '33155');
""")
conn.commit()
print("1. Added new clinic: 'Gables Clinic'")

# 2. Register a new pet owner and their pet
cursor.execute("""
INSERT INTO Owner (ownerNo, name, address, telephone)
VALUES (1, 'Olga Escoto Balas', '2300 sw 64th Ave, Miami', '3155');
""")
cursor.execute("""
INSERT INTO Pet (petNo, name, DOB, species, breed, color, ownerNo, clinicNo)
VALUES (1, 'Bond', '2015-12-01', 'Dog', 'Mix', 'Golden', 1, 1);
""")
conn.commit()
print("2. Registered new owner: 'OLga Escoto Balas' and their pet: 'Bond'")

# 3. Assign a staff member to manage a clinic
cursor.execute("""
INSERT INTO Staff (staffNo, name, address, telephone, DOB, position, salary, clinicNo)
VALUES (1, 'Dr. Gonzales', 'Moracle Mile, oral Gables', '33155', '1980-02-12', 'Veterinarian', 80000.00, 1);
""")
conn.commit()
print("3. Assigned staff member 'Dr. Gonzales' to 'Gables Clinic'")

# 4. Record an examination for a pet
cursor.execute("""
INSERT INTO Examination (examNo, dateSeen, actionsTaken, chiefComplaint, description, petNo, staffNo)
VALUES (1, '2024-12-01', 'Rabbis Vaccination', 'General Checkup', 'Administered vaccine 3 years', 1, 1);
""")
conn.commit()
print("4. Recorded examination for pet 'Bond'")

# 5. Retrieve all examinations for a specific pet
cursor.execute("""
SELECT Examination.examNo, Examination.dateSeen, Examination.actionsTaken, Pet.name
FROM Examination
JOIN Pet ON Examination.petNo = Pet.petNo
WHERE Pet.petNo = 1;
""")
examinations = cursor.fetchall()
print("\n5. Examinations for Pet ID 1:")
for exam in examinations:
    print(f"   ExamNo: {exam[0]}, Date: {exam[1]}, Actions: {exam[2]}, Pet Name: {exam[3]}")

# Close the connection
conn.close()
