import sys
#always file managing inside of try block
try:
    f = open(sys.argv[1],"rt",encoding="utf-8")
    for line in f:
        sys.stdout.write(line)
finally:
    f.close()

# Alternative method, using with the file is always closed!
with open(sys.argv[1],"rt",encoding="utf-8") as f:
    for line in f:
        sys.stdout.write(line)

