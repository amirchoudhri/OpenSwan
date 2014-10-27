from _elementtree import parse
from __builtin__ import int
fortigate_model = ""
while fortigate_model not in ['1', '2', '3', '4', '5', '6', '7']:
    print """Which FortiGate Model is being used:
    1.  60D
    2.  100D
    3.  200D
    4.  300D
    5.  500D
    6.  600C
    7.  800C
Select a number between 1-7: """
    fortigate_model = raw_input ()



dicts_from_file = []
with open('data.txt','r') as inf:
    for line in inf:
        dicts_from_file.append(eval(line))   


print dicts_from_file[int(fortigate_model)-1]
