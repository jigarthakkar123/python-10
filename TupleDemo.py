t=(1,10,1.1,"tops",[10,20,30],True,"python")

print(t)
for i in t:
    print(i)
print(10 in t)
print(t.count(1))
print(t.index(10))
print(t[4])
t[4].append(40)
print(t)
