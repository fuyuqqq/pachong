from Spider_Product_Information import Spider_Product_Information


if __name__ == '__main__':
    i = 1
    # 打开文件
    with open("Product_attribute_information.txt", "r") as file:
        # 读取文件的所有行
        lines = file.readlines()

        # 按照给定的链接获取信息
        for line in lines[0:10]:
            url = line.strip()
            print("正在爬取第" + str(i) + "个链接：" + url + "的商品信息")
            i = i + 1
            # 进行爬虫并将数据保存进csv文件
            # 搞一个循环，循环爬取保存
            Spider_Product_Information(url)
        print("------爬取结束------")

