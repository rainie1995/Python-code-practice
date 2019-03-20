from selenium import webdriver
import time
browser = webdriver.Chrome()
# 登录微博
"""
implicitly_wait():隐式等待
当使用了隐式等待执行测试的时候，如果 WebDriver没有在 DOM中找到元素，将继续等待，超出设定时间后则抛出找不到元素的异常
换句话说，当查找元素或元素并没有立即出现的时候，隐式等待将等待一段时间再查找 DOM，默认的时间是0
一旦设置了隐式等待，则它存在整个 WebDriver 对象实例的声明周期中，隐式的等待会让一个正常响应的应用的测试变慢，
它将会在寻找每个元素的时候都进行等待，这样会增加整个测试执行的时间。
implicitly_wait(5)属于隐式等待，5秒钟内只要找到了元素就开始执行，5秒钟后未找到，就超时；
time.sleep(5)表示必须等待5秒定位；
"""
def weibo_login(username, password):
    # 打开微博登录页
    browser.get('https://passport.weibo.cn/signin/login?display=0&retcode=6102')
    browser.implicitly_wait(5)
    time.sleep(1)
    # 填写登录信息：用户名、密码
    browser.find_element_by_id("loginName").send_keys(username)
    browser.find_element_by_id("loginPassword").send_keys(password)
    time.sleep(1)
    # 点击登录
    browser.find_element_by_id("loginAction").click()
    time.sleep(1)
# 设置用户名、密码
username = '18851190398'
password = "mym@1249690440"
weibo_login(username, password)