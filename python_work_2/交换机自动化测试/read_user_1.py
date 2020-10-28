import sys
import time
import json

#读取用户配置文件json,相对路径
wenjian="user_set_2.json"
with open(wenjian) as file_object:
   user_setting=json.load(file_object)
   
print(user_setting)
user_setting_list_name=[]
user_setting_list_values=[]
for a,values in user_setting.items():
    user_setting_list_name.append(a)
    user_setting_list_values.append(values)

print(user_setting_list_name)
print(user_setting_list_values)

#检查列表中的属性是否有问题，有问题则退出，
def check_user_setting():
    if "user_name" not in user_setting_list_name:
        print("缺少用户名属性！！请检查user_setting.json中是否有user_name!!")
        time.sleep(2)
        sys.exit()
    elif 'password' not in user_setting_list_name:
        print("缺少密码属性！！请检查user_setting.json中是否有password!!")
        time.sleep(2)
        sys.exit()
    elif 'management_ip' not in user_setting_list_name:
        print("缺少管理口IP属性！！请检查user_setting.json中是否有management_ip！！")
        time.sleep(2)
        sys.exit()
    elif 'local_ip' not in user_setting_list_name:
        print("缺少本地ip属性！！请检查user_setting.json中是否有local_ip！！")
        time.sleep(2)
        sys.exit()
    elif 'vlan_ip_1'not in user_setting_list_name:
        print("缺少Vlan地址属性！！请检查user_setting.json中是否有vlan_ip_1！！")
        time.sleep(2)
        sys.exit()
    elif "subnet_1" not in user_setting_list_name:

        print("缺少子网掩码属性！！请检查user_setting.json中是否有subnet_1!!")
        time.sleep(2)
        sys.exit()

#执行检查列表的函数，没有问题才会执行下一步，有问题会退出。   
check_user_setting()

#给变量赋值(多重赋值)
user_name,password,management_ip,local_ip,vlan_ip_1,subnet_1=user_setting_list_values
print(user_name)
print(password)
print(management_ip)
print(local_ip)
print(vlan_ip_1)
print(subnet_1)

    



