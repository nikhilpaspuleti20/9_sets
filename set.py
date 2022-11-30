'''
DATE=29th NOV 2022
DAY= monday
TOPIC= set
AUTHOR= nikhil
'''
t={4,2.3,'nikhil',('hi',5)}
print(t,type(t)) #{'nikhil',('hi',5),2.3,4} set
r={4,8,7}
# print(r[1]) #typeerror:'set' object is not subscriptable
p={3,5,6}
m='p',8,6
p.add(m)
print(p) #{3,('p',8,6),5,6}
h={4,5,6}
h.clear()
print(h) #set()
a={1,2,3};b={4,5,6};c={7,8,9};d={9,6,3}
print(a.intersection(b)) #set()
print(a.intersection(c)) #set()
print(a.intersection(d)) #{3}
print(b.intersection(d)) #{6}
d={1,3,'hello'}
y={5,7,'hey'}
print(a.union(b)) #{1,2,3,4,5,6}
print(b.union(a)) #{1,2,3,4,5,6}
l={7,5};h={3,5};k={6,7}
l.update(h)
l.update(k)
print(l) #{3,5,6,7}
p={6,7,8,9};k={8,7,3}
print(p.difference(k)) #{9,6}
print(k-p)#{3}