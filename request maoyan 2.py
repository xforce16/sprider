import requests
import json
import  re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

def get_one_html(url):
    responed = requests.get(url,headers=headers)
    if responed.status_code ==200:
        return responed.text
    return None


def parse_one_html(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score': item[5].strip() + item[6].strip()
        }

def write_to_json(content):
    with open('result.txt','a') as f:
        f.write(json.dumps(content,ensure_ascii=False).encode('utf-8'))


def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_html(url)
    for i in parse_one_html(html):
        write_to_json(i)

