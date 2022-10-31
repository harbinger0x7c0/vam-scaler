#! env python
from sys import argv
from os import chdir
from plumbum.cmd import file, ls, magick, mkdir, rm, unzip, zip as archive

def process_var(varname):
    print(f"Preparing to unzip {varname}.")
    mkdir['-p', 'unzipped']()
    print("Unzipping...", end=' ')
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
        elif ('png' in entry or 'jpg' in entry):
            spaces_in_name = filename.count(' ')
            dimension = int(magick['identify', filename]().split()[spaces_in_name + 2].split('x')[0])
            if dimension > 1024:
                print(f"Scaling {filename}... ", end=' ')
                magick[filename, '-resize', '1024x1024', filename]()
                print("Done.")
        else:
            print(f"Nothing to do for {filename}.")

for varfile in argv[1:]:
    process_var(varfile)
