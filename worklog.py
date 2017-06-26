import os
import sys
import csv

CSV_FILE = 'entries.csv'
FIELDNAMES = ['Name', 'Minutes Spent', 'Date', 'Notes']
def run_program():
    with open(CSV_FILE, 'a') as csvfile:
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
    with open(CSV_FILE, 'a') as csvfile:
        task = {}
        task['Name'] = input('What is the name of your task? ')
        task['Minutes Spent'] = input('How many minutes total did you spend on this task? ')
        task['Date'] = input('What day did this task occur? Please use DD/MM/YYYY format: ')
        if input('Would you like to add notes for this task? ').lower() == 'y':
            task['Notes'] = input('Please types your notes: ')
        task_writer = csv.DictWriter(csvfile, FIELDNAMES)
        task_writer.writerow(task)



def search_for_entry():
    '''Display menu with options for searching for an entry these
    options include searching by [Date], [Time Spent], [Exact Search]
    and [Regex Pattern]'''

def search_by_date():
    '''Allows user to search for tasks by a date'''

def search_by_time_spent():
    '''Allows user to search for tasks by number of minutes spent on
    task'''

def search_exact():
    '''Allows user to search by the exact name of the task'''

def search_by_pattern():
    '''Allows user to provide a RegEx pattern to search for tasks'''

def display_entry():
    '''Displays one entry'''

def display_entries():
    '''Used for returning search results. Can be paged through. Also
    provides options to editing an entry, deleting an entry, and returning
    to the main menu'''

def delete_entry(entry):
    '''Removes a specified entry from the CSV file'''

def edit_entry(entry):
    '''Allows user to change any field of a passed in entry'''



if __name__ == "__main__":
    run_program()
