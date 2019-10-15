# Application Event

---

## 概述

1. Some events are actually triggered before the ApplicationContext is created, so you cannot register a listener on those as a @Bean.

    + 有些事件需要在==应用启动前==触发
    + @Bean注解的类需要在==应用启动后==才能触发

2. You can register them with the SpringApplication.addListeners(…​) method or the SpringApplicationBuilder.listeners(…​) method.

3. You often need not use application events, but it can be handy to know that they exist. Internally, Spring Boot uses ==events== to handle a variety of tasks.

4. To allow your listener to distinguish between ==an event for its context== and ==an event for a descendant context==, it should request that its application context is injected and then compare the injected context with the context of the event.
   + The context can be injected by implementing ApplicationContextAware or,
     + ApplicationContextAware在19-ApplicationContextAware中理解
   + if the listener is a bean, by using @Autowired.
   + ==**event和context，在SpringBoot中具体定位以及关系**==

5. Application events are sent in the following order, as your application runs:

    + An **ApplicationStartingEvent** is sent at the start of a run but before any processing, except for the registration of listeners and initializers.
    + An **ApplicationEnvironmentPreparedEvent** is sent when the Environment to be used in the context is known but before the context is created.
    + An **ApplicationPreparedEvent** is sent just before the refresh is started but after bean definitions have been loaded.
    + An **ApplicationStartedEvent** is sent after the context has been refreshed but before any application and command-line runners have been called.
    + An **ApplicationReadyEvent** is sent after any application and command-line runners have been called. It indicates that the application is ready to service requests.
    + An **ApplicationFailedEvent** is sent if there is an exception on startup.

## ApplicationStartingEvent

1、事件类编写

```java
package com.zn.springboot5web.events;

import com.zn.springboot5web.customize.BannerCustomize;
import org.springframework.boot.Banner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.context.event.ApplicationStartingEvent;
import org.springframework.context.ApplicationListener;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2019/9/16 16:22
 * @description
 */
public class MyAppStartingEvent implements ApplicationListener<ApplicationStartingEvent> {
    @Override
    public void onApplicationEvent(ApplicationStartingEvent applicationStartingEvent) {
        // 获取源？
        Object source = applicationStartingEvent.getSource();
        // 获取时间戳
        long timestamp = applicationStartingEvent.getTimestamp();
        // 获取参数 public static void main(String[] args) {...}
        String[] args = applicationStartingEvent.getArgs();
        // 获取SpringApplication并设置横幅 - ApplicationStartingEvent的主要作用
        SpringApplication application = applicationStartingEvent.getSpringApplication();
        Banner banner = new BannerCustomize();
        application.setBanner(banner);                // 注入自定义Banner
//        application.setBannerMode(Banner.Mode.OFF);   // 禁用Banner
        System.out.println("ApplicationStartingEvent 执行完毕");
    }
}

```

+ ApplicationStartingEvent有四个getXXX方法，其中getSpringApplication()能得到SpringApplication对象
+ ApplicationStartingEvent主要运用于SpringApplication的参数设置，如自定义Banner。

2、加入容器

```java
@SpringBootApplication
public class SpringBoot5WebApplication {

    public static void main(String[] args) {
        SpringApplication app = new SpringApplication(SpringBoot5WebApplication.class);
        // 将该监听加入容器
        app.addListeners(new MyAppStartingEvent());
        app.run(args);
    }

}
```

## ApplicationEnvironmentPreparedEvent

1、事件类编写

```java
package com.zn.springboot5web.events;

import org.springframework.boot.context.event.ApplicationEnvironmentPreparedEvent;
import org.springframework.context.ApplicationListener;
import org.springframework.core.env.ConfigurableEnvironment;
import org.springframework.core.env.MutablePropertySources;
import org.springframework.core.env.PropertySource;

import java.util.Iterator;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2019/9/16 17:28
 * @description
 */
public class MyAppEnvPreparedEvent implements ApplicationListener<ApplicationEnvironmentPreparedEvent> {
    @Override
    public void onApplicationEvent(ApplicationEnvironmentPreparedEvent applicationEnvironmentPreparedEvent) {
        ConfigurableEnvironment environment = applicationEnvironmentPreparedEvent.getEnvironment();
        MutablePropertySources maps = environment.getPropertySources();
        // ...
        System.out.println("ApplicationEnvironmentPreparedEvent 执行完毕");
    }
}
```

