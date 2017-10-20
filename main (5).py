file = open("running-config.cfg","r")

mylist = []
for myline in file:
    mylist = line.split()
    print(mylist)
for i in mylist:
    if 'accesmylist' in line:
       print(line)
    if 'vlan' in myline:
        print(myline)