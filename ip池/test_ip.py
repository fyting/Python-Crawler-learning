from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType

proxy = Proxy(
        {
            'proxyType': ProxyType.MANUAL,
            'httpProxy': '114.235.82.16:8118'  # 代理ip和端口
        }
    )
# 新建一个代理IP对象
desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
# 加入代理IP
proxy.add_to_capabilities(desired_capabilities)
driver = webdriver.PhantomJS(executable_path='E:/phantomjs/bin/phantomjs.exe',
                             desired_capabilities=desired_capabilities)
# 测试一下，打开使用的代理IP地址信息
driver.get('http://www.whatismyip.com.tw/')
print(driver.page_source)