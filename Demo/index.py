# jiujiu
def jiujiu(n,m):
    for i in range(1,n):
        for j in range(1,m):
            if (j>i):
                break
            else:
                print(j,'*',i,'=',i*j,end='  ')
        print('\n')
jiujiu(10,10)

def Pascal_riangle(n,m):
    line = [1]
    while True:
        yield line
        line = [1] + [line[i] + line[i + 1] for i in range(len(line) - 1)] + [1]


    # for i in range(1,n+1):
    #     for space in range(0,n-i):
    #         print(' ',end=' ')
    #     for j in range(0,i*2-1):
    #         if(j==0 or j==i*2-2):
    #             print(1,end=' ')
    #         else:
    #             print('$',end=" ")
    #     print("")
Pascal_riangle(10,10)


