import fileinput
import re

for line in fileinput.input():
    line = re.sub('adama','anonymized', line.rstrip())
    print(line)
