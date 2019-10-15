# ApplicationArguments

---

在Controller中想获取启动参数

```java
@RestController
public class HelloWorldController {

    @Autowired
    private ApplicationArguments applicationArguments;

    ...

}
```

启动参数指的是 args

```java
@SpringBootApplication
public class SpringBoot5WebApplication {

    public static void main(String[] args) {}

}
```
