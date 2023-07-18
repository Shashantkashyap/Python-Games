def sum(a,b,c):
    return a+b+c
def printboard(Xvalue,Ovalue):
    zero = 'x' if Xvalue[0] else ('o' if Ovalue[0] else 0)
    one = 'x' if Xvalue[1] else ('o' if Ovalue[1] else 1)
    two = 'x' if Xvalue[2] else ('o' if Ovalue[2] else 2)
    three = 'x' if Xvalue[3] else ('o' if Ovalue[3] else 3)
    four = 'x' if Xvalue[4] else ('o' if Ovalue[4] else 4)
    five = 'x' if Xvalue[5] else ('o' if Ovalue[5] else 5)
    six = 'x' if Xvalue[6] else ('o' if Ovalue[6] else 6)
    seven = 'x' if Xvalue[7] else ('o' if Ovalue[7] else 7)
    eight = 'x' if Xvalue[8] else ('o' if Ovalue[8] else 8)


    print(f"{one} | {two} | {three}" )
    print(".........")
    print(f"{four} | {five} | {six}" )
    print(".........")
    print(f"{seven} | {eight} | {zero}")

def check(Xvalue,Ovalue,X,O):
    wins= [[1, 2, 3], [4, 5, 6], [7, 8, 0], [1, 4, 7], [2, 5, 8], [3, 5, 0], [1, 5, 0], [3, 5, 7]]
    for win in wins:
        if (sum(Xvalue[win[0]],Xvalue[win[1]],Xvalue[win[2]])==3):
            print(X,"win")
            return 1
        if (sum(Ovalue[win[0]],Ovalue[win[1]],Ovalue[win[2]])==3):
            print(O,"win")
            return 0
    return -1



X= input("Enter player 1 name ")
O=input("enter player 2 name ")
Xvalue=[0,0,0,0,0,0,0,0,0]
Ovalue=[0,0,0,0,0,0,0,0,0]
turn=1
while(True):
    printboard(Xvalue,Ovalue)
    if(turn==1):
        print(X," chance ",end="")
        value=int(input())
        Xvalue[value]=1
    else:
        print(O," chance ",end="")
        value = int(input())
        Ovalue[value]=1

    win=check(Xvalue,Ovalue,X,O)
    if (win!=-1):
        print("match END")
        break

    turn=1-turn
