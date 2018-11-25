def MERGE(*args):
    if len(args) < 2:
        print("Nur möglich mit mindestens zwei Intervallen")
        return
    args=sorted(args)
    new=None
    newlist = []
    length = True 
    x=0
    y=0
    while (length):
        for arg in args:
            y=y+1
            x=x+1
            if len(args) == y:
                if new is not None:
                    newlist.append(new)
                else:
                    newlist.append(s)
                length=False
                return newlist
            else:
                if new is None:
                    f=arg
                    s=args[x]
                    new=domerge(f,s)
                    if (new is None) and (f not in newlist):
                        newlist.append(f)
                else:
                    f=new
                    s=args[x]
                    new=domerge(f,s)
                    if (new is None) and (f not in newlist):
                        newlist.append(f)
                        


def domerge(f,s):
    for i in range(f[0],f[-1]+1):
        for j in range(s[0],s[-1]+1):
            if i == j:
                if f[0]<=s[0]:
                    a=f[0]
                else:
                    a=s[0]
                if f[-1]>=s[-1]:
                    b=f[-1]
                else:
                    b=s[-1]
                new=[a,b]
                return new
            elif (i+1 == j) or (i-1 == j):
                if f[0]<=s[0]:
                    a=f[0]
                else:
                    a=s[0]
                if f[-1]>=s[-1]:
                    b=f[-1]
                else:
                    b=s[-1]
                new=[a,b]
                return new
            elif i == f[-1]:
                return None

MERGE([25,30],[2,19],[14,23],[4,8]) 
