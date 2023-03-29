from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from msedge.selenium_tools import Edge, EdgeOptions

options = EdgeOptions()
options.use_chromium = True
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"  # 浏览器的位置
driver = Edge(options=options, executable_path=r"D:\下载\edgedriver_win64\MicrosoftWebDriver.exe")  # 相应的浏览器的驱动位置
# driver.implicitly_wait(10)
driver.get('https://item.jd.com/10057421571809.html')

# WebDriverWait(driver, 20).until(lambda driver:driver.find_element_by_class_name('p-price').text[2:])


# 价格 = driver.find_element_by_xpa('/html/body/div[6]/div/div[2]/div[4]/div/div[1]/div[2]/span[1]/span[2]').text
价格 = driver.find_element_by_class_name('p-price').text[0:]
print(价格)


# 旗舰店 = driver.find_element_by_xpath('//*[@id="crumb-wrap"]/div/div[2]/div[2]/div[1]/div/a').text
# 品牌 = driver.find_element_by_xpath('//*[@id="parameter-brand"]/li/a').text
# 原产地 = driver.find_element_by_xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[6]').text[4:]
# 商品名称 = driver.find_element_by_xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[1]').text[5:]
# 商品编号 = driver.find_element_by_xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[2]').text[5:]
# 国产进口 = driver.find_element_by_xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[8]').text[6:]
# 贮存条件 = driver.find_element_by_xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[7]').text[5:]
#
# 一条商品数据 = [[旗舰店, 品牌, 价格, 原产地, 商品名称, 商品编号, 国产进口, 贮存条件], ]
# print(一条商品数据)
# driver.close()
