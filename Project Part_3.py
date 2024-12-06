import sqlite3
import pandas as pd

# A) Develop SQL code to create the entire database schema, reflecting the constraints identified in previous steps
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


# Insert rows for testing
cursor.execute("INSERT INTO Clinic (clinicNo, name, address, telephone) VALUES (1, 'Sunnydale Vet', '123 Sunny St, Miami, FL', '33186')")
cursor.execute("INSERT INTO Clinic (clinicNo, name, address, telephone) VALUES (2, 'Greenfield Clinic', '456 Green Ave, Miami, FL', '33155')")
cursor.execute("INSERT INTO Clinic (clinicNo, name, address, telephone) VALUES (3, 'Mountain View Clinic', '789 Mountain Rd, Miami, FL', '33156')")
cursor.execute("INSERT INTO Clinic (clinicNo, name, address, telephone) VALUES (4, 'Downtown Pet Care', '101 Downtown Blvd, Miami, FL', '33144')")
cursor.execute("INSERT INTO Clinic (clinicNo, name, address, telephone) VALUES (5, 'Beachside Vet', '202 Beach Rd, Miami, FL', '33155')")

cursor.execute("INSERT INTO Staff (staffNo, name, address, telephone, DOB, position, salary, clinicNo, skillCode, deptName) VALUES (1, 'Dr. John Doe', '123 Sunny St, Miami, FL', '33186', '1980-06-15', 'Veterinarian', 75000, 1, 1, 'Veterinary')")
cursor.execute("INSERT INTO Staff (staffNo, name, address, telephone, DOB, position, salary, clinicNo, skillCode, deptName) VALUES (2, 'Jane Smith', '456 Green Ave, Miami, FL', '33156', '1990-11-20', 'Veterinary Technician', 45000, 2, 2, 'Technical')")
cursor.execute("INSERT INTO Staff (staffNo, name, address, telephone, DOB, position, salary, clinicNo, skillCode, deptName) VALUES (3, 'Alice Johnson', '789 Mountain Rd, Miami, FL', '33155', '1985-03-10', 'Receptionist', 35000, 3, 3, 'Administration')")
cursor.execute("INSERT INTO Staff (staffNo, name, address, telephone, DOB, position, salary, clinicNo, skillCode, deptName) VALUES (4, 'Bob Brown', '101 Downtown Blvd, Miami, FL', '33187', '1982-02-25', 'Veterinarian', 80000, 4, 1, 'Veterinary')")
cursor.execute("INSERT INTO Staff (staffNo, name, address, telephone, DOB, position, salary, clinicNo, skillCode, deptName) VALUES (5, 'Charlie White', '202 Beach Rd, Miami, FL', '33186', '1979-12-05', 'Manager', 60000, 5, 4, 'Management')")

cursor.execute("INSERT INTO Owner (ownerNo, name, address, telephone) VALUES (1, 'Michael Scott', '123 Scranton Ave, Miami, FL', '33185')")
cursor.execute("INSERT INTO Owner (ownerNo, name, address, telephone) VALUES (2, 'Dwight Schrute', '456 Schrute Farms, Miami, FL', '33155')")
cursor.execute("INSERT INTO Owner (ownerNo, name, address, telephone) VALUES (3, 'Jim Halpert', '789 Dunder Ave, Miami, FL', '33186')")
cursor.execute("INSERT INTO Owner (ownerNo, name, address, telephone) VALUES (4, 'Pam Beesly', '101 Dunder Blvd, Miami, FL', '33156')")
cursor.execute("INSERT INTO Owner (ownerNo, name, address, telephone) VALUES (5, 'Ryan Howard', '202 Valley Rd, Miami, FL', '33186')")

cursor.execute("INSERT INTO Pet (petNo, name, DOB, species, breed, color, ownerNo, clinicNo) VALUES (1, 'Max', '2018-05-14', 'Dog', 'Labrador', 'Yellow', 1, 1)")
cursor.execute("INSERT INTO Pet (petNo, name, DOB, species, breed, color, ownerNo, clinicNo) VALUES (2, 'Bella', '2017-08-23', 'Cat', 'Siamese', 'Gray', 2, 2)")
cursor.execute("INSERT INTO Pet (petNo, name, DOB, species, breed, color, ownerNo, clinicNo) VALUES (3, 'Charlie', '2020-02-10', 'Dog', 'Golden Retriever', 'Golden', 3, 3)")
cursor.execute("INSERT INTO Pet (petNo, name, DOB, species, breed, color, ownerNo, clinicNo) VALUES (4, 'Lucy', '2019-11-02', 'Dog', 'Beagle', 'Brown', 4, 4)")
cursor.execute("INSERT INTO Pet (petNo, name, DOB, species, breed, color, ownerNo, clinicNo) VALUES (5, 'Milo', '2016-04-25', 'Cat', 'Persian', 'White', 5, 5)")

cursor.execute("INSERT INTO Examination (examNo, chiefComplaint, description, dateSeen, actionsTaken, petNo, staffNo) VALUES (1, 'Limping', 'Possible sprain', '2024-12-06', 'Rest and pain meds', 1, 1)")
cursor.execute("INSERT INTO Examination (examNo, chiefComplaint, description, dateSeen, actionsTaken, petNo, staffNo) VALUES (2, 'Vomiting', 'Possible food poisoning', '2024-12-06', 'Administered IV fluids', 2, 2)")
cursor.execute("INSERT INTO Examination (examNo, chiefComplaint, description, dateSeen, actionsTaken, petNo, staffNo) VALUES (3, 'Coughing', 'Possible kennel cough', '2024-12-06', 'Prescribed antibiotics', 3, 3)")
cursor.execute("INSERT INTO Examination (examNo, chiefComplaint, description, dateSeen, actionsTaken, petNo, staffNo) VALUES (4, 'Itchy Skin', 'Allergic reaction', '2024-12-06', 'Administered antihistamines', 4, 4)")
cursor.execute("INSERT INTO Examination (examNo, chiefComplaint, description, dateSeen, actionsTaken, petNo, staffNo) VALUES (5, 'Scratching eyes', 'Possible conjunctivitis', '2024-12-06', 'Prescribed eye drops', 5, 5)")

# Commit the changes
conn.commit()

# Verifying the inserted data
def fetch_and_print(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")

    # Commit the changes
conn.commit()
   
   # Fetch and print data from tables
def fetch_and_print(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    print(f"Data from {table_name} table:")
    for row in rows:
        print(row)

# Fetch and print data from all tables
fetch_and_print('Clinic')
fetch_and_print('Staff')
fetch_and_print('Owner')
fetch_and_print('Pet')
fetch_and_print('Examination')

# Close the connection
conn.close()

