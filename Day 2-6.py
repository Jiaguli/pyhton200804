names=[] 
scores=[]
totl=0
highest=0
lowest=100
avg=0
x=input('班上有幾個人')
x = int(x)
for j in range(x):
    name=input('你是誰')
    names.append(name)
    score=input('你幾分')
    scores.append(score)
    totl=int(score)+int(totl)
avg=int(totl)/int(x)
print('班上的平均是',avg)
for i in range(x):
    num=int(scores[i])
    if int(num)>int(highest):
        highest=scores[i]
    else:
        highest=int(highest)
print('班上最高分是',highest,'分')
for w in range(x):
    num=int(scores[w])
    if int(num)<int(lowest):
        lowest=scores[w]
    else:
        lowest=int(lowest)
print('班上最低分是',lowest,'分')