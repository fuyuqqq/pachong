# 导入所需要的库
import requests
import time
from bs4 import BeautifulSoup


# 获取网页内容函数
def get_html(w_url):
    # 写了两个headers，用于意外爬虫被限制时的备用选项。
    headers_0 = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      # 'Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.51'
        'Chrome/84.0.4147.105 Safari/537.36'
        ,

        'accept-language': 'zh-CN,zh;q=0.9'
    }
    headers_1 = {
        "Origin": "http://www.jd.com/",
        "Referer": "http://www.jd.com/",
        "Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "text/html;q=0.9,p_w_picpath/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/3.0 AppleWebKit/537.36 (KHTML,Gecko) Chrome/3.0.w4.",
        "Cookie": "__utmz=qwer2434.1403499.1.1.utmcsr=www.jd.com|utmccn=("
                  "refrral)|utmcmd=rferral|utmcct=/order/getnfo.action; _pst=xx89; pin=x9; unick=jaa; "
                  "cshi3.com=D6045EA24A6FB9; _tp=sdyuew8r9e7r9oxr3245%3D%3D; user-key=1754; cn=0; ipLocation=%u7F0C; "
                  "ipLoc97; areaId=1; mt_ext2%3a%27d; "
                  "aview=6770.106|68|5479.665|675.735|6767.100|6757.13730|6ee.9ty711|1649.10440; "
                  "atw=65.15.325.24353.-4|188.3424.-10|22; __j34|72.2234; __jdc=2343423; __jdve|-; __jdu=3434 "
    }
    headers_2 = {
        'Referer': 'http://www.jd.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    headers_3 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    headers_4 = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }

    response = requests.get(w_url, headers=headers_0)  # 请求访问网站
    if response.status_code == 200:
        html = response.text  # 获取网页内容
        soup = BeautifulSoup(html, 'lxml')
        return soup  # 返回网页内容
    else:
        print(url + "获取网站信息失败！")


# 获取商品信息网址函数
def get_prod_attr_inf_urls(w_url):
    # 用于存放链接
    with open("Product_attribute_information.txt", "w") as f:
        with open("Product_com_information.txt", "w") as p:
            # 获取页面内容
            f_soup = get_html(w_url)

            # 要知道一共有多少页商品
            page = f_soup.find('div', id='J_topPage', class_='f-pager').find('i').get_text()

            # 获取每一页内的商品链接
            for i in range(int(page)):
                print('共' + str(page) + '页商品，正在获取第' + str(i + 1) + '页商品链接')
                f_url_1 = w_url + '&page=' + str(2 * i + 1)
                f_soup_1 = get_html(f_url_1)
                time.sleep(7)
                ul = f_soup_1.find('ul', class_='gl-warp clearfix')
                li_list = ul.find_all('li')
                for li in li_list:
                    data_sku = li.get('data-sku')
                    f.write('https://item.jd.com/' + str(data_sku) + '.html' + '\n')
                    p.write('https://item.jd.com/' + str(data_sku) + '.html' + '#comment' + '\n')
            f.close()
            p.close()


if __name__ == '__main__':
    # 拼凑链接
    url = 'https://search.jd.com/Search?keyword=阳光玫瑰葡萄'
    # url = 'https://search.jd.com/Search?keyword=' + input('请输入要搜索的商品: ')
    # 获取每一个商品的链接
    get_prod_attr_inf_urls(url)
