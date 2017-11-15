h,j=input,range
r=int(h()[0])
g=[]
for i in j(r):
 g.append(h().split())
n=int(h())
for i in j(n):
 f=0
 a,b,x,y=map(int,h().split())
 for c in j(a,x+1):
  f+=g[c][b:y+1].count('1')
 print(f)
