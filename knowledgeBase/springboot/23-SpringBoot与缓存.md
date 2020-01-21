# SpringBoot与缓存

+ JSR107
+ Spring缓存抽象
  + 因简化JSR107而诞生
+ 整合redis

**Cache**

+ 缓存接口，定义缓存操作。
+ 实现类有**RedisCache**、**EhCacheCache**、**ConcurrentMapCache**等

**CacheManager**

+ 管理缓存的组件

@**Cacheable**

==先判断是否有缓存，若无则执行方法==

+ value/cacheNames
  + 缓存组件名字，代表一个缓存组件（类比变量名和变量的关系）
  + 缓存组件由**CacheManager**管理
+ key(缓存键值)
  + key与keyGenerator二选一
  + key实例 
    + key="#root.getMethod+'['+#id+']'"
    + key="#root.getMethod+'['+#p0+']'"或key="#root.getMethod+'['+#a0+']'"
+ keyGenerator
  + key与keyGenerator二选一
+ cacheManager
  + cacheManager与cacheResolver二选一
  + 得到Cache
+ cacheResolver
  + cacheManager与cacheResolver二选一
  + 得到Cache的集合（RedisCache、EhCacheCache）
+ condition
  + 指定缓存条件，满足条件缓存
  + condition实例
    + condition="#id>1"
    + condition="#id eq 'zn'"
+ unless
  + 指定缓存条件，满足条件不缓存
  + 可以获取结果判断(#result)
  + 若同时存在condition和unless, 两者之间是并的关系，必须都为真才会满足
+ sync(异步模式)

@**CacheEvict**

==@CacheEvict通常配置在删除方法上==

+ allEntries
  + allEntries默认为false，当为true删除所有缓存
+ beforeInvocation
  + beforeInvocation默认为false，缓存清除在方法运行之后执行（若方法执行异常，也不会执行清除缓存操作）
  + beforeInvocation设置为true，缓存清除在方法运行之前执行

@**CachePut**

==无条件先执行方法，再更新缓存==

+ key
  + #result只能在**CachePut**中使用，不能在**Cacheable**中使用
  + 实例
    + key="#result.id"

@**EnableCaching**

**keyGenerator**

**serialize**

## SpringBoot嵌入缓存框架

1）启动类上添加开启缓存的注解@**EnableCaching**

```java
@EnableCaching
@SpringBootApplication
public class SpringBoot04LogApplication {

    public static void main(String[] args) {
        SpringApplication.run(SpringBoot04LogApplication.class, args);
    }

}
```

2）@**Cacheable**等注解添加在服务实现类上
