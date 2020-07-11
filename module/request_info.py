import requests
import json
from bs4 import BeautifulSoup


def get_ex_info(url):
    '''
    This method is used to get comic info from ex.
    :param url: Ex URL to get comic id and token
    '''
    # 获取链接信息
    gallery_info = url.split('/')
    gallery_id = int(gallery_info[-3])
    gallery_token = str(gallery_info[-2])
    gid_list = [gallery_id, gallery_token]
    
    # 构造JSON参数
    data = {
        "method": "gdata",
        "gidlist": [gid_list],
        "namespace": 1
    }
    json_data = json.dumps(data)
    
    API_URL = "https://api.e-hentai.org/api.php"

    # 发送请求
    response = requests.post(API_URL, data=json_data)
    
    return response.json()


def get_fav_count(url):
    '''
    This method is used to get comic's favourite count info from ex.
    :param url: Ex URL to get comic link
    '''
    # U-A msg to avoid Anti_Crawler
    with open('config/header.json', 'r', encoding='utf-8') as header_file:
        headers = json.load(header_file)

    page = requests.get(url, headers=headers)
    
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        fav_count = soup.find("td", attrs={"class": "gdt2","id": "favcount"}).string
        return fav_count
    else:
        print('ERROR:%d' % page.status_code)


if __name__ == '__main__':
    print(get_fav_count(321))