import requests
import json


def get_ex_info(url):
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
