fhand=open('mbox.txt')
#print(fhand)
for lx in fhand:
    lxstrip=lx.strip()
    #print(lxstrip)
    upper=lxstrip.upper()
    print(upper)