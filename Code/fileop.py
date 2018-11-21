
path = "file.txt"

f = open(path, "w")

f.write("This should work")
f.close()
f.write("This should be caught by the monitor")
