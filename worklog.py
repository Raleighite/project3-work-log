import os
import sys
import csv
import datetime
import re

CSV_FILE = 'entries.csv'
FIELDNAMES = ['ID','Name', 'Minutes Spent', 'Date', 'Notes']
DATA_ID_FORMAT = '%Y%m%d%H%M%S%f'

def run_program():
    if os.path.exists('entries.csv'):
        display_menu()
    else:
        with open(CSV_FILE, 'a', newline='') as csvfile:
            entry_writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
            entry_writer.writeheader()
        display_menu()

def display_menu():
    clear_screen()
    print("What would you like to do? ")
    choice = input("""Chose one of the following: \n
    N -> Make a new entry \n
    S -> Search for an entry \n
    Q -> Quit\n
    -> """).lower().strip()
    if choice == 's':
        search_for_entry()
    elif choice == 'q':
        sys.exit()
    else:
        new_entry()

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def new_entry():
    '''Make a new entry in the CSV file. New entry must include
    [Name], [Minutes Spent], [Date], and [Notes]'''
    clear_screen()
    timestamp_format = '%m-%d-%Y %H:%M'
    the_date = datetime.datetime.now()
    with open(CSV_FILE, 'a') as csvfile:
        task = {}
        task['ID'] = the_date.strftime(DATA_ID_FORMAT)
        task['Name'] = input('What is the name of your task? ')
        task['Minutes Spent'] = input('How many minutes total did you spend on this task? ')
        task['Date'] = the_date.strftime(timestamp_format)
        if input('Would you like to add notes for this task? ').lower() == 'y':
            task['Notes'] = input('Please type your notes: ')
        task_writer = csv.DictWriter(csvfile, FIELDNAMES)
        task_writer.writerow(task)
    clear_screen()
    input('Task saved! Please hit any key to return to the main menu')
    display_menu()



def search_for_entry():
    '''Display menu with options for searching for an entry these
    options include searching by [Date], [Time Spent], [Exact Search]
    and [Regex Pattern]'''
    clear_screen()
    choice = input('''
    How would you like to search?
    D -> Search by date
    T -> Search by time spent
    N -> Search by task name
    P -> Search by Regex pattern

    M -> Return to main menu
    ''').lower().strip()

    if choice == "d":
        search_by_date()
    elif choice == "t":
        search_by_time_spent()
    elif choice == "n":
        search_exact()
    elif choice == "p":
        search_by_pattern()
    else:
        display_menu()

def search_by_date():
    '''Allows user to search for tasks by a date'''
    clear_screen()
    results = []
    date_given= input("Please enter the date you want to search for tasks from. Please"
          "use the format MM-DD-YYYY ")
    if re.search(r'\d{2}-\d{2}-\d{4}', date_given):
        with open('entries.csv') as csvfile:
            csv_dict = csv.DictReader(csvfile)
            for entry in csv_dict:
                if date_given in entry['Date']:
                    results.append(entry)
    else:
        print("Sorry, that's not a date I recognize. Please try again.")
        search_by_date()
    if results:
        display_entries(results)
        input("That's all I could find. Press any key to return to the search menu")
        search_for_entry()
    else:
        print("No results were found for your search")
        search_for_entry()

def search_by_time_spent():
    '''Allows user to search for tasks by number of minutes spent on
    task'''

def search_exact():
    '''Allows user to search by the exact name of the task'''

def search_by_pattern():
    '''Allows user to provide a RegEx pattern to search for tasks'''

def display_entry(entry):
    '''Displays one entry'''
    print("*" * 50)
    print("Date and time: {}".format(entry['Date']))
    print("Task name: {}".format(entry['Name']))
    print("Minutes spent: {}".format(entry['Minutes Spent']))
    if entry['Notes']:
        print("Notes: {}".format(entry['Notes']))
    print("*" * 50)

def display_entries(entries):
    '''Used for returning search results. Can be paged through. Also
    provides options to editing an entry, deleting an entry, and returning
    to the main menu'''
    print("Based on your search I found {} entries".format(len(entries)))
    count = 0
    while count < len(entries):
        display_entry(entries[count])
        entry = entries[count]
        print("\n")
        choice = input("""
        What would you like to do?
        E -> Edit this entry
        D -> Delete this entry
        P -> View previous entry
        N -> View next entry
        S -> Return to search menu
        """).strip().lower()
        if choice == "e":
            edit_entry(entry)
        elif choice == "d":
            delete_entry(entry)
        elif choice == "p":
            count -= 1
        elif choice == "s":
            search_for_entry()
        elif choice == "n":
            count += 1
        else:
            print("That's not a valid choice, start again")
            display_entries(entries)
    if count > len(entries):
        input("That's all the entries I could find. Press any key to return to the search menu")
        search_for_entry()


def delete_entry(entry):
    '''Removes a specified entry from the CSV file'''
    print("You reached the delete entry section")

def edit_entry(entry):
    '''Allows user to change any field of a passed in entry'''
    print("You reached the edit entry section")



if __name__ == "__main__":
    run_program()
