# name-sorter program
The name sorter program reads in a file with names separated by return characters (\n) and provides cleaning and sorting methods.
Finally, the program allows for the user to save the sorted names to another file

## Initialise:
First import the module:
> import name_sorter

Pass in the full path of file to the class by calling:
> ns = NameSorter(file_path)

That's it! Now you can maniplate your list of names

## Clean names
Call the clean() method by
> ns.clean()

## Sort names
Sort the names by using the sort() method
The program uses quicksort algorithm that allow for O(n log n) time complexity
> ns.sort()

## Print names to screen
To print the names to screen simply:
> print(ns)

## Save the names
To save the names to a specified file
> ns.save(file_path)

Sample text with fictious names are provided
