# SpringBoot配置

---

## 1、配置文件

SpringBoot使用一个全局的配置文件，配置文件名是固定的

+ application.properties

+ application.yml

配置文件的作用：修改SpringBoot自动配置的默认值

YAML(YAML Ain't Markup Language)

+ YAML A Markup Language：是一个标记语言

+ YAML isn't Markup Language：不是一个标记语言

标记语言

+ 以数据为中心

+ 比xml、json更适合做配置文件

YML样例

```yml
server:
    port: 8081
```

XML样例

```xml
<server>
    <port>8081</port>
</server>
```

结论：**YML比XML更加简洁**

## 2、YAML语法

### 1、基本语法

k:(空格)v
以空格的缩进来控制层级关系

### 2、值的写法

==字面值:普通值（数字，字符串，布尔）==

+ 字符串默认不用加上单引号或者双引号
  + 双引号：会转义特殊字符
    + name: "zhangsan \n lisi" -> zhangsan 换行 lisi
  + 单引号：不会转义特殊字符
    + name: 'zhangsan \n lisi' -> zhangsan \n lisi

==对象、Map（属性和值）（键值对）==

+ 写法

```yml
friends:
    lastName: zhangsan
    age: 20
    weight: 60
```

+ 行内写法

```yml
friends: {lastName: zhangsan, age: 18, weight: 60}
```

==数组（List、Set）==

+ 写法

用-标识数组中的一个元素

```yml
animals:
 - cat
 - dog
 - pig
```

+ 行内写法

```yml
animals: [cat, dog, pig]
```

@**ConfigurationProperties(prefix = "person")**

+ 所标注的类中所有的属性和配置文件中的配置一一映射
+ prefix = "person" -> 根元素映射

### 3、properties配置

==字面值:普通值（数字，字符串，布尔）==

+ person.last-name=张三
+ person.age=13
+ person.boss=false

==map配置==

+ person.maps.k1=v1
+ person.maps.k2=v2

==list配置==

+ person.lists=1,2,3

properties中文乱码解决方法

![properties配置](/pic/2019-08-31_121000.png "properties配置")

### 4、比较

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

+ @**Value**
  + @Value("true")
  + @Value("${name})
  + @Value("#{1+1}")
  + 不支持松散绑定（必须和配置文件中的属性名相同）
    + person.firstName <-> person.firstName
  + 支持表达式（SpEL）
  + 不支持校验
  + 不支持复杂类型（如map）

### 4、配置文件占位符

#### 随机数

${random.value}、${random.int}、${random.long}
${random.int(10)}、${random.int[1,10]}、${random.uuid}

#### 样例

```xml
person.last-name=李逍遥${random.uuid}
person.age=${random.int}
# person.dogs.name=${person.last-name}_dog
# 若last-name没有值则默认为dog
person.dogs.name=${last-name:dog}
```
