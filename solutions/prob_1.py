import json
d=json.load(open('../inputs/1.json'))
x=d['devices']
y=d['bans']
a=len(x)
for i in x:
 for j in y:
  if i[j['key']]==j['value']:a-=1
print(a)
