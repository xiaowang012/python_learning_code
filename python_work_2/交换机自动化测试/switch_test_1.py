import winreg
import json
import os
import keyboard


print("gala_win_7_64_")
print('')
print("按TAB键自动切换1G全双工和100M全双工....")
print("")
print("注册表中网卡的属性所在的路径可自行更换，在json文件中....")
print("")
print("正在获取当前配置和网卡信息....")
#读取json文件中的注册表地址
wenjian2='reg_ip_1.json'
with open(wenjian2) as file_object:
   regadress=json.load(file_object)

#读取注册表代码块(ip地址和子网掩码)
key=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,regadress)
name,key_1=winreg.QueryValueEx(key,"SubnetMask")#注意这里的文件路径使用双斜杠，因为py不允许0开头
name_1,key_2=winreg.QueryValueEx(key,"IPAddress")
print("当前的本地IP地址为："+name_1[0])
print("当前的子网掩码为："+name[0])




def inter_rest():
  '''重新加载网卡'''
  os.system('"netsh interface set interface name="以太网" admin=Disable"')
  os.system('netsh interface set interface name="以太网" admin=Enable')

def update_reg_1G():
  '''修改注册表键值为1G'''
  key_2=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,regadress,0,winreg.KEY_ALL_ACCESS)
  winreg.SetValueEx(key_2,"*SpeedDuplex",0,winreg.REG_SZ,value_1[-1])#1G全双工

def update_reg_100M():
  '''修改注册表属性为100M'''
  key_2=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,regadress,0,winreg.KEY_ALL_ACCESS)
  winreg.SetValueEx(key_2,"*SpeedDuplex",0,winreg.REG_SZ,value_1[-2])#100M全双工



#a=0
#jt=True
#value_1=["0","1","2","3","4","6"]#速率双工模式对应6个键值
#print("开始监听键盘.....")
#while jt:
 # keyboard.wait("TAB")
 # a+=1
 # if a%2==0:
  #  update_reg_1G()
  #  inter_rest()
   # print("reboot of network card successful")
  #  print("您已经修改为1Gbps-full-duplex")
    
 # else:
  #  update_reg_100M()
  #  inter_rest()
  #  print("reboot of network card successful")
   # print("您已经修改为100Mbps-full-duplex")
    



user_setting={"user_name":"admin","password":"123456","management_ip":"192.168.1.1","local_ip":"192.168.x.x","vlan_ip_1":"192.168.x.x"}