# spiderT

## 简介

>       可配置静态爬虫
>       此爬虫项目目前,仅支持静态翻页html的爬取和解析
>       动态ajax的post请求正在开发中，欢迎喜欢设计开发的朋友共同参与
    
## 技术需求

>       此项目只需要增加自己的配置文件或者修改已有配置，就可实现自己的爬虫
>       如果你仅仅是拿本项目使用已有爬虫来获取数据，那么你仅仅需要了解Python的环境配置和命令行的使用
>       如果你是想要根据需求开发自己的爬虫那么你需要掌握以下几点：
>   [XPath](https://www.w3school.com.cn/xpath/index.asp)  
>   [HTML](https://www.w3school.com.cn/html/index.asp)
>
        
    
    
    
    
## 配置说明
>       此项目的配置文件都在spiderT/config/下以**_yaml.yaml命名规则
>       配置内容请参考yaml文件中的注释
    
    
## 程序调用
>       跟目录下的main.py为程序的主入口，
>       调用对应配置文件只需传递前缀，目前有两个配置lj(链家)、yc(易车网)
>       如：你自定义的yaml文件名叫aa_yaml.yaml，那么调用时代码如下
```
    run(conf("aa"))
```

## 重构计划
##### 目前项目结构比较草率，下一步准备重构代码，思维导图如下：
![初步重构计划思维导图](https://github.com/ThirteenR/spiderT/blob/master/RefactorMind.pdf)