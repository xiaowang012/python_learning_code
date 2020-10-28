#输入年月日
year=input('请输入年份：')
month=input('请输入月份：')
day=input('请输入日期：')

while True:
    try:
        year=int(year)
        month=int(month)
        day=int(day)
    except ValueError:
        print('类型错误！')
        year=input('请输入年份：')
        month=input('请输入月份：')
        day=input('请输入日期：')
    else:
        break

if year%4==0:
    print('闰年')
    if month==1:
        result=day
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')
    elif month==2:
        result=day+31
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')
    elif month==3:
        result=day+31+29
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')
    elif month==4:
        result=day+31+29+31
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')
    elif month==5:
        result=day+31+29+31+30
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')
    elif month==6:
        result=day+31+29+31+30+31
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')
    elif month==7:
        result=day+31+29+31+30+31+30
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')
    elif month==8:
        result=day+31+29+31+30+31+30+31
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')
    elif month==9:
        result=day+31+29+31+30+31+30+31+31
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')
    elif month==10:
        result=day+31+29+31+30+31+30+31+31+30
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')
    elif month==11:
        result=day+31+29+31+30+31+30+31+31+30+31
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')
    elif month==12:
        result=day+31+29+31+30+31+30+31+31+30+31+30
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')
else:
    print('平年')
    if month==1:
        result=day
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')
    elif month==2:
        result=day+31
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')
    elif month==3:
        result=day+31+29
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')
    elif month==4:
        result=day+31+29+31
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')
    elif month==5:
        result=day+31+29+31+30
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')
    elif month==6:
        result=day+31+29+31+30+31
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')
    elif month==7:
        result=day+31+29+31+30+31+30
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')
    elif month==8:
        result=day+31+29+31+30+31+30+31
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')
    elif month==9:
        result=day+31+29+31+30+31+30+31+31
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')
    elif month==10:
        result=day+31+29+31+30+31+30+31+31+30
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')
    elif month==11:
        result=day+31+29+31+30+31+30+31+31+30+31
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')
    elif month==12:
        result=day+31+29+31+30+31+30+31+31+30+31+30
        print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')

#print('你输入的日期为：'+str(year)+'年'+str(month)+'月'+str(day)+'日'+','+'它是第'+str(result)+'天。')