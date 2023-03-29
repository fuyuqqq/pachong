# 使用 selenium 模拟浏览器访问  利用切片有选择的选择先前爬取下来的链接 将数据保存下来并写入css文件。
from msedge.selenium_tools import Edge, EdgeOptions
import csv

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


def write_product_data_to_csv(file_path, product_data):
    with open(file_path, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(product_data)


# 给一个函数，获得商品的基本信息
def Spider_Product_Information(url):
    options = EdgeOptions()
    options.use_chromium = True
    options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"  # 浏览器的位置
    driver = Edge(options=options, executable_path=r"D:\下载\edgedriver_win64\MicrosoftWebDriver.exe")  # 相应的浏览器的驱动位置

    driver.get(url)
    # driver.implicitly_wait(10)
    try:
        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_class_name('p-price').text[2:])
    except TimeoutException:
        print("系统超时")

    try:
        价格 = driver.find_element_by_class_name('p-price').text[2:]
        旗舰店 = driver.find_element_by_xpath('//*[@id="crumb-wrap"]/div/div[2]/div[2]/div[1]/div/a').get_attribute(
            "title")
        品牌 = driver.find_element_by_xpath('//*[@id="parameter-brand"]/li/a').text
        原产地 = driver.find_element_by_xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[6]').get_attribute("title")
        商品名称 = driver.find_element_by_xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[1]').get_attribute("title")
        商品编号 = driver.find_element_by_xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[2]').get_attribute("title")
        国产进口 = driver.find_element_by_xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[8]').get_attribute("title")
        贮存条件 = driver.find_element_by_xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[7]').get_attribute("title")

        一条商品数据 = [[旗舰店, 品牌, 价格, 原产地, 商品名称, 商品编号, 国产进口, 贮存条件], ]
        print(一条商品数据[0])

        for product_data in 一条商品数据:
            write_product_data_to_csv('Product_Information.csv', product_data)

        print("这条数据已写入")
        driver.close()

    except:

        print('这条数据错了')
        write_product_data_to_csv('Product_Information_error.csv', [url])
        driver.close()
