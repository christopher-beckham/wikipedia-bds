import glob
import sys

centrals = set()

arr = glob.glob("output/*.txt")
for filename in arr:
    f = open(filename)
    st = ""
    for line in f:
        line = line.rstrip()
        if line == "":
            break
        st = line

    centrals.add(st)

for elem in centrals:
    print elem
