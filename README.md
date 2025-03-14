﻿# 圆周率生日搜索游戏
一个在圆周率中搜索生日的小游戏
# 运行效果
![运行效果](https://github.com/tuyi1203/PiBirthdayFinder/blob/master/screenshoot.gif)
## 安装
1. 复制仓库
```
git clone https://github.com/tuyi1203/PiBirthdayFinder.git 
```
2. 安装依赖
```
pip install -r requirements.txt
```
3. 运行服务端:
```
waitress-serve --host=0.0.0.0 --port=5000 server:app
```
## 本机运行
1. 双击 index.html
## 局域网中运行
1. 修改 server.py 文件main函数中，绑定的 ip 地址为服务器地址
2. 运行 http 服务器：python -m http.server 8000
3. 打开浏览器输入地址：http://server_ip_address:8000/index.html
