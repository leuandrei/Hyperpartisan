from monitors import fileMonitorPrinter

def open_out_file():
    fileout = open("out.txt", "w")

    fileout.write('Leustean M. Andrei')

    fileout.close()

    fileout.write('Alex VDS')


open_out_file()
