#coding=utf-8
import ftplib

'''
ftp = FTP()					# 获取FTP对象
ftp.set_debuglevel(2)		# 打开调试级别2，显示详细信息
ftp.connect('IP', PORT)	# 连接ftp，server和端口
ftp.login('user', 'password')  # 登录用户
print(ftp.getwelcome())     # 打印欢迎信息
ftp.cmd('xxx/xxx')			# 进入远程目录
bufsize = 1024				# 设置缓存区大小
filename='filename.txt'     # 需要下载的文件
file_handle=open(filename, 'wb').write   # 以写的模式在本地打开文件
file.retrbinary('RETR filename.txt', file_handle,bufsize)  # 接收服务器上文件并写入本地文件
ftp.set_debuglevel(0)       # 关闭调试模式
ftp.quit					# 退出ftp
ftp.cwd(pathname)			# 设置FTP当前操作的路径
ftp.dir()					# 显示目录下所有目录的信息
ftp.nlst()					# 获取目录下的文件
ftp.mkd(pathname)			# 新建远程目录
ftp.rmd(dirname)			# 删除远程目录
ftp.pwd()					# 返回当前所在位置
ftp.delete(filename)		# 删除远程文件
ftp.rename(fromname, toname)    #将fromname改为toname
ftp.storbinaly('STOR filename.txt',file_handel,bufsize)  # 上传目标文件 
ftp.retrbinary('RETR filename.txt',file_handel,bufsize)  # 下载FTP文件 '''


def ftp_x(usera,passd,server_host_ip,port):
    '''一个简单的ftp登录服务器实例'''
    try:
        ftp_response=ftplib.FTP()
        ftp_response.connect(server_host_ip,port)
    except:
        print('open ftp server error!')
    else:
        ftp_response.set_debuglevel(2)
        print('user login!')
        try:
            ftp_response.login(usera,passd)
        except:
            print('password or username error!')
        else:
            print(ftp_response.getwelcome())
            ftp_response.cmd('xxx/xxx')			# 进入远程目录
            bufsize = 1024				# 设置缓存区大小
            filename='filename.txt'     # 需要下载的文件
            file_handle=open(filename, 'wb').write   # 以写的模式在本地打开文件
            file.retrbinary('RETR filename.txt', file_handle,bufsize)  # 接收服务器上文件并写入本地文件
            ftp_response.set_debuglevel(0)  
            ftp_response.quit()


ftp_x('admin','123456','192.168.1.1',20)