"""
File:       name_sorter.py
Purpose:    gets a list of names from a file and sorts the names, before
            printing the sorted names to screen, then outputs the sorted names
            to another text file
Author:     Ethan Ng
Source:     https://github.com/ethannjw/name-sorter.git
"""

import csv
import os

class NameSorter:

    def __init__(self, file_path):
        """initialises the class by reading the file and storing into an attribute"""
        self._openfile(file_path)

    def clean(self):
        """
        Public method that cleans the list of names by removing trailing spaces
        """
        if len(self.list_of_names) > 0:
            for name in self.list_of_names:
                name[0] = name[0].strip()

    def __repr__(self):
        """
        To string method to print out the list of names present in the class
        @return string of list of names separated by return char (\n)
        """
        str = ""
        for name in self.list_of_names:
            str = str + f"{name[0]}\n"
        return str

    def quicksort(self, x):
        """
        Static Method that sorts a list using the quick algorithm
        Quicksort is a divide and conquer strategy algorithm that first selects a pivot,
        then move the smaller elments to the left and the larger ones to the right,
        repeating this till the array is sorted.

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
            first_part = self.quicksort(x[:i])
            second_part = self.quicksort(x[i+1:])
            first_part.append(x[i])
            return first_part + second_part

    def sort(self):
        """Public Method that sorts the list_of_names in class"""
        self.list_of_names = self.quicksort(self.list_of_names)

    def _openfile(self, file_name):
        """
        Private method that opens and reads the file and saves the file in the
        class
        @param file name of file
        @return list of entries in file
        """
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            self.list_of_names = list(reader)

    def save(self, file_name):
        """
        Saves the file with a specified file path
        @param file name of file
        @return list of entries in file
        """
        with open(file_name, "w") as file:
            for name in self.list_of_names:
                file.write(f"{name[0]}\n")

def main():
    """
    Main driver code
    """
    current_folder = os.getcwd()    # get the path of current folder
    parent_folder = os.path.dirname(current_folder)    # get the path of parent folder
    file_path = os.path.join(parent_folder, "unsorted-names-list.txt") # get the file path
    # open the file and read data
    ns = NameSorter(file_path)  # instance of name sorter
    print(f"After import:\n{ns}\n")
    # clean the data
    ns.clean()
    print(f"After cleaning:\n{ns}\n")
    # Sort the data
    ns.sort()
    print(f"After sorting:\n{ns}\n")
    # output to file
    ns.save(os.path.join(parent_folder, "sorted-names-list.txt"))

if __name__ == "__main__":
    main()
