import json

zidian={"user_name":"admin","password":"123456","management_ip":"192.168.1.1","local_ip":"192.168.x.x","vlan_ip_1":"192.168.x.x","subnet_1":"255.255.255.0"}
filename="user_set_2.json"
with open(filename,'w') as f_obj:
    json.dump(zidian,f_obj)