import json
import re

import requests
from  bs4 import BeautifulSoup
url = 'https://www.toutiao.com/a6569753279499076109/'


def get_image(url):
    respond = requests.get(url)
    try:
        if respond.status_code ==200:
            return respond.text

    except requests.RequestException:
        print ('error')

def get_image_detail(html):
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    image_pattern = re.compile('gallery: JSON.parse\\((.*?)\\),',re.S)
    results = re.findall(image_pattern,html)
    result = json.loads(results[0])
    image = [s.get('url') for s in json.loads(result).get('sub_images')]
    return {
        'title' : title,
        'image' : image
    }




if __name__ == '__main__':
    html = get_image(url)

    h = get_image_detail(html)

    print(h)







