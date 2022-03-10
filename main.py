from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

import sys
import os
import shutil

# Required: Treble or Bass Clef
if 'treble' in sys.argv:
    mode = 'Treble'
elif 'bass' in sys.argv:
    mode = 'Bass'
else:
    raise Exception("You must specify treble or bass.")

# Initiation: possibly create new student or if not, get name
if sys.argv[1] == 'create':
    student_name = sys.argv[2].title()
    shutil.copy(src = f'Students/Copy-{mode}.csv', dst = f'Students/{student_name}-{mode}.csv')
else:
    try:
        student_name = sys.argv[1].title()
    except IndexError:
        student_name = 'Sample'

# Check is student is existing valid
while not os.path.exists(f'Students/{student_name}-{mode}.csv'):
    student_name = input("That student's file doesn't exist. Enter a new one. >>> ")

def load_data(student: str = student_name):
    """Loads a CSV of student's data and returns a DataFrame."""
    try:
        return pd.read_csv(f'Students/{student}-{mode}.csv', index_col = 0)
    except FileNotFoundError:
        print('File not found. Try again.')
        student = input("Enter the student's name. >>> ")
        return load_data(student)

def save_data(data: pd.DataFrame, student: str = student_name):
    """Takes student's name and their data and writes a file (or updates) CSV with their data."""
    data.to_csv(f'Students/{student}-{mode}.csv')

def save_plot(data: pd.DataFrame, student: str = student_name):
    """Takes a DataFrame and saves a student's data to Graphs folder."""
    fig, ax = plt.subplots()
    plt.style.use('fivethirtyeight')
    ax.set_title(f'{mode} Note Reading Accuracy: {student}')
    ax.set_xlabel('Note')
    ax.set_ylabel('Accuracy')
    ax.bar(data.index, data['Accuracy'])
    fig.savefig(f'Graphs/{student}-{mode}')

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