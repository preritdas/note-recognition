from matplotlib import pyplot as plt
import pandas as pd
import sys
import numpy as np
from os import path

# Get student name
try:
    student_name = sys.argv[1].title()
except IndexError:
    student_name = 'Sample'

# Check is student is existing valid
while not path.exists(f'Students/{student_name}.csv'):
    student_name = input("That student's file doesn't exist. Enter a new one. >>> ")

def load_data(student: str = student_name):
    """Loads a CSV of student's data and returns a DataFrame."""
    try:
        return pd.read_csv(f'Students/{student}.csv', index_col = 0)
    except FileNotFoundError:
        print('File not found. Try again.')
        student = input("Enter the student's name. >>> ")
        return load_data(student)

def save_data(data: pd.DataFrame, student: str = student_name):
    """Takes student's name and their data and writes a file (or updates) CSV with their data."""
    data.to_csv(f'Students/{student}.csv')

def save_plot(data: pd.DataFrame, student: str = student_name):
    fig, ax = plt.subplots()
    plt.style.use('fivethirtyeight')
    ax.set_title(f'Note Reading Accuracy: {student}')
    ax.set_xlabel('Note')
    ax.set_ylabel('Accuracy')
    ax.bar(data.index, data['Accuracy'])
    fig.savefig(f'Graphs/{student}')

def fix_nan(data: pd.DataFrame, note: str):
    data['Correct'][note] = 0
    data['Incorrect'][note] = 0

def main():
    # Load data
    data = load_data()

    # Run the program
    iterations = int(input('How many attempts? >>> '))
    for i in range(iterations):
        note = input('Correct answer >>> ').upper()
        # Nonexistent note check:
        while note not in data.index:
            note = input("That note wasn't in the index. Enter another. >>> ").upper()

        correct = input('Correct? (y/n) >>> ').lower()
        # Not 'y' or 'n' check
        while correct != 'y' and correct != 'n':
            correct = input("Invalid incorrect statement. (y/n) >>> ").lower()

        if correct == 'y':
            if np.isnan(data['Correct'][note]):
                fix_nan(data = data, note = note)
            data['Correct'][note] += 1
            data['Accuracy'][note] = round(data['Correct'][note]/(data['Correct'][note] + data['Incorrect'][note]), 2)
        elif correct =='n':
            if np.isnan(data['Correct'][note]):
                fix_nan(data = data, note = note)
            data['Incorrect'][note] += 1
            data['Accuracy'][note] = round(data['Correct'][note]/(data['Correct'][note] + data['Incorrect'][note]), 2)

    # Save data to CSV
    save_data(data = data)

    # Plot data
    save_plot(data = data)

if __name__ == "__main__":
    main()