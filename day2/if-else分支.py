
#if分支
# a = int(input('please input a value:'))
#
# if a>0:
#     a += 1
#
# print('a的值为：',a)



#if-else分支

# a = int(input('please input a value:'))
#
# if a>0:
#     a += 1
# else:
#     a -= 1
#
# print('a的值为：',a)


#if-else嵌套分支

a = int(input('please input a value:'))

if a>0:
    a += 1
elif a == 0:
    a -= 1
else:
    a -= 2

print('a的值为：',a)