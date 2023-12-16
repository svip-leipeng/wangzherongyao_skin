import os
import requests
import time
import random
from fake_useragent import UserAgent

url = 'https://pvp.qq.com/web201605/js/herolist.json'
herolist = requests.get(url)
herolist_json = herolist.json()
hero_name = list(map(lambda x: x['cname'], herolist_json))
hero_number = list(map(lambda x: x['ename'], herolist_json))

def downloadPic():
    i = 0
    for j in hero_number:
        os.makedirs("C:\\Users\\XXXXX\\XXXX\\skin\\" + hero_name[i])
        os.chdir("C:\\Users\\XXXXX\\XXXX\\skin\\" + hero_name[i])
        i += 1
        for k in range(10):
            onehero_link = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(j) + '/' + str(j) + '-bigskin-' + str(k) + '.jpg'
            ua = UserAgent()
            headers = {'User-Agent': ua.random}
            im = requests.get(onehero_link, headers=headers)
            if im.status_code == 200:
                open(str(k) + '.jpg', 'wb').write(im.content)
            time.sleep(random.randint(10, 20))

downloadPic()
