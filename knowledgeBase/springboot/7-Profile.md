# Profile

---

==properties类型的文件优先级大于yml文件==

## 1、多Profile文件

文件名

+ application-{profile}.properties
+ application-{profile}.yml
+ 默认使用application.properties

![多Profile文件](/pic/2019-08-31_210926.png "多Profile文件")

## 2、yml

以下配置运行，访问8082端口

```yml
server:
  port: 8081
spring:
  profiles:
    active: dev2
---
server:
  port: 8081
spring:
  profiles: dev1
---
server:
  port: 8082
spring:
  profiles: dev2
```

## 3、激活指定文件

+ 在配置文件中指定
+ 命令行
  + java -jar xxx.jar -spring.profiles.active=dev
  + 在ide环境中配置，如下

  ![激活指定文件](/pic/2019-08-31_212558.png "激活指定文件")
+ 虚拟机
  ![激活指定文件](/pic/2019-08-31_212924.png "激活指定文件")
