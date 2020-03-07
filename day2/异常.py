


def calc(a,b):
    try:
        print(a/c)
    except TypeError:
        print('类型错误')
        raise
    except NameError:
        print('该对象未声明')

a = int(input())
b= int(input())

calc(a,b)
