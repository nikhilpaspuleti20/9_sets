'''
DATE=29th NOV 2022
DAY= monday
TOPIC= set
AUTHOR= nikhil
'''
d={36,25,43}
d.discard(45)
print(d) #{25,43,36}
d.discard(25)
print(d) #{43,36}
c={7,3,8,15}
c.pop()
print(c) #{3,7,15}
g={1,2,3,4};f={5,6,7};d={4,5,6}
print('Are g and f disjoint?',g.isdisjoint(f))#Are g and f disjoint? True
print('Are g and d disjoint?',g.isdisjoint(d))#Are g and d disjoint? False
print('Are f and d disjoint?',d.isdisjoint(d))#Are f and d disjoint? False
b={1,2,3};v={1,2,3,4,5};c={4,5,6}
print(b.issubset(v)) #True
print(v.issubset(b)) #False
print(c.issubset(v)) #False
x={5,7,3}
# x.remove(25)
# print(x) #keyerroe:25
m={3,6,7};n={3,6,7,2,4}
print(m.issuperset(n)) #False
print(n.issuperset(m)) #True