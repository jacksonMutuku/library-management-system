# library-management-system

A Django-based Library Management System for managing books, members, and transactions. It supports features like adding books and members, issuing and returning books, tracking outstanding debt, and calculating rent fees.

## Features

- Manage books, members, and transactions.
- 
- Issue and return books to/from members.
- Search for books by title or author.
- Calculate rent fees based on the number of days a book is issued.
- Basic CRUD (Create, Read, Update, Delete) operations for books and members.
- Responsive UI styled with Tailwind CSS.

## Technologies Used

- **Python** (v3.12)
- **Django** (v5.1.1)
- **SQLite** (default database)
- **Tailwind CSS** for frontend styling

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/library-management-system.git
cd library-management-system

```
some  screen shot of the system include

1. This is the manage books page where the librarian can edit and delete a particular book. They can also use the search button to search for a particular book. 
![Screenshot 2024-09-18 at 22 36 19](https://github.com/user-attachments/assets/3c60074c-fe5b-4cc9-87fe-6bd2ea5b27b0)

2. This is the manage members page where the librarian can edit and delete a particular member. 
![Screenshot 2024-09-18 at 22 38 08](https://github.com/user-attachments/assets/af92ec3a-eeed-4c69-aa16-62d428d945d8)

3. This is the issue book page where the librarian can issue a book to a member. If they try to issue a book which is out of stock or to a member who has a debt of more than 500 they will get an error. 
![Screenshot 2024-09-18 at 22 39 15](https://github.com/user-attachments/assets/05fdcd93-e696-404b-b3f9-4bcdb47e8269)

4. This is the add a book page where the librarian can add a book to the system .
![Screenshot 2024-09-18 at 22 39 26](https://github.com/user-attachments/assets/b9e43a22-455c-44ca-ae15-bf954ec6f91c)

5. This is the add a member page where the librarian can add a member to the system . 
![Screenshot 2024-09-18 at 22 39 34](https://github.com/user-attachments/assets/d99697e7-1251-422f-a197-db63eaf0b024)

6. This is the page where the librarian can manage the transactions. They are able to return the book to the system in this page. 
![Screenshot 2024-09-18 at 22 39 47](https://github.com/user-attachments/assets/7a4f2c84-47ec-4ae0-9c00-563aa89ec61b)
