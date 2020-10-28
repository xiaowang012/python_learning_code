|#coding=utf-8
from telnetlib import Telnet
import unittest
import HTMLTestRunner
import re
import json
import os
import sys 
import time 
import paramiko
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import serial

#Initialization configuration
print('Check configuration\n>>>>>>>>>>>>>>>>')
if os.path.isfile('user.json')==False:
     print('configuration not found! please enter:\n')
     host_ip=input('management_ip:')
     user_name=input('user:')
     password=input('password:')
     local_ip=input('Please enter the local IP address you want to modify:\n')
     serial_1=input('Serial Port(COM1/2/3/4...):')
     bps_1=input('baud rate(9600/115200...):')

     #add to list
     set_list=[]
     set_list.append(host_ip)
     set_list.append(user_name)
     set_list.append(password)
     set_list.append(local_ip)
     set_list.append(serial_1)
     set_list.append(bps_1)

     #write in json file
     wenjian='user.json'
     with open(wenjian,'w') as obj:
         json.dump(set_list,obj)
else:
    #read json config
    wenjian2='user.json'
    with open(wenjian2,'r') as obj2:
        set_list=json.load(obj2)
    
#check set_list 
if len(set_list)==6:
    if set_list[0]!='' and set_list[1]!='' and set_list[2]!='':
        print('pass')
        if set_list[3]!='':
            host_ip,user_name,password,local_ip,serial_1,bps_1=set_list
            ipRegex=re.compile(r'\d{1,3}')
            mo1=ipRegex.findall(host_ip)
            mo2=ipRegex.findall(local_ip)
            if len(mo1)==4 and len(mo2)==4:
                if 0<int(mo1[0])<255 and 0<=int(mo1[1])<255 and 0<=int(mo1[2])<255 and 0<int(mo1[3])<255:
                    if 0<int(mo2[0])<255 and 0<=int(mo2[1])<255 and 0<=int(mo2[2])<255 and 0<int(mo2[3])<255:
                        print('pass')
                        if int(mo1[0])==int(mo2[0]) and int(mo1[1])==int(mo2[1]) and int(mo1[2])==int(mo2[2]):
                            print('The two addresses in the same segment')
                            if int(mo1[3])==int(mo2[3]):                                
                                print('The two addresses cant be the same')
                            else:
                                m='netsh interface ip set address "以太网" static '+local_ip+' '+"255.255.255.0"
                                os.system(m)
                                print('Modify local successfully!')
                                print('Conduct Ping packet testing!')
                                m2='ping'+' '+host_ip
                                a_1=os.popen(m2)
                                time.sleep(5)
                                text=a_1.read()
                                print(text)
                                #find TTL >=1
                                local_ping_hostRegex=re.compile(r'[A-Z]{3}')
                                mo10=local_ping_hostRegex.findall(text)
                                if mo10 and len(mo10)>=1:
                                    print('Telnet login！')
                                else:
                                    print('Ping package failed!')
                                    time.sleep(2)
                                    sys.exit()
                        else:
                            print('The two addresses are not in the same segment')
                            time.sleep(2)
                            sys.exit()
                    else:
                        print('local_ip OUT!')
                        time.sleep(2)
                        sys.exit()  
                else:
                    print('host_ip OUT!')
                    time.sleep(2)
                    sys.exit()       
            else:
                print('host_ip can not found')
                time.sleep(2)
                sys.exit()   
        else:
            #without local_ip
            host_ip=set_list[0]
            user_name=set_list[1]
            password=set_list[2]
            serial_1=set_list[4]
            bps_1=set_list[5]
            ip_2Regex=re.compile(r'\d{1,3}')
            mo3=ip_2Regex.findall(host_ip)
            if len(mo3)==4:
                if 0<int(mo3[0])<255 and 0<=int(mo3[1])<255 and 0<=int(mo3[2])<255 and 0<int(mo3[3])<255:
                    print('pass')
                    print('Telnet login！')
                else:
                    print('host_ip OUT!')
                    time.sleep(2)
                    sys.exit()                    
            else:
                print('host_ip can not found!')
                time.sleep(2)
                sys.exit()                    
    else:
        print('Lost management_ip or user or password!')
        time.sleep(2)
        sys.exit()
else:
    print('unknown ERROR!')
    time.sleep(2)
    sys.exit()

