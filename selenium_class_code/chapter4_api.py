#介绍了selenium的API
#webdriver的原理
#webdriver的功能

from selenium import webdriver
from time import sleep

#定义浏览器
driver=webdriver.Firefox()
driver.get('http://iqianhai.sznews.com')

#获取当前页面的URL地址
print(driver.current_url)

#获取当前的窗口句柄
handle=driver.current_window_handle
print('当前的窗口句柄为：'+handle)

#获取当前session里所有的窗口句柄
handles=driver.window_handles
print('当前session里所有的窗口句柄为：'+str(handles))

#获取该实例底层所使用的浏览器名称(Firefox)
name_1=driver.name
print('当前所使用的浏览器为：'+name_1+' '+'浏览器')

#获取当前设备的方位  ？？？
#driver.orientation

#获取当前页面的源代码
source_1=driver.page_source
print('源代码为：'+str(source_1))

#获取当前页面的标题
title_web=driver.title
print('网页标题为：'+title_web)


#################################
#webdriver的方法

# #页面后退
# driver.back()

# #关闭当前浏览器窗口
# driver.close()

# #页面前进
# driver.forward()

# #访问目标url
# driver.get(url)

# #浏览器窗口最大化
# driver.maximize_window()

# #退出当前的driver并关闭所有的相关窗口
# driver.quit()

# #刷新页面
# driver.refresh()

# #返回当前页面唯一焦点所在的元素或者元素体
# driver.switch_to_active_element()

# #把焦点切换至当前弹出的警告
# driver.switch_to_alert()

# #切换焦点至默认框架内
# driver.switch_to_default_content()

# #通过索引、名称、网页元素将焦点切换至指定的框架，这种方法也适用于IFRAMES
# #其参数为：frame_reference,要切换的目标窗口的名称，整数类型的索引或者要切换的目标框架的网页元素
# driver.switch_to_frame(frame_reference)

# #切换到指定窗口,参数为窗口名称或者窗口句柄
# driver.switch_to_window(handle)

# #超时等待目标元素被找到,参数为等待时间(秒)
# driver.implicitly_wait(100)

# #设置一个页面完全加载完成的超时等待时间,(秒)
# driver.set_page_load_timeout(100)

# #设置脚本的执行超时时间，应该在execute_async_script抛出错误之前,(秒)
# driver.set_script_timeout(100)

# #######################################################
# #WebElement接口
# #WebElement的功能

# element=driver.find_elements_by_name('xx')
# #获取元素的大小
# element.size

# #获取元素的HTML标签的名称
# element.tag_name

# #获取元素的文本值
# element.text

# #webelemet的方法

# #清楚文本框或者文本域中的内容
# element.clear()

# #单击元素
# element.click()

# #获取元素的属性值,参数为元素名称
# element.get_attribute('xx')

# #检查元素对于用户是否可见
# element.is_displayed()

# #检查元素是否可用
# element.is_enabled()

# #检查元素是否被选中，应用于复选框和单选按钮
# element.is_selected()

# #模拟输入文本
# element.send_keys('xxx')

# #用于提交表单，如果对于一个元素使用这个方法，将提交该元素所属的表单
# element.submit()

# #获取css属性的值，参数为CSS属性的名称
# element.value_of_css_property(property_name)

# ##############################################
# #Select原理
# #select是selenium中一个特定的类，用于与下拉菜单和列表交互

# #select功能

# #获取下拉菜单和列表中被选中的所有选项内容
# select_element.all_selected_options

# #获取下拉菜单和列表的第一个选项/当前选择项
# select_element.first_selected_option

# #获取下拉菜单和列表的所有选项
# select_element.options 

# #Select的方法

# #清除多选下拉菜单和列表的所有选择项
# select_element.deselect_all()

# #根据索引清除下拉菜单和列表的选择项
# #参数，index：要清除目标选择项的索引
# select_element.deselect_by_index(index)

# #清除所有选项值和给定参数匹配的下拉菜单，和列表的选择项
# #参数为：value，目标选择项的value值
# select_element.deselect_by_value(value)

# #清除所有展示的文本和给定参数匹配的下拉菜单和列表的选择项，
# #参数:text,要清除目标选择项的文本值
# select_element.deselect_by_visible_text(text)

# #根据索引选择下拉菜单和列表的选择项
# #参数：index，要选择的目标选择项的索引
# select_element.select_by_index(index)

# #选择所有选项值和给定参数匹配的下拉菜单和列表的选择项
# #参数，value 要选择的目标选择项的value属性
# select_element.select_by_value(value)

# #选择所有展示的文本和给定参数匹配的下拉菜单和列表的选择项
# #参数text 要选择的目标选择项的文本值
# select_element.select_by_visible_text(text)

# #################################################
# #操作警告和弹出框
# #Alert原理，selenium webdriver通过Alert类来操控javascript警告，其包含的方法有接受，驳回，输入和获取警告的文本
# #Alert的功能

# #获取警告窗口的文本
# alert.text()

# #Alert的方法

# #接受JavaScript警告信息，单击OK按钮
# alert.accept()

# #驳回JavaScript警告信息，单击取消按钮
# alert.dismiss()

# #模拟输入信息
# #参数：字符串
# alert.send_keys('xx')