+ ApplicationEnvironmentPreparedEvent也拥有ApplicationStartingEvent的四个getXXX方法，即也能得到SpringApplication对象，==也能完成ApplicationStartingEvent所涉及的功能==
+ getEnvironment方法能得到ConfigurableEnvironment对象，ConfigurableEnvironment中能获取应用系统参数(getSystemProperties)、环境变量(getSystemEnvironment)等
+ 综上所述ApplicationEnvironmentPreparedEvent比ApplicationStartingEvent多一个getEnvironment方法
+ 官方文档例子

  + adding a new property source with highest search priority

    ```java
    ConfigurableEnvironment environment = new StandardEnvironment();
    MutablePropertySources propertySources = environment.getPropertySources();
    Map<String, String> myMap = new HashMap<>();
    myMap.put("xyz", "myValue");
    propertySources.addFirst(new MapPropertySource("MY_MAP", myMap));
    ```

  + removing the default system properties property source

    ```java
    MutablePropertySources propertySources = environment.getPropertySources();
    propertySources.remove(StandardEnvironment.SYSTEM_PROPERTIES_PROPERTY_SOURCE_NAME);
    ```

  + mocking the system environment for testing purposes

    ```java
    MutablePropertySources propertySources = environment.getPropertySources();
    MockPropertySource mockEnvVars = new MockPropertySource().withProperty("xyz", "myValue");
    propertySources.replace(StandardEnvironment.SYSTEM_ENVIRONMENT_PROPERTY_SOURCE_NAME, mockEnvVars);
    ```

2、加入容器

同ApplicationStartingEvent

## ApplicationPreparedEvent

1、事件类编写

```java
package com.zn.springboot5web.events;

import org.springframework.boot.context.event.ApplicationPreparedEvent;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationListener;
import org.springframework.context.ConfigurableApplicationContext;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2019/9/16 19:51
 * @description
 */
public class MyAppPreparedEvent implements ApplicationListener<ApplicationPreparedEvent> {
    @Override
    public void onApplicationEvent(ApplicationPreparedEvent applicationPreparedEvent) {
        ConfigurableApplicationContext context = applicationPreparedEvent.getApplicationContext();
        passContextInfo(context);
        System.out.println("ApplicationPreparedEvent 执行完毕");
    }

    /**
     * 传递上下文
     * @param cac
     */
    private void passContextInfo(ApplicationContext cac) {
        // dosomething()
    }
}
```

+ ApplicationPreparedEvent也拥有ApplicationStartingEvent的四个getXXX方法，即也能得到SpringApplication对象，但该事件类型是在banner打印完后触发，故不再能操作banner。
+ getApplicationContext方法得到ConfigurableApplicationContext对象

2、加入容器

同ApplicationStartingEvent

## ApplicationStartedEvent

1、事件类编写

```java
package com.zn.springboot5web.events;

import org.springframework.boot.context.event.ApplicationStartedEvent;
import org.springframework.context.ApplicationListener;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2019/9/16 20:52
 * @description
 */
public class MyAppStartedEvent implements ApplicationListener<ApplicationStartedEvent> {
    @Override
    public void onApplicationEvent(ApplicationStartedEvent applicationStartedEvent) {
        System.out.println("ApplicationStartedEvent 执行完毕");
    }
}

```

2、加入容器

同ApplicationStartingEvent

## ApplicationReadyEvent

1、事件类编写

```java
package com.zn.springboot5web.events;

import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.context.ApplicationListener;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2019/9/16 20:32
 * @description
 */
public class MyAppRdyEvent implements ApplicationListener<ApplicationReadyEvent> {
    @Override
    public void onApplicationEvent(ApplicationReadyEvent applicationReadyEvent) {
        // UserService userService = applicationContext.getBean(UserService.class); 
        System.out.println("ApplicationReadyEvent 执行完毕");
    }
}

```

+ ApplicationReadyEvent也拥有ApplicationStartingEvent的四个getXXX方法，即也能得到SpringApplication对象，但该事件类型是在banner打印完后触发，故不再能操作banner。
+ getApplicationContext方法得到ConfigurableApplicationContext对象
+ ==这个监听器中已经可以开始获取bean==

2、加入容器

同ApplicationStartingEvent

## ApplicationFailedEvent

1、事件类编写

```java
package com.zn.springboot5web.events;

import org.springframework.boot.context.event.ApplicationFailedEvent;
import org.springframework.context.ApplicationListener;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2019/9/16 20:48
 * @description
 */
public class MyAppFailedEvent implements ApplicationListener<ApplicationFailedEvent> {
    @Override
    public void onApplicationEvent(ApplicationFailedEvent applicationFailedEvent) {
        System.out.println("ApplicationFailedEvent 执行完毕");
        Throwable exception = applicationFailedEvent.getException();
        System.out.println(exception);
    }
}

```

2、加入容器

同ApplicationStartingEvent

## 加载顺序

+ ApplicationStartingEvent(**可自定义banner**)
+ ApplicationEnvironmentPreparedEvent(**可自定义banner**)
+ (banner)
+ ApplicationPreparedEvent
+ ApplicationStartedEvent
+ ApplicationReadyEvent(**可加载或获取bean**)

