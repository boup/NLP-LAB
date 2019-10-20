import csv

def validate_alignment(alignment_filename):
    f = open(alignment_filename) # avoid using key word `file`

    f.readline()  # pass the head line

    contents = csv.reader(f)
    for row in contents:
        if len(row) == 0:
            return False
        row = map(int, row)  # cast read_start and read_end to integer
        if row[0] > row[1]:
            return False
    return True
validate_alignment('file.csv')
