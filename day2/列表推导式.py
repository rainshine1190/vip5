


list1 = [ i for i in range(1,100) if i%2 == 0 ]
print(list1)


#等价
list1 = []
for i in range(1,100):
    if i%2 == 0:
        list1.append(i)

print(list1)