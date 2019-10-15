# 注解

---

+ @**ResponseBody**
  + 对象转json
  + 标注在方法上
  + 标注在类上，相当于给类中所有方法都标注了该注解

+ @**RestController**

  + 相当于@Controller+@ResponseBody

+ @**ConfigurationProperties**
  + 所标注的类中所有的属性和配置文件中的配置一一映射
  + prefix = "person" -> 根元素映射
  + 所标注的注解必须有@**Component**注解，才能被容器识别
  + 支持松散绑定
    + person.firstName  <-> ${person.firstName}
    + person.first-name <-> ${person.firstName}
    + person.first_name <-> ${person.firstName}
    + PERSON_FIRST_NAME <-> ${person.firstName}
  + 不支持表达式（SpEL）
  + 支持校验（JSR303 @Validated）
  + 支持复杂类型（如map）

+ @**Component**
  配置标注类在容器中

+ @**Value**
  + @Value("true")
  + @Value("${name})
  + @Value("#{1+1}")
  + 不支持松散绑定（必须和配置文件中的属性名相同）
    + person.firstName <-> person.firstName
  + 支持表达式（SpEL）
  + 不支持校验
  + 不支持复杂类型（如map）
  + 相当于下列spring配置中的value

    ```xml
    <bean class="Person">
      <property name="lastName" value=""><property/>
    </bean>
    ```

+ @**RequestBody**

  + json转对象(json -> User)

```java
@PostMapping
public String add(@RequestBody User user) {
  ...
}
```

+ @**RequestParam**

  + @RequestParam("username") -> username映射前端标签name属性
  + 若前端标签name属性和后端形参名一致，@RequestParam可省略

```java
public String login(@RequestParam("username") String userName,
                    @RequestParam("password") String passWord) {
    return "";
}
```
