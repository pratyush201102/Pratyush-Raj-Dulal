a=open("rank.txt","r")
b=a.readlines()
squares=[]
for i in range(len(b)):
    c=(b[i])
    my_list=(c.split())
    mynewlist = [s for s in my_list if s.isdigit()]
    if mynewlist[3]=="11":
        d=mynewlist[2]
        squares.append(int(d))
print(sorted(squares))    
