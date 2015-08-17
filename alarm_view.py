#!/usr/bin/env python3
"""
--------------------------------------------------------------
Alan Marchiori - Aug 2015
Bucknell University
--------------------------------------------------------------

Views alarm clock i/o trace files. Reads input lines from stdin.

File format is text-based with one event per line.

Each line is fixed width:



             BUZZER
             ---------\
                       \
            ALARM      |
            ---------\ |
                     | |
       timestamp     | |   Led1    Led2    Led3    Led4
|-------- 21 ------| | | |--7--| |--7--| |--7--| |--7--|
                   0 0 0 0000000 0000000 0000000 0000000
012345679
         0123456789
                   0                   
Here is a sample trace:


"""

import fileinput

def display_digit(d):
    """
     _
    | |
     -
    | |
     -
     """
     
    lines = []
        
    if d & 64 == 64:
        lines += [ ' _ ' ]
    else:
        lines += [ '   ' ]
    
    line = ''
    if d & 2 == 2:
        line += '| '
    else:
        line += '  '
    if d & 32 == 1:
        line += '|'
    else:
        line += ' '
    lines += [line]
    
    if d & 1 == 1:
        lines += [' - ']
    else:
        lines += ['   ']
     
    line = ''
    if d & 4 == 4:
        line += '| '
    else:
        line += '  '
    if d & 2 == 2:
        line += '|'
    else:
        line += ' '
    lines += [line]     
    
    if d & 8 == 8:
        lines += [' - ']
    else:
        lines += ['   ']
    
    return "\n".join (lines)
     
def show_line(line):
    p = line.strip().split()
    # parse timestamp as base 10 (default)
    ts = int(p[0])
    
    # parse remaining arguments in binary
    alarm, buz = map(lambda x: int(x, 2), p[1:3])
    digits = map(lambda x: int(x, 2), p[3:])
    
    for d in digits:
        print (d, display_digit(d))

if __name__=="__main__":
    for line in fileinput.input():  # read stdin
        show_line(line)

