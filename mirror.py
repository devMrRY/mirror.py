l=[['*','*','*','*','*'],
    ['','*','*','*','*'],
     ['','','*','*','*'],
      ['','','','*','*'],
       ['','','','','*']]
def cal_edges(l):
    x=0;c=0;
    for i in l:
        x+=1
        y=0
        for j in i:
            y+=1
            if c<y:
                c=y
    return(x,c)

def mirror(w,e,t,side='left'):
    if side=="left" or side=="right":
        a=[]
        for i in range(0,w):
            a.append([])
            for j in range(0,e):
                a[i].append(t[i][e-j-1])   
        return(a)

    if side=="up" or side=="down":
        a=[]
        for i in range(0,w):
            a.append([])
            for j in range(0,e):
                a[i].append(t[w-i-1][j])   
        return(a)
    
def join(first,sec,fsoi,feoi,fsoj,feoj,ssoi,seoi,ssoj,seoj,side='right'):
    t=[]
    xmin=min(fsoi,ssoi)
    ymin=min(fsoj,ssoj)
    xmax=max(feoi,seoi)
    ymax=max(feoj,seoj)
    if side=='right' or side=='left':
        for i in range(xmin,xmax+1) :
            t.append([])
            for j in range(fsoj,feoj+1):
                if i>=fsoi and i<=feoi: 
                    t[i].append(first[i][j])
                else:
                    t[i].append(' ')
        for i in range(xmin,xmax+1) :
              for j in range(ssoj,seoj+1):
                if i>=ssoi and i<=seoi: 
                    t[i].append(sec[i][j])
                else:
                    t[i].append(' ')
        return(t)

    if side=='up' or side=='down':
        for i in range(0,feoi+1) :
            t.append([])
            for j in range(0,ymax+1):
                if i>=fsoi and i<=feoi and j>=fsoj and j<=feoj: 
                    t[i].append(first[i][j])
                else:
                    t[i].append(' ')
        for i in range(ssoi,seoi+1) :
            t.append([])
            for j in range(0,ymax+1):
                if j>=ssoj and j<=seoj: 
                    t[feoi+1].append(sec[i][j])
                else:
                    t[feoi+1].append(' ')
            feoi+=1
        return(t)

x,c=cal_edges(l)
a=mirror(x,c,l,'up')    
z=join(l,a,0,4,0,4,1,3,0,4,'up')
for i in z :
    for j in i:
        print(j,end=" ")
    print()