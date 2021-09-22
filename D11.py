text =" yeah , i am learning"

print(text=='yeah')

print(text.startswith('yeah'))

print(text.endswith('python'))

import re
text = "11/27/2021"
if re.match(r'\d+/\d+/\d+', text):
    print("yes")
else:
    print("no")

text = "FEB 27 2021"
if re.match(r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|OCT|DEC)\s[\d]{1,2}\s[\d]{4}",text):
    print("yes")
else:
    print("no")
