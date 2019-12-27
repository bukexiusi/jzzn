# <center>Add Your Own FailureAnalyzer</center>

## 继承AbstractFailureAnalyzer，重写analyze方法，返回FailureAnalysis。泛型的类型是Throwable的子类。

```java

package com.example.demo.failureAnalyzer;
 
import org.springframework.boot.diagnostics.AbstractFailureAnalyzer;
import org.springframework.boot.diagnostics.FailureAnalysis;
 
public class NullPointFailureAnalyzer extends AbstractFailureAnalyzer<NullPointerException> {
    @Override
    protected FailureAnalysis analyze(Throwable rootFailure, NullPointerException cause) {
        return new FailureAnalysis(cause.getMessage(), "请检查空指针", cause);
    }
}
```

## src/main/resources/META-INF中添加spring.factories，并注册自定义的FailureAnalyzer。

```factories
org.springframework.boot.diagnostics.FailureAnalyzer=\
com.momo.springbootfailureanalyzer.ArithmeticFailureAnalyzer
```

## 测试

```java
@Service
public class ValidateNullPointExceptionService {
    public ValidateNullPointExceptionService() {
        Integer a = null;
        System.out.println(a.equals("88"));
    }
}
```

@Service注解的类会在启动时加载执行