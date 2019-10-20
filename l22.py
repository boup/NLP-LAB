
import re
import csv

def validate_alignment(alignment_filename):
    f = open(alignment_filename) # avoid using key word `file`

    f.readline()  # pass the head line

    contents = csv.reader(f)
    pattern='(\,|\r?\n|\r|^)(?:"([^"]*(?:""[^"]*)*)"|([^"\,\r\n]*))'
    if re.search(pattern, alignment_filename):
        print ("correct")
    else:
        print("error")

validate_alignment('file.csv')
