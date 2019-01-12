numb = int(input())
for j in range(numb):
    a = input()
    b = a.replace('X',' ')
    b = b.split()
    res = 0
    for i in range(len(b)):
        for j in range(1,len(b[i])+1):
           res +=j

    print(res)