#Create a test class for the switch
class SwitchTest(unittest.TestCase):
    '''CLI TEST'''
    @classmethod
    def setUpClass(self):
        self.host_ip=host_ip
        self.user_name=user_name
        self.password=password
        self.serial_1=serial_1
        self.bps_1=bps_1
        print('Configuration initialized successfully!\nStart testing the switch!\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        try:
            self.tn=Telnet()
            self.tn.open(host_ip,port=23,timeout=10)
            time.sleep(2)
            self.tn.read_until(b'username:',timeout=2)
            self.tn.write(user_name.encode('ascii')+b'\n')
            self.tn.read_until(b'password:',timeout=2)
            self.tn.write(password.encode('ascii')+b'\n')
            time.sleep(2)
            self.tn.read_until(b'switch#',timeout=2)
        except:
            print('ERROR\nTest results:\n')
        else:
            print('successful login to switch\nTest results:\n')

    #@unittest.skip('test')
    def test_a_version(self):
        '''查看版本信息'''
        tn=self.tn
        tn.write(b'show version\n')
        time.sleep(5)
        result=tn.read_very_eager().decode('ascii')
        #creat regex
        serialnumberRegex=re.compile(r'[A-Z]{2}\d{10}[A-Z]{1}\d{4}')
        version_portRegex=re.compile(r'\d{2}')
        version_loadRegex=re.compile(r'\d\.\d')
        version_sofwareRegex=re.compile(r'\d\.\d\.\d[A-Z]{1}\d')      
        mo1=serialnumberRegex.findall(result)
        mo2=version_portRegex.findall(result)
        mo3=version_loadRegex.findall(result)
        mo4=version_sofwareRegex.findall(result)
        if len(mo1)==1:
            x=True
        else:
            x=False
        self.assertTrue(x,'the serial number error!')
        re_2=mo2[-1]
        self.assertEqual(re_2,'28','the port number error!')
        re_3=mo3[0]
        self.assertEqual(re_3,'1.4','the load version error!')
        re_4=mo4[0]
        self.assertEqual(re_4,'1.6.9R2','the software version error!')

    #@unittest.skip('test')  
    def test_b_run(self):
        '''查看配置信息'''
        tn=self.tn
        tn.write(b'show running-config\n')
        time.sleep(5)
        tn.write(b' ')
        tn.write(b' ')
        tn.write(b' ')
        tn.write(b' ')
        tn.write(b' ')
        tn.write(b' ')
        tn.write(b' ')
        tn.write(b' ')
        tn.write(b' ')
        tn.write(b' ')
        tn.write(b' ')
        time.sleep(5)
        result_1=tn.read_very_eager().decode('ascii')
        run_interRegex=re.compile(r'interface\sethernet\s\d\/\d{1,2}')
        run_vlan1Regex=re.compile(r'ip\sadd\sdhcp')
        run_intercraftRegex=re.compile(r'ip\sadd\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
        run_ssh_is_enaRegex=re.compile(r'ip\sssh\sserver\senable')
        mo5=run_interRegex.findall(result_1)
        mo6=run_vlan1Regex.findall(result_1)
        mo7=run_intercraftRegex.findall(result_1)
        mo8=run_ssh_is_enaRegex.findall(result_1)
        # print(mo5)
        # print(mo6)
        # print(mo7)
        # print(mo8)
        re_5=len(mo5)
        self.assertEqual(re_5,28,'the port number(run) error!')
        re_6=mo6[0]
        self.assertEqual(re_6,'ip add dhcp','the vlan1 error!')
        re_7=mo7[0]
        self.assertEqual(re_7,'ip add 192.168.1.1 255.255.255.0','the management_ip error!')
        re_8=mo8[0]
        self.assertEqual(re_8,'ip ssh server enable','the ssh server is close error!')
        
    #@unittest.skip('test')      
    def test_d_ddm(self):
        '''是否可以查看DDM'''
        tn=self.tn
        tn.write(b'show tran\n')
        time.sleep(3)
        tn.write(b' ')
        tn.write(b' ')
        tn.write(b' ')
        tn.write(b' ')
        time.sleep(5)
        result_2=tn.read_very_eager().decode('ascii')
        ddmmessageRegex=re.compile(r'DDM\sInformation')
        ddmmessageRegex_2=re.compile(r'DDM\sThresholds')
        mo9=ddmmessageRegex.findall(result_2)
        mo10=ddmmessageRegex_2.findall(result_2)
        re_9=len(mo9)
        re_10=len(mo10)
        self.assertEqual(re_9,4,'can not find DDM Error!')
        self.assertEqual(re_10,4,'can not find DDM Error!')
       
    #@unittest.skip('test')
    def test_e_ssh2(self):
        '''SSH2是否可以连通'''
        try:
            client=paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname='192.168.1.1',port=22,username='admin',password='admin')#client.connect(hostname='192.168.1.105', port=22, username='root', password='123456')
        except:
            print('error')
            x=False
        else: 
            client.close()           
            x=True
        self.assertTrue(x,'SSH2 service test Error!')

    #@unittest.skip('test')
    def test_f_serial(self):
        '''串口是否可以连通'''
        # portx="COM5"

        # #bps：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
        # bps=bps_1

        #time out
        timex=10
        # open serial 
        ser=serial.Serial(serial_1,bps_1,timeout=timex)
        # write 

        ser.write(b"\n")
        time.sleep(5)
        
        #read
        if ser.read_until('User Access Verification'):
            x=True
        else:
            x=False
        ser.close()
        self.assertTrue(x,'Serial connection failed, error')
    
    #@unittest.skip('test')
    def test_g_web(self):
        
        '''用FireFox登录web页面'''
        driver=webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(30)
        url='http://'+host_ip
        try:
            driver.get(url)
            time.sleep(3)
            ele=driver.find_element_by_id('username')
            ele.clear()
            ele.send_keys(user_name)
            ele_1=driver.find_element_by_id('password')
            ele_1.clear()
            ele_1.send_keys(password)
            ele_3=driver.find_element_by_id('loginbutton')
            ele_3.click()
            time.sleep(10)
        except:
            x=False
        else:
            x=True
        driver.close()
        self.assertTrue(x,'web browser login failed, Error!')  

    #@unittest.skip('test')
    def test_h_set_vlan1(self):
        '''创建一个vlan1地址并检查'''
        tn=self.tn
        tn.write(b'conf ter\n')
        time.sleep(1)
        tn.write(b'interface vlan 1\n')
        time.sleep(1)
        tn.write(b'no ip add\n')
        time.sleep(1)
        tn.write(b'ip add 192.168.2.123 255.255.255.0\n')
        time.sleep(1)
        tn.write(b'exit\n')
        tn.write(b'exit\n')
        tn.write(b'show run\n')
        time.sleep(3)
        result=tn.read_very_eager().decode('ascii')
        vlanipRegex=re.compile(r'\d{3}\.\d{3}\.\d{1}\.\d{3}\s\d{3}\.\d{3}\.\d{3}\.\d{1}')
        mo12=vlanipRegex.findall(result)
        re_12=mo12[0]
        self.assertEqual(re_12,'192.168.2.123 255.255.255.0','Failed to modify vlan address')
    
    #@unittest.skip('test')
    def test_c_sys(self):
        '''检查OID,温度,MAC地址'''
        tn=self.tn
        tn.write(b'show system\n')
        time.sleep(2)
        result_4=tn.read_very_eager().decode('ascii')
        #print(result_4)
        MacRegex=re.compile(r'\d{2}\-\d{1}[A-Z]{1}\-\d{2}')
        OIDRegex=re.compile(r'\d\.\d\.\d\.\d\.\d\.\d\.\d{5}\.\d\.\d\.\d{2}\.\d{3}')
        tempRegex=re.compile(r'\d{2}\sdegrees')
        mo13=MacRegex.findall(result_4)
        mo14=OIDRegex.findall(result_4)
        mo15=tempRegex.findall(result_4)
        re17=mo13[0]
        re14=mo14[0]
        re15=mo15[0]
        self.assertEqual(re17,'64-9D-99','MAC address ERROR!')
        self.assertEqual(re14,'1.3.6.1.4.1.52642.2.1.45.101','OID ERROR!')
        m=[]
        for a in re15:
            m.append(a)
        temp=int(m[0])*10+int(m[1])*1
        if -15<temp<75:
            x=True
        else:
            x=False
        self.assertTrue(x,'temperature out of range!')
        
            
        


        



    # def test_spanning_tree(self):


    @classmethod
    def tearDownClass(self):
        '''Reboot the switch and close the Telnet server'''
        self.tn.close()


    













    # @classmethod
    # def tearDownClass(self):
    #     '''close the firefox'''


if __name__ == "__main__":
    unittest.main()



