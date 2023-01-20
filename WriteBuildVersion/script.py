#!/usr/bin/env python3

# This script checks for the file "BuildVersion.h" and replaces it with the
# correct semver numbers from the git history (these are inputs)

import fileinput
import sys
import os

def main(filepath, major, minor, patch, pre_release_tag, pre_release_number):
    # Figure out which pre-release index to use
    if(not pre_release_tag.isnumeric() and not pre_release_number.isnumeric()):
        build = '0'
    elif(pre_release_tag.isnumeric()):
        build = pre_release_tag
    else:
        build = pre_release_number

    # We first check to see if the file exists
    if (os.path.isfile(filepath)):
        print("Updating BuildVersion.h with "+major+"."+minor+"."+patch+"+"+build)

        for line in fileinput.input(filepath, inplace = 1):
            if "major" in line:
                print(line.replace("0", major).rstrip())
            elif "minor" in line:
                print(line.replace("0", minor).rstrip())
            elif "patch" in line:
                print(line.replace("0", patch).rstrip())
            elif "build" in line:
                print(line.replace("0", build).rstrip())
            else:
                print(line.rstrip())
    
    else:
        print("BuildVersion.h not found. Skipping this step")


if __name__ == '__main__':
    # Get major, minor, and patch versions from inputs
    if len(sys.argv) < 5:
        sys.exit("Correct usage needs at least: script.py <file_path> <major version> <minor number> <patch number>")

    filepath = sys.argv[1]
    major = sys.argv[2]
    minor = sys.argv[3]
    patch = sys.argv[4]
    
    try:
        pre_release_tag = sys.argv[5]
    except:
        pre_release_tag = ''
        
    try:
        pre_release_number = sys.argv[6]
    except:
        pre_release_number = ''

    main(filepath, major, minor, patch, pre_release_tag, pre_release_number)
