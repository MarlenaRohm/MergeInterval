def MERGE(*args):
    if len(args) < 2:     #if not more then 2 intervals are given, the script stops
        print("Only possible with at least two intervals as input")
        return
    args=sorted(args) #sorts the arguments
    new=None #temporarily saves a merged interval
    newlist = [] #this will be the list of merged intervals
    length = True 
    x=0 
    y=0 
    while (length):
        for arg in args:
            y=y+1
            x=x+1
            #last argument (or if merged before, the last merge) is added into the newlist without being compared again and script stops
            if len(args) == y:
                if new is not None:
                    newlist.append(new)
                else:
                    newlist.append(s)
                length=False
                return newlist
            else:
                #if nothing is merged yet "new" will be none. The current and next argument will be compared
                if new is None: 
                    f=arg
                    s=args[x] 
                    new=domerge(f,s)
                    #if there was nothing to merge (None as output from domerge()) the current argument will be saved in "newlist" without creating duplicates
                    if (new is None) and (f not in newlist): 
                        newlist.append(f)
                else:
                    #if there was something merged before, it will be used as new current argument and will be compared with next argument
                    f=new 
                    s=args[x]
                    new=domerge(f,s)
                    if (new is None) and (f not in newlist):
                        newlist.append(f)
                        

#actual merge function
def domerge(f,s):
    for i in range(f[0],f[-1]+1): #goes through the interval of current argument/previously merged
        for j in range(s[0],s[-1]+1): #goes through the interval of the next argument
            #if intervals overlap or are consecutive, first digit in current argument becomes first number in new merge (it was sorted previously), highest number of arguments will be last number in new merge
            if i == j:
                a=f[0] 
                if f[-1]>=s[-1]:
                    b=f[-1]
                else:
                    b=s[-1]
                new=[a,b]
                return new
            elif (i+1 == j) or (i-1 == j):
                a=f[0]
                if f[-1]>=s[-1]:
                    b=f[-1]
                else:
                    b=s[-1]
                new=[a,b]
                return new
            #if last is reached without overlap/consecutive stop without output
            elif i == f[-1]: 
                return None

#example:
MERGE([25,30],[2,19],[14,23],[4,8]) 
