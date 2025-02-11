Python Project: Data Processing and To-Do List with PostgreSQL

Description

This Python project covers multiple functionalities including:

Reading and writing names to a file

Extracting baby names from an HTML file using regex

Implementing sorting (Bubble Sort) and searching (Binary Search)

Generating a Fibonacci series

Managing a to-do list with PostgreSQL

Storing baby names in a PostgreSQL database

Features

1. File Handling: Writing and Reading Names

Writes a full name to a text file (name.txt)

Reads and extracts first name, surname, and last name from the file

2. Extracting Baby Names from HTML

Uses regex to extract baby names along with their ranks from an HTML file (baby2008.html)

Displays the names sorted by rank

3. Sorting and Searching

Implements Bubble Sort to sort a list of numbers

Implements Binary Search to find an element in a sorted list

4. Fibonacci Series Generator

Generates the Fibonacci sequence up to n terms

5. To-Do List with PostgreSQL

Uses PostgreSQL for persistent storage

Supports CRUD operations: add, retrieve, update, and delete tasks

6. Saving Baby Names to PostgreSQL

Creates a baby_names table in PostgreSQL

Inserts extracted baby names into the database

Requirements

Make sure you have the following installed:

Python 3.x

PostgreSQL

Required Python packages: psycopg2

Installation

Clone this repository:

git clone https://github.com/Dannynsikak/Bincom-fibonaciseries.git
cd Bincom-fibonaciseries

Install dependencies:

pip install psycopg2

Set up PostgreSQL:

Create a database: my_database

Update the connection parameters in the create_connection() function

Run the script:

python script.py

Usage

Modify the baby2008.html file with your dataset before running the script.

Run the script to extract names, manage tasks, and store data in PostgreSQL.

Database Schema

To-Do List Table (todo)

    id

    task

    status

    SERIAL PRIMARY KEY

    TEXT NOT NULL

    BOOLEAN DEFAULT FALSE

Baby Names Table (baby_names)

    rank

    girl_name

    boy_name

    INTEGER

    TEXT

    TEXT

Author

Ofonime Nsikak Eno

License

This project is licensed under the MIT License.
