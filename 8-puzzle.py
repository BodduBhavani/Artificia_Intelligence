s=[]
des=[]
d={}
directions={0:"up",1:"down",2:"left",3:"right"}
move_directions=[]
print("enter Source Matrix")
for i in range(3):
    a,b,c=map(int,input().split())
    s.extend([a,b,c])
print("enter destination Matrix")
for i in range(3):
    a,b,c=map(int,input().split())
    des.extend([a,b,c])
d={}
s=tuple(s)
des=tuple(des)
d[s]=(s,-1)
q=[(s,0)]
f=0

while q:
    cur,move_num=q[0]
    q.pop(0)
    if cur==des:
        f=1
        break
    for i in range(9):
        if cur[i]==0:
            idx=i
            break
    temp=list(cur)
    if idx>=3:
        a=temp[:]
        a[idx],a[idx-3]=a[idx-3],a[idx]
        a=tuple(a)
        if a not in d:
            d[a]=(cur,move_num+1)
            q.append((a,move_num+1))
            move_directions.append(directions[0])

    if idx<=5:
        a=temp[:]
        a[idx],a[idx+3]=a[idx+3],a[idx]
        a=tuple(a)
        if a not in d:
            d[a]=(cur,move_num+1)
            q.append((a,move_num+1))
            move_directions.append(directions[1])
    if idx%3!=2:
        a=temp[:]
        a[idx],a[idx+1]=a[idx+1],a[idx]
        a=tuple(a)
        if a not in d:
            d[a]=(cur,move_num+1)
            q.append((a,move_num+1))
            move_directions.append(directions[3])
    if idx%3!=0:
        a=temp[:]
        a[idx],a[idx-1]=a[idx-1],a[idx]
        a=tuple(a)
        if a not in d:
            d[a]=(cur,move_num+1)
            q.append((a,move_num+1))
            move_directions.append(directions[2])
if f==0:
    print("no solution")
else:
    print("solution")
    ans=[]
    while d[cur][1]!=-1:
        ans.append((cur,d[cur][1]))
        cur=d[cur][0]
    ans.reverse()
    for step,move_number in ans:
        print("move number:",move_number)
        print("move direction:",move_directions[move_number-1])
        c=0
        for j in range(3):
            for k in range(3):
                print(step[k+c*3],end=' ')
            print()
            c+=1
        print()
