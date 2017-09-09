#!/usr/bin/env python -tt


#Import
import sys

import os

import shutil

'''
filenames = os.listdir(dir) -- list of filenames in that directory path (not including . and ..). The filenames are just the names in the directory, not their absolute paths.
os.path.join(dir, filename) -- given a filename from the above list, use this to put the dir and filename together to make a path
os.path.abspath(path) -- given a path, return an absolute form, e.g. /home/nick/foo/bar.html
os.path.dirname(path), os.path.basename(path) -- given dir/foo/bar.html, return the dirname "dir/foo" and basename "bar.html"
os.path.exists(path) -- true if it exists
os.mkdir(dir_path) -- makes one dir, os.makedirs(dir_path) makes all the needed dirs in this path
shutil.copy(source-path, dest-path) -- copy a file (dest path directories should exist)
'''


def main():
  dir = sys.argv[1]
  fileNames = os.listdir(dir)
  
  for file in fileNames:
    print file
    print
    pth = os.path.join(dir, file)
    print os.path.abspath(pth) ## print os.path.abspath(os.path.join(dir, file))
  shutil.copy('C:\Users\El-Machina\iCloudDrive\Documents\Workspace\Python\hello.py', 'C:\Users\El-Machina\iCloudDrive\Documents\Workspace\Python\MyScripts')  

# Standard boilerplate for calling main
if __name__ == '__main__':
  main()
