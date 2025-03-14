# 圆周率生日搜索游戏
一个在圆周率中搜索生日的小游戏
# 运行效果
![运行效果](https://github.com/tuyi1203/PiBirthdayFinder/blob/master/screenshoot.gif)
# 安装
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
# 本机运行
1. 双击 index.html
# 局域网中运行
1. 修改 server.py 文件main函数，绑定的 ip 地址为服务器地址
```
 app.run(host='192.168.11.10', port=5000, debug=False)
```
2. 运行 http 服务器
```
python -m http.server 8000
```
3. 打开浏览器输入地址：http://server_ip_address:8000/index.html

# 备注
1. 生日可搜索范围：1950年1月1日-2020年12月31日
2. 在圆周率小数点后250亿位以内进行搜索
3. pi_birthday_index.pkl 是索引二进制文件
