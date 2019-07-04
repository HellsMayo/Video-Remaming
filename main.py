import os
import csv
import sys

"""
search in the given directory path and according to the csv
within the folder rename each file within the folder.

renamed to:
"s[season #]e[episode #] [episode name].[file type]"

contents of csv must be formatted as:
[episode #],[episode name],[file type]
"""


if __name__ == "__main__":
    season = "3"
    dir_path = fr"G:\Media\Cartoons\_We Bare Bears\Season 3 1080p"
    csv_file_name = fr"season {season}.csv"

    # Create list of current file names
    # dubbed old_file_names
    old_file_names = os.listdir(dir_path)
    old_file_names.remove(csv_file_name)
    old_file_names.sort()

    # Create list of files names to be updated to
    # dubbed new_file_names
    new_file_names = []
    with open(fr"{dir_path}\{csv_file_name}") as csv_file:
        episode_reader = csv.reader(csv_file)
        for row in episode_reader:
            empty = True
            for cell in row:
                if len(cell) != 0:
                    empty = False
                    break
            if not empty:
                new_file_names.append(fr"s{season}e{row[0]} {row[1][:]}.{row[2]}")

    # print both lists
    print(old_file_names)
    print(new_file_names)

    # check if all of the new names are valid files names
    invalid_names = []
    for name in new_file_names:
        if ('\\' in name or
                '/' in name or
                ':' in name or
                '*' in name or
                '?' in name or
                '"' in name or
                '<' in name or
                '>' in name or
                '|' in name):
            invalid_names.append(name)
    if len(invalid_names) != 0:
        print()
        print("ERROR: some of the new names are non-valid file names")
        print("ERROR: renaming will not be allowed")
        print("ERROR: the following are the new names that are non-valid")
        for name in invalid_names:
            print(name)
        sys.exit()

    # print what the current files names will be renamed to
    print()
    i = 0
    while i < len(old_file_names) and i < len(new_file_names):
        print(old_file_names[i], end='\t\t-->\t\t')
        print(new_file_names[i])
        i += 1

    # check if the lists are the same length
    if len(old_file_names) != len(new_file_names):
        print()
        if len(old_file_names) > len(new_file_names):
            print(fr"WARNING: there are {(len(old_file_names) - len(new_file_names))} more files than updating names")
            print("WARNING: the following are the files that will not be renamed")
            while i < len(old_file_names):
                print(old_file_names[i])
                i += 1
        else:
            print(fr"WARNING: there are '{len(new_file_names) - (len(old_file_names))}' less files than updating names")
            print("WARNING: the following are the updating names that will not be used")
            while i < len(new_file_names):
                print(new_file_names[i])
                i += 1

    # require user input to commit to renaming the files
    print()
    print(fr"if confirmed, the above renamings will continue within {dir_path}")
    if input("type 'yes' and press enter to confirm with the above renamings: ") != "yes":
        # exit the program
        print("Rename not completed")
        sys.exit()
    else:
        # rename all the listed files
        i = 0
        while i < len(old_file_names) and i < len(new_file_names):
            os.rename(fr"{dir_path}\{old_file_names[i]}", fr"{dir_path}\{new_file_names[i]}")
            i += 1
        print()
        print("Rename completed")
