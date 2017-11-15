l,r=input,range
t=l()
for _ in r(int(t)):
 c,s=l(),l()
 k=[]
 for i in r(int(s)):
  k.append(list(map(int,input().split())))
 for z in k:
  if z[1]==4:z[1]=9
  if z[1]==3:z[1]=4
 v=int(input())
 q=[]
 for i in r(v+1):
  for m in q:
   m[1]-=1
   if m[1]==0:q.remove(m)
  q.extend([j for j in k if j[0]==i])
 print(q)
