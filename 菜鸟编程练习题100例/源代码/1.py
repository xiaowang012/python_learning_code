# #1-3红球，4-6黄球，7-12绿球
# for a in range(1,13):
#     for b in range(1,13):
#         for c in range(1,13):
#             for d in range(1,13):
#                 for e in range(1,13):
#                     for f in range(1,13):
#                         for g in range(1,13):
#                             for h in range(1,13):
#                                 if a!=b and a!=c and a!=d and a!=e and a!=f and a!=g and a!=h and b!=c and b!=d and b!=e and b!=f and b!=g and b!=h and c!=d and c!=e and c!=f and c!=g and c!=h and d!=e and d!=f and d!=g and d!=h and e!=f and e!=g and e!=h and f!=g and f!=h and g!=h and h!=g:
#                                     print(a,b,c,d,e,f,g,h)
            

zifuchuan='1 2 5 12 8 4 3 6'.split()
print(zifuchuan)
list_2=[]
for x in zifuchuan:
    x=int(x)
    if 1<=x<=3:
        abc='红'
    elif 4<=x<=6:
        abc='黄'
    elif 7<=x<=12:
        abc='绿'
    list_2.append(abc)

print(list_2)
    



# a=['aaa','kkk',111]

# #b c d
# b=a[0] 
# c=a[1]
# d=a[-1]
# print(b,c,d)



# #多重赋值
# b,c,d=a
# print(b,c,d)


# #
# a=(1,23,)