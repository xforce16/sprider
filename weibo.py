import requests
from urllib.parse import urlencode
base_url='https://m.weibo.cn/api/container/getIndex?'
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

def get_one_page(page):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    url=base_url+urlencode(params)
    try:
        responed = requests.get(url,headers=headers)

        if responed.status_code ==200:
            return responed.json()
    except requests.ConnectionError as e:
        print ('ERROR',e.args)








