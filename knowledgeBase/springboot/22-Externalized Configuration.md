# Externalized Configuration

---

## 配置值来源

Spring Boot lets you externalize your configuration so that you can work with the same application code in different environments. You can use

+ ==properties files==,
  + application.properties文件
+ ==YAML files==,
  + application.yml文件
+ ==environment variables==,
+ and ==command-line arguments== to externalize configuration.
  + ~~cmd运行jar，java -jar xxx.jar param1 param2~~
  + cmd运行jar，java -jar xxx.jar --key=value

<font color=lightgreen>以上配置值的四种来源</font>(2019-9-18补充)

## 配置值注入bean方式

Property values can be injected directly into your beans by using

+ the @**Value** annotation,
+ accessed through Spring’s ==Environment abstraction==, or
+ be bound to structured objects through @**ConfigurationProperties**.

<font color=lightgreen>以上四项是配置值注入bean的三种方式</font>(2019-9-18补充)

## 配置值作用顺序

Spring Boot uses a very particular PropertySource order that is designed to allow sensible overriding of values. Properties are considered in ==the following order==:

1.Devtools global settings properties on your home directory (~/.spring-boot-devtools.properties when devtools is active).
2.@TestPropertySource annotations on your tests.
3.properties attribute on your tests. Available on @SpringBootTest and the test annotations for testing a particular slice of your application.
4.==Command line arguments==.

+ java -jar xxx.jar --zn.jz.jj=2
+ java -jar xxx.jar --spring.application.json='{"name": "test"}'

5.Properties from SPRING_APPLICATION_JSON (inline JSON embedded in an environment variable or system property).
6.ServletConfig init parameters.
7.ServletContext init parameters.
8.JNDI attributes from java:comp/env.
9.Java System properties (System.getProperties()).
10.OS environment variables.
11.A RandomValuePropertySource that has properties only in random.*.
12.==Profile-specific application properties outside of your packaged jar (application-{profile}.properties and YAML variants)==.
  
+ yml文件和properties文件拥有相同配置时，properties文件的配置值起作用

13.==Profile-specific application properties packaged inside your jar (application-{profile}.properties and YAML variants)==.
14.==Application properties outside of your packaged jar (application.properties and YAML variants)==.
15.==Application properties packaged inside your jar (application.properties and YAML variants)==.
16.@PropertySource annotations on your 17.@Configuration classes.
Default properties (specified by setting SpringApplication.setDefaultProperties).

<font color=lightgreen>以上是配置值作用的先后顺序</font>(2019-9-18补充)

17.例子如下

classpath路径下application.properties文件

```properties
zn.jz.jj=1
```

命令行 ==java -jar xxx.jar --zn.jz.jj=2==

+ 最终zn.jz.jj值为1
+ 可在启动行赋值更改配置文件值

## 禁用命令行参数

If you do not want command line properties to be added to the Environment, you can disable them by using **SpringApplication.setAddCommandLineProperties(false)**.

## profile补充

SpringBoot默认从下面四个位置寻找==名为application==的文件(此时**spring.config.name**=application,**spring.config.location**=classpath:/,classpath:/config/,file:./,file:./config/)

+ file:      ./config/
+ file:      ./
+ classpath: /config/
+ classpath: /

1）若设置**spring.config.name**=zn
则SpringBoot会在以上四个路径寻找==名为zn==的文件

2）若设置**spring.config.location**=classpath:/zn/,classpath:/config/zn/
则SpringBoot会在以下路径寻找文件

+ classpath:/zn/
+ classpath:/config/zn/

3）若设置**spring.config.additional-location**=classpath:/zn/,classpath:/config/zn/
则SpringBoot会在以下路径寻找文件

+ classpath:/zn/
+ classpath:/config/zn/
+ file:      ./config/
+ file:      ./
+ classpath: /config/
+ classpath: /

---

spring.config.additional-location和spring.config.location必须以"/"结尾

## 配置值加密

Spring Boot does not provide any built in support for encrypting property values, however, it does provide the hook points necessary to modify values contained in the Spring Environment. The **EnvironmentPostProcessor** interface allows you to manipulate the Environment before the application starts.

+ SpringBoot不支持配置值加密
+ 可以通过实现EnvironmentPostProcessor接口实现配置值加密

## EnvironmentPostProcessor

在任意目录下建立一个名为springboot.properties文件，

```properties
xj=lixiaoyao
```

定义MyEnvironmentPostProcessor实现EnvironmentPostProcessor接口

```java
package com.zn.springboot5web.component.environment;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.env.EnvironmentPostProcessor;
import org.springframework.core.env.ConfigurableEnvironment;
import org.springframework.core.env.PropertiesPropertySource;
import org.springframework.stereotype.Component;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2019/9/18 17:07
 * @description
 */

@Component
public class MyEnvironmentPostProcessor implements EnvironmentPostProcessor {
    @Override
    public void postProcessEnvironment(ConfigurableEnvironment environment, SpringApplication application) {
        try (InputStream inputStream = new FileInputStream("F:/_java/test/outside-application.properties")){

            Properties properties = new Properties();
            properties.load(inputStream);
            PropertiesPropertySource propertiesPropertySource = new PropertiesPropertySource("zn", properties);
            environment.getPropertySources().addLast(propertiesPropertySource);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

```

在classpath定义一个META-INF文件夹然后在其下面先建spring.factories文件，在其中指定：

```factories
org.springframework.boot.env.EnvironmentPostProcessor=com.zn.springboot5web.component.environment.MyEnvironmentPostProcessor
```

启动类

```java
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        ConfigurableApplicationContext context = SpringApplication.run(Application.class,args);
        String username = context.getEnvironment().getProperty("jdbc.root.user");
        String password = context.getEnvironment().getProperty("jdbc.root.password");
        System.out.println("username==="+username);
        System.out.println("password==="+password);
        context.close();
    }
}
```
