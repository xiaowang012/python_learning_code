i=input('请输入本月的业绩I(按enter确认)(单位:万元)：')

#这一段代码不断的int(),直到不出错才break
while True:
    try:
        i=int(i)
    except ValueError:
        print('请输入正确的数字！')
        i=input('请输入本月的业绩I(按enter确认)：')
    else:
        break 

if i<=10:
    money=0.1*i
    print('可以获得的奖金为：'+str(money)+'万元')
elif i>10 and i<20:
    money=10*0.1+0.075*(i-10)
    print('可以获得的奖金为：'+str(money)+'万元')
elif i>=20 and i<=40:
    money=(i-20)*0.05+10*0.1+0.075*(i-10)
    print('可以获得的奖金为：'+str(money)+'万元')
elif i>40 and i<=60:
    money=(i-40)*0.03+(i-20)*0.05+10*0.1+0.075*(i-10)
    print('可以获得的奖金为：'+str(money)+'万元')
elif i>60 and i<=100:
    money=(i-60)*0.015+(i-40)*0.03+(i-20)*0.05+10*0.1+0.075*(i-10)
    print('可以获得的奖金为：'+str(money)+'万元')
elif i>100:
    money=(i-100)*0.01+(i-60)*0.015+(i-40)*0.03+(i-20)*0.05+10*0.1+0.075*(i-10)
    print('可以获得的奖金为：'+str(money)+'万元')