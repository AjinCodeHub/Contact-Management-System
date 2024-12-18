import sqlite3

conn = sqlite3.connect('Contacts_List.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS Contacts(Name TEXT PRIMARY KEY, Number INT )')

while True:
    choice = int(input("\n1. Create Contact\n2. Update Contact\n3. Search Contact\n4. Delete Contact\n5. Display All\n6. Quit\nChoose: "))
    if choice == 1:
        Name = input(str('Enter the Name : '))
        Number = input('Enter the Number : ')
        try:
            cursor.execute('INSERT INTO Contacts(Name, Number) VALUES (?, ?)',(Name, Number))
            conn.commit()
            print('Added Successfully')
        except sqlite3.IntegrityError:
            print('Contact Already Exists')
    
    elif choice == 2:
        choice1 = int(input('1.Update Name \n2.Update Number \n Chooce Any one : '))
        if choice1 == 1:
            Name = input(str('Enter the Name: '))
            cursor.execute('SELECT * FROM Contacts WHERE Name = ?',(Name,))
            record = cursor.fetchone()
            if record:
                New_Name = input(str('Enter the New_Name : '))
                cursor.execute('UPDATE Contacts SET Name = ? WHERE Name = ?',(New_Name, Name))
                conn.commit()
                print('Contact Update Successfully')
            else:
                print('Contact Not Found')
        elif choice1 == 2:
            Name = input(str('Enter the Name: '))
            cursor.execute('SELECT * FROM Contacts WHERE Name = ?',(Name,))
            record = cursor.fetchone()
            if record:
                New_Number =input('Enter the New_Number : ')
                cursor.execute('UPDATE Contacts SET Number = ? WHERE Name = ?',(Name, New_Number))
                conn.commit()
                print('Contact Update Successfully')
            else:
                print('Contact Not Found')
    elif choice == 3:
        Name = input(str('Enter Name to Search: '))
        cursor.execute('SELECT * FROM Contacts WHERE Name = ?',(Name,))
        record = cursor.fetchone()
        if record:
            print(record)
        else:
            print(f'Contact {Name} not avilable')
    elif choice == 4:
        Name = input(str('Enter the Name to Delete: '))
        cursor.execute('SELECT * FROM Contacts WHERE Name = ?',(Name,))
        record = cursor.fetchone()
        if record:
            cursor.execute('DELETE FROM Contacts WHERE Name = ?', (Name,))
            conn.commit()
            print('Delete Contact Successfully')
        else:
            print(f'Conatct {Name} not found')
    elif choice == 5:
        cursor.execute('SELECT * FROM Contacts')
        all_record = cursor.fetchall()
        if all_record:
            for contact in all_record:
                print('Name:', contact[0], '| Number:', contact[1])
        else:
            print('Contacts not found...')

    elif choice == 6:
        print('Thank You...')
        break

    else:
        print('Invalid Entry')
