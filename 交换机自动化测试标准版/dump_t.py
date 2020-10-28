# coding=utf-8
import json
dict_config={'version_serial_number':'[A-Z]{2}\d{10}[A-Z]{1}\d{4}',
'version_number_port':'\d{2}',
'version_load_version':'\d\.\d',
'version_operation_code_version':'\d\.\d\.\d[A-Z]{1}\d',
'run_inter':'interface\sethernet\s\d\/\d',
'run_inter_vlan1':'ip\sadd\sdhcp',
'run_inter_craft':'ip\sadd\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',
'run_ssh_is_ena':'ip\sssh\sserver\senable',
'ddm_message':'DDM\sInformation',
'ddm_message_2':'DDM\sThresholds',
}
# with open('config.json','w') as obj:
#     json.dump(dict_config,obj)
#     obj.close()

wenjian='config.json'
with open(wenjian,'r') as obj_f:
    aaa=json.load(obj_f)

print(aaa)