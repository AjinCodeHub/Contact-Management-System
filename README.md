# Contact Management System

## Description

A simple Python-based Contact Management System that allows users to create, update, search, delete, and display contacts. The project uses SQLite for database storage and features a menu-driven command-line interface for ease of use.

---

## Features

1. **Create Contact:** Add new contacts with a unique name and associated phone number.
2. **Update Contact:** Modify existing contact details (name or number).
3. **Search Contact:** Retrieve contact details using the name as a query.
4. **Delete Contact:** Remove contacts from the database.
5. **Display All Contacts:** View all saved contacts.

---

## Technologies Used

- **Programming Language:** Python
- **Database:** SQLite

---

## Code Overview

The main Python script contains:

- **Database Setup:** Creates the \`\` table if it doesn't exist.
- **Menu-Driven Interface:** Allows the user to select options to manage contacts.
- **Error Handling:** Prevents duplicate entries and handles invalid inputs.

---

## Example Usage

### 1. Create Contact

Input:

```
Enter Name: John
Enter Number: 1234567890
```

Output:

```
Contact added.
```

### 2. Display All Contacts

Output:

```
Name: John, Number: 1234567890
```

### 3. Update Contact

Input:

```
1.Update name
2.Update number
Choose Any One: 1
Enter the name: John
Enter the New_Name: Johnny
```

Output:

```
Contact updated successfully.

```
---
### To install **DB Browser for SQLite**, follow these steps based on your operating system:

### **Windows**
1. **Download**:
   - Visit the official website: [DB Browser for SQLite](https://sqlitebrowser.org/dl/).

2. **Install**:
   - Run the downloaded `.exe` file.
   - Follow the installation wizard:
     - Accept the license agreement.
     - Choose the installation directory.
     - Complete the installation.

3. **Launch**:
   - Open DB Browser for SQLite from the Start Menu or Desktop shortcut.
---

### **Using DB Browser for SQLite**
1. Open the application.
2. Click **Open Database** and select your `.db` file (e.g., `Contacts List.db`).
3. Navigate to the **Browse Data** tab to view or edit the contents of your database.

---
