import random 
number=random.randint(1,10)
ans=input('猜一個數字')
if int(ans)==int(number):
    print('恭喜')
else:
    print('噗噗')
