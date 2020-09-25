"""
File:       name_sorter.py
Purpose:    gets a list of names from a file and sorts the names, before
            printing the sorted names to screen
"""

import csv
import os
from os import path

class NameSorter:
    def __init__(self, file_path):
        self.list = self.openfile(file_path)

    @staticmethod
    def quicksort(x):
        """
        Quicksort is a divide and conquer strategy algorithm that first selects a pivot,
        then move the smaller elments to the left and the larger ones to the right,
        repeating this till the array is sorted
        @param array to be sorted
        @return sorted array
        """
        if len(x) == 1 or len(x) == 0:
            return x
        else:
            pivot = x[0]
            i = 0
            for j in range(len(x)-1):
                if x[j+1] < pivot:
                    x[j+1],x[i+1] = x[i+1], x[j+1]
                    i += 1
            x[0],x[i] = x[i],x[0]
            first_part = quicksort(x[:i])
            second_part = quicksort(x[i+1:])
            first_part.append(x[i])
            return first_part + second_part

    def clean(self):
        """
        Cleans the list of names passed into the function and returns a generator
        @param list
        @return generator of cleaned names
        """
        if len(self.list) > 0:
            for name in self.list:
                name[0] = name[0].strip()
                yield name[0]

    @staticmethod
    def openfile(file_name):
        """
        Open the file with read permission using a context manager
        @param file name of file
        @return list of entries in file
        """
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            data = list(reader)
        return data


def main():
    """
    Main driver code
    """
    current_folder = os.getcwd()    # get the path of current folder
    parent_folder = path.dirname(current_folder)    # get the path of parent folder
    file_path = path.join(parent_folder, "unsorted-names-list.txt") # get the file path
    # open the file and read data
    ns = NameSorter(file_path)  # instance of name sorter
    # clean the data
    cleaned_data = list(ns.clean())
    # Sort the data
    sorted_data = ns.quicksort(cleaned_data)
    # print the data using a list comprehension
    [print(name) for name in sorted_data]

if __name__ == "__main__":
    main()
