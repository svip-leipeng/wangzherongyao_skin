# CSDN_text1_skin
![屏幕截图 2023-04-19 092548](https://user-images.githubusercontent.com/128241333/232942735-db3947c6-4756-482a-9f14-95db01fda3fb.png)
-效果图
-使用愉快
--鸣谢：
---1.导入os和requests库，os用于处理文件和目录，requests用于发送HTTP请求。
---2.定义一个url变量，指向英雄列表的json文件。
---3.使用requests.get()方法获取该url的内容，返回一个Response对象。
---4.使用Response对象的.json()方法将返回的内容转换为json格式。
---5.使用map()函数和lambda表达式提取出英雄的名字和编号。
---6.定义一个downloadPic()函数，用于下载英雄的皮肤图片。
---7.在downloadPic()函数中，首先创建一个文件夹，然后进入该文件夹。
---8.对于每个英雄，遍历其皮肤编号，拼接出皮肤图片的url，然后发送请求获取图片内容。
---9.如果请求成功（状态码为200），则将图片内容写入文件。
---10.在每一步操作后，使用time.sleep()函数暂停一段时间，随机休眠10-20秒。
