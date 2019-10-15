# helloWorld解析

---

## 1、POM的父项目

pom.xml的父项目如下

```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>1.5.9.RELEASE</version>
    <relativePath/> <!-- lookup parent from repository -->
</parent>
```

pom.xml的父项目的父项目如下

```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-dependencies</artifactId>
    <version>1.5.9.RELEASE</version>
    <relativePath>../../spring-boot-dependencies</relativePath>
</parent>
```

spring-boot-dependencies管理了其**声明的jar包**的版本管理
即声明的jar包不需要声明版本
未声明的jar需要声明版本
故spring-boot-dependencies是版本仲裁中心

## 2、启动器（jar包由谁导入）

```xml
<dependencies>
    <!--org.springframework.web包-->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
</dependencies>
```

spring-boot-starter-web: spring-boot web场景启动器
帮我们导入了web正常运行所需的组件，构建环境

spring-boot有很多种场景的starter(启动器)，spring-boot-starter-web只是其中一种

## 3、查看启动器(starter)的方法

+ [spring官网](https://spring.io/projects "spring官网")

+ 如下图
![查看启动器](/pic/2019-08-28_005407.png "查看启动器")

+ 如下图
![查看启动器](/pic/2019-08-28_005718.png "查看启动器")

+ 搜索starter

## 4、主程序类，主入口类

+ **@SpringBootApplication**
  + **@SpringBootConfiguration**
    + **@Configuration**
  + **@EnableAutoConfiguration**
    + **@AutoConfigurationPackage**
      + **@Import({Registrar.class})**
        + **registerBeanDefinitions方法**
          + **(new AutoConfigurationPackages.PackageImport(metadata)).getPackageName()**
    + **@Import({EnableAutoConfigurationImportSelector.class})**
      + **AutoConfigurationImportSelector.class**
        + **getCandidateConfigurations方法**
          + **loadFactoryNames方法**
            + **META-INF/spring.factories**(spring-boot-autoconfigure:1.5.9.RELEASE.jar下)

1. @**SpringBootApplication**

    + 标注主程序类，通过主程序类的main方法来启动应用

2. @**SpringBootConfiguration**

    + SpringBoot配置类，==等同于xml配置==，容器中的组件

3. @**Configuration**

    + 配置类

4. @**EnableAutoConfiguration**

    + 开启自动配置类（springmvc配置，包扫描配置），以前需要配置的东西都不再需要配置了，就是由该类完成自动配置功能

5. @**AutoConfigurationPackage**

    + 自动配置包

6. @**Import({Registrar.class})**

    + @Import是SpringBoot底层注解

    + Registrar.class注册器类，其中registerBeanDefinitions方法将@SpringBootApplication所标注的类所在的包下所有类扫描到spring容器中

    + registerBeanDefinitions方法中的(new AutoConfigurationPackages.PackageImport(metadata)返回@SpringBootApplication所标注的类所在的包名

7. **@Import({EnableAutoConfigurationImportSelector.class})**

    + 导入某些组件的选择器

    + EnableAutoConfigurationImportSelector.class开启自动配置导入选择器

    + selectImports方法将导入的组件以全类名的方式返回，这些组件就会被添加到容器中

    + selectImports给容器导入的大量的自动配置类
