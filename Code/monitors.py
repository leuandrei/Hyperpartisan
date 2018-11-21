import aspectlib

@aspectlib.Aspect
def fileMonitorPrinter(f):
    if f.closed:
        print("Write in closed file!")


@aspectlib.Aspect
def fileMonitorOpen(f, path):
    if f.closed:
        f=open(path, "w")