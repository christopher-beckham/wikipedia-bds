import glob
import sys
import os

print "nodes"

files = glob.glob("output/*.txt")
for f in files:
    wc = os.popen("wc -l " + f).read()
    print wc.split()[0]
