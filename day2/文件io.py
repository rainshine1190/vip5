
with open('data.txt','r' ) as file:
    # text = file.read()
    # print(text)
    #让每次的光标移动到首行的第一个字符前面
    # file.seek(0)
    # row1 = file.readline()
    # print(row1)


    rows = file.readlines()
    print(rows)

    for i in rows:
        m = i.strip('\n')
        print(m)