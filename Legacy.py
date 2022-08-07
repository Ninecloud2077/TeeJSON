import getopt
import sys

Opts,Args=getopt.getopt(sys.argv[1:],
'fkv:',
['file=','key=','value='])

FileName=KeyName=ValueName=None

for name,value in Opts:
    if name in ('-f','--file'):
        FileName=value
    elif name in ('-k','--key'):
        KeyName=value
    elif name in ('-v','--value'):
        ValueName=value

if not FileName:
    print('Invaild File Name:'+FileName)
    exit()