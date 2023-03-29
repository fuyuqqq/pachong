from pc_urls import get_html
import time

# 打开文件
with open("Product_attribute_information.txt", "r") as file:
    # 读取文件的所有行
    lines = file.readlines()

# 按照给定的链接获取信息
for line in lines[9:10]:
    url = line.strip()
    print("url = " + url)
    soup = get_html(url)

    # 获取信息 店名,
    Store_name = soup.find('div', class_='J-hove-wrap EDropdown fr').find('div', class_='name').find('a').get_text()
    price = soup.find('div', class_='summary summary-first')
    xinxi = soup.find('div', class_='summary-price J-summary-price')
    print(xinxi)
