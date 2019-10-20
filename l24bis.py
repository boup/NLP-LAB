
import re
import fileinput


for line in fileinput.input():

    lst=re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", line)
    print(lst)
