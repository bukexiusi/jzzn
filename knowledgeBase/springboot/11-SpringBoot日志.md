# SpringBoot日志

---

## 1、常见的框架和日志框架选择

+ JUL(java.util.logging)
+ JCL(Apache Commons Logging)
+ Log4j
+ Log4j2
+ Logback
+ SLF4j
+ jboss-logging

日志门面（抽象层）|日志实现|
-|:-:|
~~JCL~~、SLF4j、~~jboss-logging~~|Log4j、JUL、Log4j2、Logback|

SLF4、Log4j、Logback出自同一人之手

==日志门面：SLF4j==
==日志实现：Logback==

JCL 太久没更新
jboss-logging 普适性不强
JUL 日志市场被Log4j占有，匆忙推出
Log4j2 apache推出，太新，很多框架还没适配
Log4j 有性能上的问题

## 2、SLF4j使用

### 如何在系统中使用SLF4j

以后开发的时候、日志记录方法的调用，不应该直接调用日志的实现类，而是调用日志抽象层里面的方法

1. 进入[SLF4j官网](https://www.slf4j.org/index.html "SLF4j官网")

2. 点击用户指南
  ![SLF4j使用](/pic/2019-09-01_190203.png "SLF4j使用")

3. 例子

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class HelloWorld {
  public static void main(String[] args) {
    Logger logger = LoggerFactory.getLogger(HelloWorld.class);
    logger.info("Hello World");
  }
}
```

图示

![slf4j](/pic/concrete-bindings.png "slf4j")

每一个日志的实现框架都有各自的配置，使用slf4j之后，==配置文件还是用实现日志框架自身的配置==

## 2、遗留问题

+ a系统(slf4j+lockback)
+ Spring(commons-log)
+ Hibernate(jboss-log)
+ Mybatis

能否统一日志框架？

1. 进入[SLF4j官网](https://www.slf4j.org/index.html "SLF4j官网")

2. 点击老式apis
  ![SLF4j使用](/pic/2019-09-02_083401.png "SLF4j使用")

3. 统一日志方案
  ![SLF4j使用](/pic/legacy.png "SLF4j使用")
  如何让系统中所有的日志都统一到slf4j：
  ==1、将系统中其他日志框架移除==
  ==2、用中间包替换原有的日志框架==
  ==3、导入slf4j其他的实现==

## 3、SpringBoot日志关系

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter</artifactId>
  <version>2.1.7.RELEASE</version>
  <scope>compile</scope>
</dependency>
```

SpringBoot使用它来做日志功能

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-logging</artifactId>
  <version>2.1.7.RELEASE</version>
  <scope>compile</scope>
</dependency>
```

## 4、日志使用

```java
@RunWith(SpringRunner.class)
@SpringBootTest
public class SpringBoot04LogApplicationTests {

    //日志记录器
    Logger logger = LoggerFactory.getLogger(getClass());

    @Test
    public void contextLoads() {
        //日志级别
        //由低到高
        logger.trace("这是trace日志");
        logger.debug("这是debug日志");
        logger.info("这是info日志");
        logger.warn("这是warn日志");
        logger.error("这是error日志");
    }

}
```

重要参数

```properties
logging.level.com.zn=info

# logging.path和logging.file互斥，两者都存在时logging.file起作用，一般选择logging.path
# 生成日志文件目录
#logging.path=
# 生成日志文件
#logging,file=

# 控制台输出格式自定义
logging.pattern.console=%d{yyyy-MM-dd} %n
# 日志文件输出格式自定义
logging.pattern.file=%d{yyyy-MM-dd} [%thread] %-5level %logger %msg %n

```

%d          - 时间
%thread     - 线程名
%-5level    - 日志级别从左显示5个字符宽度
%logger{50} - log名最长五十，否则按照句点分隔
%msg        - 日志消息
%n          - 换行

指定配置
在类路径下(resource)放日志框架的配置文件，则SpringBoot不会使用自身关于日志的属性配置（properties和yml）

Logging System|Customization|
-|-|
Logback|**logback-spring.xml**, logback-spring.groovy, ~~logback.xml~~, or logback.groovy|
Log4j2|log4j2-spring.xml or log4j2.xml|
JDK|logging.properties|

logback.xml        -> 正常的日志配置
logback-spring.xml -> 可以用spring高级特性profile，如下

```xml
<springProfile name="staging">
<!-- configuration to be enabled when the "staging" profile is active -->
</springProfile>

<springProfile name="dev | staging">
<!-- configuration to be enabled when the "dev" or "staging" profiles are active -->
</springProfile>

<springProfile name="!production">
<!-- configuration to be enabled when the "production" profile is not active -->
</springProfile>
```

## 4、切换日志实现类

按照日志适配图进行相关的切换

+ 方法一

排除依赖，引入新依赖

+ 方法二（推荐）

排除starter-logging
引入starter-log4j
