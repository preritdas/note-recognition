from matplotlib import pyplot as plt
import pandas as pd

def main():
    # Get student
    student = input('Student name: >>> ')
    student = student.title()
    print(student)

    # Load data
    data = pd.read_csv(f'Students/{student}.csv')
    print(data)

if __name__ == "__main__":
    main()