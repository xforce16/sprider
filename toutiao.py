import json
import re
from urllib.parse import urlencode
from requests.exceptions import RequestException
import requests
from bs4 import BeautifulSoup


def get_one_page(offset):
    data = {
        'offset': '0',
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    respond = requests.get(url)
    try:
        if respond.status_code == 200:
            return respond.text
    except RequestException:
        print ('error')
        return None


def get_image(html):
    data = json.loads(html)
    if data and 'data'in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')


def get_page_detail(url):
    respond = requests.get(url)
    try:
        if respond.status_code == 200:
            return respond.text
    except RequestException:
        print ('error')
        return None


def parse_page(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.title.string
    image_pattern = re.compile('gallery: JSON.parse\\((.*?)\\),', re.S)
    results = re.findall(image_pattern, html)
    if results:
        result = json.loads(results[0])
        image = [s.get('url') for s in json.loads(result).get('sub_images')]
        return {
            'title': title,
            'image': image
        }


def main():
    html = get_one_page(0)
    urls = get_image(html)
    u = 'https://toutiao.com/group/6569889788726346247/'
    url = 'https://www.toutiao.com/a6569753279499076109/'
    #print (urls)
    for url in urls:
        if url != None:
            print(url)
            #print(type(url))
            #break
            h3 = url[:4]+'s'+url[4:]
            h4 = h3.replace('group/', 'a')
            h5 = get_page_detail(h4)
            h6 = parse_page(h5)
            print(h6)



            #result = parse_page(h2)
            #print (result)



if __name__ == '__main__':
    main()

