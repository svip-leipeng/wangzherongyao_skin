import os
import requests
import time
import random
from tkinter import *
from tkinter import filedialog

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
            im = requests.get(onehero_link)
            if im.status_code == 200:
                open(str(k) + '.jpg', 'wb').write(im.content)
            time.sleep(random.randint(10, 20))

def select_folder():
    folder_path = filedialog.askdirectory()
    return folder_path

root = Tk()
root.title("英雄皮肤下载器")

label = Label(root, text="请选择要下载的英雄：")
label.pack()

for i, name in enumerate(hero_name):
    button = Radiobutton(root, text=name, variable=StringVar(), value=i)
    button.pack()

folder_button = Button(root, text="选择保存文件夹", command=select_folder)
folder_button.pack()

start_button = Button(root, text="开始下载", command=downloadPic)
start_button.pack()

root.mainloop()
