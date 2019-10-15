# @PropertySource、@ImportResource、@Bean

---

## 1、@PropertySource

### 概述

+ @ConfigurationProperties是完成类与配置的映射
+ @PropertySource是增加指定的配置文件（同时也会读取默认的配置文件）
+ ==两者需要配合使用==

### 样例

@PropertySource(value={"classpath:person.properties"})

+ value是一个数组，说明可配置多个properties文件
+ classpath(类路径)，一般放在resource文件夹下
![PropertySource](/pic/2019-08-31_182734.png "PropertySource")

## ~~2、@ImportRource~~

### ~~概述~~

+ ~~导入spring的配置文件，让配置文件生效~~
+ ~~标注在配置类上~~
  + ~~标有@SpringBootApplication注解的类（主配置类）~~
  + ~~标有@Configuration注解的类~~
+ ~~兼容spring配置文件、==不推荐这种方式~~
+ ==推荐@Configuration==

### ~~样例~~

![ImportRource](/pic/2019-08-31_190002.png "ImportRource")

## 3、@Configuration

### 概述

标有该注解的类，等同于配置文件，用类代替配置文件（SpringBoot推荐方式）

### 样例

```java
package com.zn.springboot02config.config;

import com.zn.springboot02config.services.HelloService;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2019/8/31 18:40
 * @description 声明当前类是配置类，等同于原来的spring配置文件
 *
 * 在配置文件中用<bean></bean>标签添加组件
 */

@Configuration
public class MyAppConfig {

    //将方法的返回值添加到容器中，容器中组件默认的id就是方法名
    @Bean
    public HelloService helloService() {
        System.out.println("容器中添加helloService组件");
        return new HelloService();
    }

    /**
     *
     * 以上方法相当于
     * <bean id="helloService" class="com.zn.springboot02config.services.HelloService"></bean>
     * 给容器中添加组件
     *
     * */

}

```
