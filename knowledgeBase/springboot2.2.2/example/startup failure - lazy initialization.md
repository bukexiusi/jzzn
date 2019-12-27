# <center>Lazy Initialization</center>

==lazy initialization is not enabled by default== and it is recommended that fine-tuning of the JVM’s heap size is done before enabling lazy initialization.

## 方法一：全局加载

+ Lazy initialization can be enabled programatically using the **lazyInitialization** method on **SpringApplicationBuilder** or the **setLazyInitialization** method on **SpringApplication**. 
+ Alternatively, it can be enabled using the spring.main.lazy-initialization property as shown in the following example:
    ```properties
    spring.main.lazy-initialization=true
    ```

## 方法二：@Configuration+@Bean+@Lazy形式

```java
@Configuration
public class BeanConfig {

    @Bean
    @Lazy(value = true)
    public People people() {
        return new People();
    }
}
```

1、@Lazy(value = true)：默认为true，不执行构造方法
2、@Lazy(value = false)：执行构造方法
3、@Lazy()：默认为true，不执行构造方法
4、无@Lazy：不执行构造方法

## 方法三：@Component+@Lazy形式

```java
@Component
@Lazy(value = true)
public class Animal {

    public Animal() {
        System.out.println("************你************");
    }

}
```

1、@Lazy(value = true)：默认为true，不执行构造方法
2、@Lazy(value = false)：执行构造方法
3、@Lazy()：默认为true，不执行构造方法
4、无@Lazy：不执行构造方法

## 方法四：@Import+@Lazy形式

```java
@Import(value = {God.class})

@Lazy(value=false)
public class God {
    public God() {
        System.out.println("****************他**************");
    }
}
```

1、@Lazy(value = true)：默认为true，不执行构造方法
2、@Lazy(value = false)：执行构造方法
3、@Lazy()：默认为true，不执行构造方法
4、无@Lazy：不执行构造方法

## 方法五：classpath下的META-INF/spring.factories

```factories
org.springframework.boot.autoconfigure.EnableAutoConfiguration=\
config.DogConfig,\
entity.Sheep
```

1、@Lazy(value = true)：默认为true，不执行构造方法
2、@Lazy(value = false)：执行构造方法
3、@Lazy()：默认为true，不执行构造方法
4、无@Lazy：执行构造方法


## 方法六：后处理Bean

1. 可以加一个后处理Bean
    ```java
    @Component
    public class MyBeanPostProcessor implements BeanPostProcessor {

            前方法（）；

            后方法（）；

    }
    ```
2. 后处理Bean的前方法、后方法伴随着构造方法执行。要执行都执行，要不执行都不执行

3. 执行顺序：构造方法--->前方法--->后方法

4. 执行的位置：SpringApplication.class  run()--->refreshContext()--->refresh()--->AbstractApplicationContext.class  refresh()--->finishBeanFactoryInitialization()  执行非懒加载的bean--->ConfigurableListableBeanFactory.class  preInstantiateSingletons()