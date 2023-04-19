import os
import requests

url = 'https://pvp.qq.com/web201605/js/herolist.json'
herolist = requests.get(url)  # 获取英雄列表json文件

herolist_json = herolist.json()  # 转化为json格式
hero_name = list(map(lambda x: x['cname'], herolist.json()))  # 提取英雄的名字
hero_number = list(map(lambda x: x['ename'], herolist.json()))  # 提取英雄的编号


# 下载图片
def downloadPic():
    i = 0
    for j in hero_number:
        # 创建文件夹
        os.makedirs("C:\\Users\\leipeng\\Desktop\\skin\\" + hero_name[i])#原因是因为os.listdir()只能创建一级目录。而os.makedirs()可以创建多级目录。
        # 进入创建好的文件夹
        os.chdir("C:\\Users\\leipeng\\Desktop\\skin\\" + hero_name[i])
        i += 1
        for k in range(10):
            # 拼接url
            onehero_link = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(j) + '/' + str(
                j) + '-bigskin-' + str(k) + '.jpg'
            im = requests.get(onehero_link)  # 请求url
            if im.status_code == 200:
                open(str(k) + '.jpg', 'wb').write(im.content)  # 写入文件


downloadPic()