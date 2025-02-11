# Full Name Extraction, File Handling, Baby Names Extraction, and Sorting Algorithm

# Overview

This Python script performs multiple tasks, including:

Writing and reading a full name from a text file.

Extracting and displaying first name, surname, and last name.

Printing the local file path of the stored text file.

Extracting baby names from an HTML file using regex.

Implementing Bubble Sort for sorting an array.

Implementing Binary Search for searching an element in a sorted list.

# Features

File Handling: Reads and writes a full name to name.txt.

String Manipulation: Extracts and displays name parts.

Local Path Retrieval: Prints the absolute path of name.txt.

Regex Extraction: Extracts baby names from an HTML file (baby2008.html).

Sorting Algorithm: Implements Bubble Sort to sort an array.

Search Algorithm: Implements Binary Search to locate an element in a sorted list.

# Installation & Usage

Prerequisites

Python 3.x installed

Running the Script

Save the script in a .py file (e.g., script.py).

Ensure that baby2008.html exists in the same directory.

Run the script using:

    python3 script.py

Code Explanation

Question 1: Writing and Reading Full Name

Writes "Ofonime Nsikak Eno" to name.txt.

Reads the file and extracts the first name, surname, and last name.

Question 2: Printing Local File Path

Uses os.path.abspath() to get the full path of name.txt.

Question 3: Extracting Baby Names from HTML

Reads baby2008.html and uses regex to extract ranked baby names.

Displays extracted names sorted by rank.

Question 4: Sorting and Searching

Bubble Sort: Sorts a list of numbers.

Binary Search: Searches for a target number in the sorted list and returns its index.

Example Output

First Name: Ofonime
Surname: Nsikak
Last Name: Eno
Local Path: /absolute/path/to/name.txt

Extracted Baby Names:
Rank 1: Emma, Jacob
Rank 2: Olivia, Michael
...

Sorted Numbers: [5, 7, 23, 32, 34, 62]
Binary Search: 23 found at index 2

# Author

**Ofonime Nsikak Eno**
