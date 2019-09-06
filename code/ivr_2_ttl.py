#! /usr/bin/env python3
# Auth: Jennifer Chang
# Date: 2019/09/06

"""IVR infleunza_na.dat > turtle file

Usage:
  ivr_2_ttl.py <influenza_na.dat>

Options:
  -h --help   Show this screen.
  --version   Show version
"""

from docopt import docopt

# file = "influenza_na.dat"
# writes ttl to "out.txt"
def ivr_2_ttl(file):
  f = open(file, "r")
  o_file = open("out.txt","w+")

  fl = f.readlines()
  for x in fl:
    fl.split("\t")
    o_file.write(x)

  f.close()
  o_file.close()
  

def main():
#  print(arguments)
  ivr_2_ttl(arguments['<influenza_na.dat>'])

if __name__ == '__main__':
  arguments = docopt(__doc__, version='IVR(influenza_na.dat) > Turtle(ttl) v0.1')
  main()
