#To use this script, follow these steps:

#Create two text files: a.txt and b.txt, with each entry on a new line.
#Place these files in the same directory as the script.
#Run the script. It will compare the entries in a.txt with those in b.txt and create an output.txt file containing the entries from a.txt that are not present in b.txt.

def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return set(line.strip() for line in lines)

def write_output(output_filename, entries):
    with open(output_filename, 'w') as file:
        file.write('\n'.join(entries))

def main():
    a_entries = read_file('a.txt')
    b_entries = read_file('b.txt')

    new_entries = a_entries - b_entries

    write_output('output.txt', new_entries)

if __name__ == "__main__":
    main()
