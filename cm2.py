# A simple script which output the unqie entries of a.txt and b.txt in a single file after comparing both text files.
#Make sure you have the files a.txt and b.txt in the same directory as the script.
#This script first reads the contents of both files into separate lists, then calculates the sets of unique entries in each file by finding the difference between the sets. Finally, it combines the unique entries from both files and writes them to output.txt.


def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    return lines

def write_file(file_path, lines):
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line + '\n')

def main():
    a_lines = read_file('a.txt')
    b_lines = read_file('b.txt')

    unique_a = set(a_lines) - set(b_lines)
    unique_b = set(b_lines) - set(a_lines)

    unique_entries = list(unique_a.union(unique_b))

    write_file('output.txt', unique_entries)

if __name__ == "__main__":
    main()
