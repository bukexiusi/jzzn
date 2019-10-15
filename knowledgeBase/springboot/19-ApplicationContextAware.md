# ApplicationContextAware

---

## 问题背景

在我们的web程序中，用spring来管理各个实例(bean), 有时在程序中为了**使用已被实例化的bean**, 通常会用到这样的代码：

```java
ApplicationContext appContext = new ClassPathXmlApplicationContext("applicationContext-common.xml");  
AbcService abcService = (AbcService)appContext.getBean("abcService");
```

但是这样就会**存在一个问题**：因为它会重新装载applicationContext-common.xml并实例化上下文bean，如果有些线程配置类也是在这个配置文件中，那么会造成做相同工作的的线程会被启动两次。一次是web容器初始化时启动，另一次是上述代码显示的实例化了一次。当于重新初始化一遍！！！！这样就产生了冗余。

## 解决方法

实现ApplicationContextAware接口

```java
@Component
public class AppUtil implements ApplicationContextAware {

    private static ApplicationContext applicationContext;

    @Override
    public void setApplicationContext(ApplicationContext arg0) throws BeansException {
        applicationContext = arg0;
    }

    public static Object getObject(String id) {
        Object object = null;
        object = applicationContext.getBean(id);
        return object;
    }
}
```
