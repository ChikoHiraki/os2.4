import glob
import sys

Path = sys.argv[1]
lang = sys.argv[2]
file = glob.glob(Path + "/**/*." + lang, recursive=True)

for i in file:
    print(i)