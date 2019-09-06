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
# writes ttl to "out.ttl"
def ivr_2_ttl(file):
  f = open(file, "r")
  o_file = open("out.txt","w+")

  fl = f.readlines()

  for x in fl:
    field = x.split("\t")
    o_file.write("fid:"+field[0]+" f:segment_number \""+field[2]+"\"\n")
    o_file.write("fid:"+field[0]+" f:segment_length \""+field[6]+"\"\n")
    switcher = {
       "1": "f:pb2_genbank",
       "2": "f:pb1_genbank",
       "3": "f:pa_genbank",
       "4": "f:ha_genbank",
       "5": "f:np_genbank",
       "6": "f:na_genbank",
       "7": "f:m_genbank",
       "8": "f:ns_genbank"
    }
    strain=field[7].split("(")[1].split(")")[0]
    o_file.write("fid:"+strain+" "+switcher.get(field[2],"f:invalid_genbank")+" \""+field[0]+"\"\n")
    o_file.write("fid:"+field[0]+" f:strain \""+strain+"\"\n")
    o_file.write("fid:"+strain+" f:host \""+field[1]+"\"\n");
    o_file.write("fid:"+strain+" f:subtype \""+field[3]+"\"\n");
    o_file.write("fid:"+strain+" f:country \""+field[4]+"\"\n");
    o_file.write("fid:"+strain+" f:col_date \""+field[5]+"\"\n");

  f.close()
  o_file.close()
  

def main():
#  print(arguments)
  ivr_2_ttl(arguments['<influenza_na.dat>'])

if __name__ == '__main__':
  arguments = docopt(__doc__, version='IVR(influenza_na.dat) > Turtle(ttl) v0.1')
  main()
