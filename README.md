## 爬虫阶段遇到的坑及解决方法
### 1.selenium.common.exceptions.WebDriverException: Message: 'chromedriver'解决 
https://www.cnblogs.com/hisweety/p/13324146.html
### 2.图片懒加载情况，图片获取

### 3.文档https://www.cnblogs.com/attila/p/10885750.html

###  4.防火墙 https://blog.csdn.net/weixin_34270865/article/details/91934211
    ufw allow 80
    ufw alow 27017
    ufw alow 22
    sudo ufw deny 65000
    ufw [--dry-run] enable | disable | reload

### 5.pymongo 连接不上远程  mongodb
    mongodb 配置文件开启端口，ip访问
    防火墙开启 27017端口
    云服务器安全组出入规则 开启27017 端口
    pip3 install pymongo===3.6.1  #目标服务器积极拒绝连接,使用稳定版本pymongo

### 6.启动： scrapy crawl itcast --nolog

### 7.mongo启动失败 https://blog.csdn.net/guo_qiangqiang/article/details/88105449

### 8.有时使用这个方法response.content.decode()   解码HTML，会报错。使用response.text替代

### 目前存在的问题：

1.requests 超时连接不上后，没有相应的回调

2.try catch 异常处理



