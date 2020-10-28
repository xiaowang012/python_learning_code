#coding=utf-8
import paramiko


'''一个简单的ssh2协议的实例
   3个基础名词：
   Channel：是一种类socket ，一种安全的SSH传输通道
   Transport:是一种加密的会话，使用时会同步创建一个加密的Tunnels(通道)
   Session: 是一种client和server保持连接的对象，用connect()/start_client()/start_server()开始会话

   包含两个组件：SSHClient，SFTPClient

    SSHClient：常用参数
    hostname 连接的目标主机
    port=SSH_PORT 指定端口
    username=None 验证的用户名
    password=None 验证的用户密码
    pkey=None 私钥方式用于身份验证
    key_filename=None 一个文件名或文件列表，指定私钥文件
    timeout=None 可选的tcp连接超时时间
    allow_agent=True, 是否允许连接到ssh代理，默认为True 允许
    look_for_keys=True 是否在~/.ssh中搜索私钥文件，默认为True 允许
    compress=False, 是否打开压缩

    set_missing_host_key_policy()：设置远程服务器没有在know_hosts文件中记录时的应对策略

    AutoAddPolicy 自动添加主机名及主机密钥到本地HostKeys对象，不依赖load_system_host_key的配置。即新建立ssh连接时不需要再输入yes或no进行确认
    WarningPolicy 用于记录一个未知的主机密钥的python警告。并接受，功能上和AutoAddPolicy类似，但是会提示是新连接
    RejectPolicy 自动拒绝未知的主机名和密钥，依赖load_system_host_key的配置。此为默认选项

    exec_command()：在远程服务器执行Linux命令的方法。
    open_sftp()：在当前ssh会话的基础上创建一个sftp会话。该方法会返回一个SFTPClient对象。'''


def ssh2X(hostname,port,user,passw):
    '''ssh2'''  
    try:
        client=paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname,port,user,passw)#client.connect(hostname='192.168.1.105', port=22, username='root', password='123456')
    except:

        print('login error')
    else: 
        #打开一个Channel并执行命令
        stdin,stdout,stderr=client.exec_command('xxx')#stdout为正确输出，stderr错误输出，
        
        #读取执行的结果
        result=stdout.read().decode('utf-8')
        print(result)
        
        #关闭sshclient
        client.close()           
        
 

'''SFTPClient的常用方法
SFTPCLient作为一个sftp的客户端对象，根据ssh传输协议的sftp会话，实现远程文件操作，如上传、下载、权限、状态
from_transport(cls,t) 创建一个已连通的SFTP客户端通道
put(localpath, remotepath, callback=None, confirm=True) 将本地文件上传到服务器 参数confirm：是否调用stat()方法检查文件状态，返回ls -l的结果
get(remotepath, localpath, callback=None) 从服务器下载文件到本地
mkdir()   在服务器上创建目录
remove()  在服务器上删除目录
rename()  在服务器上重命名目录
stat()    查看服务器文件状态
listdir() 列出服务器目录下的文件
'''


def sftp_1():
    # 获取Transport实例
    tran = paramiko.Transport(('10.0.0.3', 22))
    
    # 连接SSH服务端，使用password
    tran.connect(username="root", password='123456')

    # 或者配置私人密钥文件位置
    # private = paramiko.RSAKey.from_private_key_file('/Users/root/.ssh/id_rsa')
    # # 连接SSH服务端，使用pkey指定私钥
    # tran.connect(username="root", pkey=private)
    
    # 获取SFTP实例
    sftp = paramiko.SFTPClient.from_transport(tran)
    
    # 设置上传的本地/远程文件路径
    localpath = "/Users/root/Downloads/1.txt"
    remotepath = "/tmp/1.txt"
    
    # 执行上传动作
    sftp.put(localpath, remotepath)
    # 执行下载动作
    sftp.get(remotepath, localpath)
    
    tran.close()
