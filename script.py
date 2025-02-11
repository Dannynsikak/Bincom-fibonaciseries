import os
import re
import psycopg2

# ✅ Question 1: Write and Read Full Name 
file_name = "name.txt"

# Step 1: Create and write the full name to the text file 
with open(file_name, "w") as file:
    file.write("Ofonime Nsikak Eno")

# Step 2: Read and extract name parts
with open(file_name, "r") as file:
    full_name = file.read().strip()

name_parts = full_name.split()

first_name = name_parts[0]
surname = name_parts[1] if len(name_parts) > 2 else ""
last_name = name_parts[-1]

print(f"First Name: {first_name}")
print(f"Surname: {surname}")
print(f"Last Name: {last_name}")

# ✅ Question 2: Print Local File Path
local_path = os.path.abspath(file_name)
print(f"Local Path: {local_path}")

# ✅ Question 3: Extract Baby Names from HTML Using Regex 
html_file_path = "baby2008.html"

# Read HTML content from the file
with open(html_file_path, "r") as file:
    html_data = file.read()

# Using regex to extract baby names 
pattern = r"<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>"
matches = re.findall(pattern, html_data)

baby_names = [(int(rank), girl_name, boy_name) for rank, girl_name, boy_name in matches]

# Sorting names by rank
baby_names.sort()

print("\nExtracted Baby Names:")
for rank, girl, boy in baby_names:
    print(f"Rank: {rank}: {girl}, {boy}")

# ✅ Question 4: Sorting Algorithm (Bubble Sort) and Binary Search
def bubble_sort(arr):
    """Sorts an array using Bubble Sort."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(arr, target):
    """Implements binary search to find an element in a sorted list."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example list and target
numbers = [34, 7, 23, 32, 5, 62]
sorted_numbers = bubble_sort(numbers)
print("\nSorted Numbers:", sorted_numbers)

target_number = 23
index = binary_search(sorted_numbers, target_number)
if index != -1:
    print(f"Binary Search: {target_number} found at index {index}")
else:
    print(f"Binary Search: {target_number} not found")

# ✅ Question 5: Fibonacci Series Generator
def fibonacci(n):
    """Generates Fibonacci series up to n terms."""
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

# Example usage
n_terms = 10
fib_series = fibonacci(n_terms)
print(f"\nFibonacci Series up to {n_terms} terms: {fib_series}")

# ✅ Question 6: To-Do List with Postgres for Persistent Storage
def create_connection():
    """Create a database connection."""
    try:
        conn = psycopg2.connect(
            dbname="my_database",
            user="myuser",
            password="mypassword",
            host="localhost",
            port="5432"  # Added port
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def create_table():
    """Create to-do table."""
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS todo (
                id SERIAL PRIMARY KEY,
                task TEXT NOT NULL,
                status BOOLEAN NOT NULL DEFAULT FALSE
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ To-Do Table Created Successfully")

def add_task(task):
    """Add a new task to the to-do list."""
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO todo (task) VALUES (%s)", (task,))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"✅ Task Added: {task}")

def get_tasks():
    """Retrieve all tasks from the to-do list."""
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, task, status FROM todo")
        tasks = cursor.fetchall()
        cursor.close()
        conn.close()
        print("\n📋 To-Do List:")
        for task in tasks:
            print(task)
        return tasks

def update_task(task_id, status):
    """Update the status of a task."""
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE todo SET status = %s WHERE id = %s", (status, task_id))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"✅ Task {task_id} Updated")

def delete_task(task_id):
    """Delete a task from the to-do list."""
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM todo WHERE id = %s", (task_id,))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"🗑️ Task {task_id} Deleted")

# Initialize the to-do table
create_table()

# Example usage of to-do list functions
add_task("Complete Python assignment")
add_task("Read a book")
get_tasks()

# ✅ Question 7: Save Baby Names to Postgres Table
def create_baby_names_table():
    """Create baby names table."""
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS baby_names (
                rank INTEGER,
                girl_name TEXT,
                boy_name TEXT
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Baby Names Table Created Successfully")

def save_baby_names(names):
    """Save baby names to the database."""
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        for rank, girl_name, boy_name in names:
            cursor.execute(
                "INSERT INTO baby_names (rank, girl_name, boy_name) VALUES (%s, %s, %s)",
                (rank, girl_name, boy_name)
            )
        conn.commit()
        cursor.close()
        conn.close()
        print(f"✅ Inserted {len(names)} baby names into the database.")

# Initialize the baby names table
create_baby_names_table()

# Save the extracted baby names to the database
save_baby_names(baby_names)
