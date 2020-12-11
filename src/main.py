import json
import requests

from src import constants, temp_data
from bs4 import BeautifulSoup


if __name__ == '__main__':

    try:
        response = requests.request(method='GET', url=constants.base_url, headers=constants.headers, verify=False, proxies=constants.proxies)

        if response.status_code != 200:
            print('地址访问失败，状态码为', response.status_code)

        else:
            print('打印整个页面的返回值>>>', response.text)


        # soup = BeautifulSoup(temp_data.text, 'html.parser')  # html 为下载的网页，lxml为解析器
        #
        # list_global_item_list = soup.find_all('div', class_='list-global__item')
        # for item in list_global_item_list:
        #     thumb = item.find('div', class_='list-global__thumb')
        #     thumb_a = thumb.find('a')
        #
        #     title = thumb_a['title']    # 标题
        #     print('文章标题: ', title)
        #
        #     detail_link = thumb_a['href'] # 详情链接
        #     print('详情链接: ', detail_link)
        #
        #     picture_source = thumb.find('picture').find_all('source')
        #     if (len(picture_source) > 1):
        #         source = picture_source[1]
        #         im = source['data-srcset']  # 封面图片
        #         print('封面图片: ', im)
        #
        #     print('')

    except Exception as e:
        print("Exception", e)
