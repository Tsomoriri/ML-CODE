"""
Task 1.1: Python Standard Library Deep Dive: Implement common tasks using only built-in functions and standard libraries (collections, itertools, functools, os, sys, json, csv, etc.).

    Goal: Reduce reliance on external libraries for basics; m emorize common module functions.
"""

"""
Word Frequency Counter: Write a script that reads a text file (input.txt) and counts the frequency of each word (case-insensitive). Print the words and their counts, sorted from most frequent to least frequent. Use collections.Counter.
Grouping Data: You have a list of tuples, e.g., data = [('fruit', 'apple'), ('vegetable', 'broccoli'), ('fruit', 'banana'), ('vegetable', 'carrot')]. Group these items by their category (the first element of the tuple) into a dictionary where keys are categories and values are lists of items. Use collections.defaultdict.
File Concatenation: Write a script that takes multiple filenames as command-line arguments (sys.argv) and concatenates their contents into a single output file (output.txt). Handle potential FileNotFoundError.
CSV to List of Dictionaries: Read a CSV file (data.csv) where the first row is the header. Convert each subsequent row into a dictionary where keys are the header names and values are the corresponding row entries. Store these dictionaries in a list. Use the csv module (csv.DictReader).
List of Dictionaries to CSV: Take a list of dictionaries (e.g., [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]) and write it to a CSV file (output.csv) with appropriate headers. Use the csv module (csv.DictWriter).
Find Unique Lines: Read a text file (logfile.txt) and print only the unique lines found in the file, preserving their first encountered order.
Generate Combinations: Given a list of items items = ['A', 'B', 'C', 'D'], generate all possible unique combinations of size 2. Use itertools.combinations.
Generate Permutations: Given a short string like 'RUN', generate all possible unique orderings (permutations) of its characters. Use itertools.permutations.
Flatten a List of Lists: You have nested_list = [[1, 2], [3, 4, 5], [6]]. Flatten this into a single list [1, 2, 3, 4, 5, 6]. Use itertools.chain.from_iterable.
Recursive Directory Listing: Write a function that takes a directory path as input and lists all files (not directories) within that directory and all its subdirectories. Use os.walk.
Environment Variable Check: Write a script that checks if the environment variable MY_APP_CONFIG is set. If it is, print its value; otherwise, print a default value /etc/my_app/config.json. Use os.environ.get.
JSON Data Parsing: Read a JSON file (config.json) containing configuration data (e.g., {"host": "localhost", "port": 8080, "debug": true}) and load it into a Python dictionary. Use the json module.
Python Object to JSON: Convert a Python dictionary data = {'user_id': 123, 'items': ['apple', 'banana'], 'active': True} into a JSON formatted string with an indentation of 2 spaces. Use the json module.
Calculate Factorial with Reduce: Calculate the factorial of a number (e.g., 5) using functools.reduce and a suitable lambda function or operator. (Note: math.factorial is simpler, but the goal is functools practice).
Memoization with LRU Cache: Implement a recursive function to calculate Fibonacci numbers. Apply functools.lru_cache to optimize it by caching results and avoiding redundant calculations.
Partial Function Application: Create a specialized power function power_of_two that always calculates the power of 2 for any given exponent, using functools.partial based on the built-in pow function or lambda x: x**y.
Deque as Fixed-Size Buffer: Implement a function that reads lines from a potentially large file but only keeps track of the last 5 lines read. Use collections.deque with the maxlen argument.
Named Tuple for Structured Data: Define a Person data structure using collections.namedtuple with fields name, age, and city. Create a few instances of Person.
Slicing an Iterator: You have an iterator (e.g., created by range(1000000) or reading lines from a huge file). Get items from index 100 to 199 (inclusive) without loading the entire sequence into memory. Use itertools.islice.
Zipping and Enumerating: Given two lists, names = ['Alice', 'Bob', 'Charlie'] and scores = [85, 92, 78], create a numbered list of strings like "1. Alice: 85", "2. Bob: 92", etc. Use zip and enumerate.
File Hashing: Write a script that takes a filename as a command-line argument (sys.argv) and calculates and prints its SHA-256 hash. Use the hashlib standard library module (often used alongside file I/O).
"""
 
