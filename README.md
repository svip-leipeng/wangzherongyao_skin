# CSDN_text1_skin
![屏幕截图 2023-04-19 092548](https://user-images.githubusercontent.com/128241333/232942735-db3947c6-4756-482a-9f14-95db01fda3fb.png)
-效果图
-使用愉快
--鸣谢：https://blog.csdn.net/qq_42453117/article/details/103190981?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522168187029716800211520403%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=168187029716800211520403&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-1-103190981-null-null.142^v84^control,239^v2^insert_chatgpt&utm_term=%E5%86%99%E4%B8%80%E4%B8%AA%E7%88%AC%E8%99%AB%2C%E7%88%AC%E5%8F%96%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80%E7%9A%AE%E8%82%A4&spm=1018.2226.3001.4187
1.导入os和requests库，os用于处理文件和目录，requests用于发送HTTP请求。
2.定义一个url变量，指向英雄列表的json文件。
3.使用requests.get()方法获取该url的内容，返回一个Response对象。
4.使用Response对象的.json()方法将返回的内容转换为json格式。
5.使用map()函数和lambda表达式提取出英雄的名字和编号。
6.定义一个downloadPic()函数，用于下载英雄的皮肤图片。
7.在downloadPic()函数中，首先创建一个文件夹，然后进入该文件夹。
8.对于每个英雄，遍历其皮肤编号，拼接出皮肤图片的url，然后发送请求获取图片内容。
9.如果请求成功（状态码为200），则将图片内容写入文件。
10.在每一步操作后，使用time.sleep()函数暂停一段时间，随机休眠10-20秒。
