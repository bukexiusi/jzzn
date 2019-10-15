# ApplicationRunner和CommandLineRunner

---

## 业务场景

应用服务启动时，加载一些数据和执行一些应用的==初始化动作==。如：删除临时文件，清除缓存信息，读取配置文件信息，数据库连接等。

## 解决方法

1、SpringBoot提供了**CommandLineRunner**和**ApplicationRunner**接口。当接口有多个实现类时，提供了@**Order**注解实现自定义执行顺序，也可以实现Ordered接口来自定义顺序。

+ If ==several== CommandLineRunner or ApplicationRunner beans are defined that ==must be== called in a specific ==order==, you can additionally implement the **org.springframework.core.Ordered** interface or use the **org.springframework.core.annotation.Order** annotation.

注意：数字越小，优先级越高，也就是@Order(1)注解的类会在@Order(2)注解的类之前执行。
2、==两者的区别在于==：
ApplicationRunner中run方法的参数为ApplicationArguments，而CommandLineRunner接口中run方法的参数为String数组。想要更详细地获取命令行参数，那就使用ApplicationRunner接口

```java
@Component
@Order(value = 10)
public class AgentApplicationRun2 implements ApplicationRunner {
    @Override
    public void run(ApplicationArguments applicationArguments) throws Exception {
    }
}
```

```java
@Component
@Order(value = 11)
public class AgentApplicationRun implements CommandLineRunner {
    @Override
    public void run(String... strings) throws Exception {
    }
}
```
