def yetAnotherSquare(inValue):
    import time
    #datadir='static/data/'
    datadir='./'
    inValue = int(inValue)
    fname = datadir+'int'+str(int(time.time()*100))+'.txt'
    with open(fname,'w') as f:
        f.write(str(inValue)+'\n')
    return inValue*inValue
