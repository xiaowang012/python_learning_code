import wmi

print("修改IP")
wmiService = wmi.WMI()

colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled = True)



if len(colNicConfigs) < 1:
    print("a")
    exit()

#获取第一个适配器的的设置
objNicConfig = colNicConfigs[0]


arrIPAddresses = ['192.168.1.136']
arrSubnetMasks = ['255.255.0.0']
arrDefaultGateways = ['192.168.1.1']
arrGatewayCostMetrics = [1]
arrDNSServers = ['192.168.1.3', '202.106.46.151', '202.106.0.20']
intReboot = 0

returnValue = objNicConfig.EnableStatic(IPAddress = arrIPAddresses, SubnetMask=arrSubnetMasks)
if returnValue[0] == 0:
    print("成功设置ip")
elif returnValue[0] == 1:
    print("成功设置ip")
    intReboot += 1
else:
    print("修改ip失败")
    exit()

