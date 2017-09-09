#!/usr/bin/env python -tt

# Import
import sys
import os
import shutil
import re
import commands

def GetSpecialFiles(dir):
  files = os.listdir(dir)
  specialFiles = []
  for file in files:
    match = re.search(r'\w+__+\w+__.+', file)
    if match:
      specialFiles.append(os.path.abspath(os.path.join(dir, match.group())))
  return specialFiles

def CopyToDir(paths, dest):
  for src in paths:
    spclFilesDir = GetSpecialFiles(src)
    for pth in spclFilesDir:
      if not os.path.exists('./'+dest):
        os.mkdir('./'+dest)
      shutil.copy(pth, dest)
  return

def ZipItUp(paths, zipName):
  #zip -j zipfile <list all the files>
  cmd2Zip =  'zip -j ' + zipName

  for src in paths:
    spclFilesDir = GetSpecialFiles(src)
    for pth in spclFilesDir:
      cmd2Zip = cmd2Zip + ' ' + pth
    print 'About to run:', cmd2Zip
    (status, output) = commands.getstatusoutput(cmd2Zip)
    if status:
      sys.stderr.write(output)
      print
      sys.exit(1)
    print output

  return


def main():

  args = sys.argv[1:]

  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]"
    sys.exit(1)

  if args[0] == '--todir':
    copy2Dir = args[1]
    del args[0:2]
    print args[0:]
    CopyToDir(args[0:], copy2Dir)   
  elif args[0] == '--tozip':    
    zipName = args[1]
    del args[0:2]
    ZipItUp(args[0:], zipName)


if __name__ == '__main__':
  main()  