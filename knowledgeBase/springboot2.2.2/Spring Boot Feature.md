# <center>Spring Boot Feature</center>

In many situations, you can delegate to the static *SpringApplication.run* method, as shown in the following example
```java
public static void main(String[] args) {
    SpringApplication.run(MySpringConfiguration.class, args);
}
```

## 壹、startup log

+ what
+ why
+ how(can we do)
    + setting log levels
    + turn off logging
    + To add additional logging during startup, you can override logStartupInfo(boolean) in a subclass of SpringApplication.

## 贰、startup failure

+ what
    + If your application fails to start, registered FailureAnalyzers get a chance to provide a dedicated error message and a concrete action to fix the problem
+ why
+ how
    + Spring Boot provides numerous FailureAnalyzer implementations, and you can add your own.
    + as follow
        ```git
        $ java -jar myproject-0.0.1-SNAPSHOT.jar --debug
        ```

## 叁、lazy Initialization

+ what
    + When lazy initialization is enabled, beans are created as they are needed rather than during application startup
    + shortcoming
        + A downside of lazy initialization is that it can delay the discovery of a problem with the application
        + Care must also be taken to ensure that the JVM has sufficient memory to accommodate all of the application’s beans and not just those that are initialized during startup.
+ why
+ how
    + lazy initialization is not enabled by default and it is recommended that ==fine-tuning of the JVM’s heap size== is done before enabling lazy initialization.