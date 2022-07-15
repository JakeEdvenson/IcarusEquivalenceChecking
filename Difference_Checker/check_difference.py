import os
file = open("/home/edvenson/Icarus-Tests/Difference_Check/diff.txt")

lines = 0

for line in file:
    lines = lines + 1

if(lines > 4):
    print("NOT EQUIVALENT. SEE DIFF.TXT FOR MORE INFO!")
else:
    print("Equivalent!")
    os.remove("/home/edvenson/Icarus-Tests/Difference_Check/diff.txt")
