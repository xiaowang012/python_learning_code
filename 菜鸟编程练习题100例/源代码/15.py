#学习成绩的分组

while True:    
    fenshu=input('输入你的学习成绩，按回车结束：')
    try:
        fenshu=int(fenshu)
    except ValueError:
        print('请输入正常的数值：')
        fenshu=input('请输入您的学习成绩，按回车结束：')
    else:
        break

def grades(fenshu):
    if fenshu>=90:
        return 'A'
    elif fenshu<=89 and fenshu>=60:
        return 'B'
    elif fenshu<60:
        return 'C'

print(grades(fenshu))

