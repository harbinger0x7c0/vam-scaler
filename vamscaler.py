#! env python
from sys import argv
from os import chdir
from plumbum.cmd import file, ls, magick, mkdir, rm, unzip, zip as archive

def process_var(varname):
    print("Preparing to unzip.")
    mkdir['-p', 'unzipped']()
    print("Unzipping...")
    unzip[varname, '-d', 'unzipped']()
    print("Done.")
    rm[varname]()
    print("Scaling...")
    scale_directory('unzipped')
    print(f"Reassembling {varname}")
    chdir('unzipped')
    files_to_add = ls().split('\n')[:-1]
    cmd = archive['-r', "../" + varname, files_to_add]
    print(cmd)
    cmd()
    chdir('..')
    print("Done.")
    print("Cleaning up.")
    rm['-rf', 'unzipped']()
    print("Finished")

def scale_directory(directory_name):
    for entry in ls[directory_name]().split('\n')[:-1]:
        filename = directory_name + '/' + entry
        if 'directory' in file[filename]():
            print(f"Descending into {filename}...")
            scale_directory(filename)
        elif ('png' in entry or 'jpg' in entry) and '4096x4096' in magick['identify', filename]():
            print(f"Scaling {filename}... ",)
            magick[filename, '-resize', '1024x1024', filename]()
            print("Done.")
        else:
            print(f"Nothing to do for {filename}.")

for varfile in argv[1:]:
    process_var(varfile)
