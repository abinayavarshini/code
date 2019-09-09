no=int(input())
x,y=map(int,input().split())
if(no in range(x,y+1)):
   print("yes")
else:
    print("no")
