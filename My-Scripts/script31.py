#!/usr/bin/env python -tt


#Import
import sys

import os

import commands


def main():
  dir = sys.argv[1] 
  cmd = 'ls -l ' + dir
  print "Command to run:", cmd   ## good to debug cmd before actually running it
  (status, output) = commands.getstatusoutput(cmd)
  if status:    ## Error case, print the command's output to stderr and exit
    sys.stderr.write(output)
    sys.exit(1)
  print output  ## Otherwise do something with the command's output
  
if __name__ == '__main__':
  main()
