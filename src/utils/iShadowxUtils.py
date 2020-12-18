import re

import requests

from data import ishadowx_temp_data
from src import constants
from bs4 import BeautifulSoup


def start():
    """
    获取免费ss账号信息
    :return:
    """

    try:
        response = requests.request(method='GET', url=constants.ishadowx_url, headers=constants.headers, verify=False)

        if response.status_code != 200:
            print('地址访问失败，状态码为', response.status_code)

        else:
            # print('打印整个页面的返回值>>>', response.text)

            # markup = ishadowx_temp_data.text  # 临时数据
            markup = response.text

            soup = BeautifulSoup(markup, 'html.parser')  # html 为下载的网页，lxml为解析器

            list_global_item_list = soup.find_all('div', class_='portfolio-item')
            for item in list_global_item_list:
                hover_text = item.find('div', class_='hover-text')
                ip_text = hover_text.find('span', id=re.compile("ip*"))
                port_text = hover_text.find('span', id=re.compile("port*"))
                pw_text = hover_text.find('span', id=re.compile("pw"))
                method_text = hover_text.find_all('h4')[-2]

                if ip_text is not None:
                    print('IP: ', str(ip_text.text).strip())
                    print('Port: ', str(port_text.text).strip())
                    print('Password: ', str(pw_text.text).strip())
                    print('Method: ', method_text.text[str(method_text.text).index(':') + 1:].strip())
                    print('')

    except Exception as e:
        print("Exception", e)
