import random 
number=random.randint(1,20)
time=5
ans=input('猜一個數字')
while int(ans)!=int(number) and time>0:
    print('噗噗')
    time=int(time) - 1
    if int(ans)>int(number):
        print('太大了!')
    else:
        print('太小了!')
    ans=input('再猜一個數字')
if int(ans)==int(number):
    print('恭喜!')
else:
    print('結束遊戲!你真廢!')