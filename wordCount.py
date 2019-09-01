import re
import string
import operator
import sys

# storing bash input
input_file = sys.argv[1]
output_file = sys.argv[2]

frequency = {}
document_text = open(input_file, 'r')
text_string = document_text.read()

# looking for matches
match_pattern = re.findall(r'\b[a-zA-Z]{1,30}\b', text_string)
print(len(match_pattern))
match_pattern = [x.lower() for x in match_pattern]

# populating dictionary
for word in match_pattern:
    if word == '':
        continue
    count = frequency.get(word, 0)
    frequency[word] = count + 1

# sorting dictionary
sorted_frequency = sorted(frequency.items())

# writing in output file
f = open(output_file, "w+")
for i in range(len(sorted_frequency)):
    index = i
    tuple = sorted_frequency[i]
    print(str(str(tuple[0])) + " " + str(tuple[1]))
    f.write(str(str(tuple[0])) + " " + str(tuple[1]) + "\n")
