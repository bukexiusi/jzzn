# bean转换

---

## 问题来源

![bean转换](/pic/2019-09-22_140932.png "bean转换")

## 解决方案

pom.xml中添加如下依赖

```xml
<dependency>
    <groupId>net.sf.dozer</groupId>
    <artifactId>dozer</artifactId>
    <version>5.5.1</version>
</dependency>
```

注入容器

```java
package com.zn.springboot5web.config;

import org.dozer.DozerBeanMapper;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2019/9/22 14:19
 * @description
 */
@Configuration
public class DozerBeanMapperConfig {

    @Bean
    public DozerBeanMapper mapper() {
        return new DozerBeanMapper();
    }


}

```

使用方法

```java
@Autowired
private DozerBeanMapper dozerBeanMapper;
```
