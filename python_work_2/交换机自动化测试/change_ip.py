# -*- coding: utf-8 -*-
import wmi

print('正在修改IP,请稍候...')
wmiService = wmi.WMI()
colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled = True)
if len(colNicConfigs) < 1:
    print('没有找到可用的网络适配器')
    exit()


objNicConfig = colNicConfigs[0]
print(colNicConfigs)

arrIPAddresses = ['192.168.100.100']
arrSubnetMasks = ['255.255.255.0']
arrGatewayCostMetrics = [1]

returnValue = objNicConfig.EnableStatic(IPAddress = arrIPAddresses, SubnetMask =arrSubnetMasks)


