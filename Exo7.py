

def splitor(dic1,dic2):
    dic ={}

    for item in dic1:
        x=0
        for item2 in dic2:
            if item == item2:
                x+=1
                dic[item] = dic1[item[0]]+dic2[item2[0]]
        if x==0:
            dic[item] = dic1[item[0]]

    for item2 in dic2:
        x=0
        for item2 in dic2:
            if item == item2:
                x+=1
        if x==0:
            dic[item2] = dic2[item2[0]]

    return dic



print(splitor({'a' : 100, 'b' : 200, 'c':300, 'x':2},{'a' : 300, 'b' : 200, 'd':400, 'x':555555}))
