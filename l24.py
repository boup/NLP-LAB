import re
import fileinput


for line in fileinput.input():
    lst = re.findall('\S+@\S+', line)
    print(lst)
