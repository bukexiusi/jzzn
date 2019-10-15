# @Conditional

---

## 概述

@Conditional派生注解
只有满足条件，该类才会被加载

## 样例

```java
@ConditionalOnWebApplication(
    type = Type.SERVLET
)
@ConditionalOnClass({CharacterEncodingFilter.class})
@ConditionalOnProperty(
    prefix = "spring.http.encoding",
    value = {"enabled"},
    matchIfMissing = true
)
```

## ide

vm中加入 -Ddebug=debug
或者application.properties中 debug=true
Positive matches: 加载配置（满足条件）
Negative matches: 未被加载的配置（不满足条件）
