d={908:"Meet",765:"Sagar",545:"Kuldip",235:"Uttam"}

print(d)
print(d[765])
d[545]="Jigar"
print(d)
d[111]="Kuldip"
print(d)
for i in d:
    print(i," : ",d[i])
print(d.get(111))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(545))
print(d)
print(d.popitem())
d1={545:"Jigar",111:"Kuldip",222:"Jeet",333:"Himanshu"}
d.update(d1)
print(d)
