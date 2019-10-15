# SpringMVC自动配置原理

---

[SpringMVC自动配置原理](https://docs.spring.io/spring-boot/docs/2.1.8.RELEASE/reference/html/boot-features-developing-web-applications.html "SpringMVC自动配置原理")

## 1、自动配置原理

Spring Boot provides auto-configuration for Spring MVC that works well with most applications.
The auto-configuration adds the following features on top of Spring’s defaults:

1、Inclusion of ContentNegotiatingViewResolver and BeanNameViewResolver beans.

+ **自动配置ViewResolver（视图解析器,根据方法的返回值得到视图对象（View），视图对象决定如何渲染（转发、重定向））**

+ **ContentNegotiatingViewResolver：组合所有的视图解析器**

2、Support for serving static resources, including support for WebJars (covered later in this document)).
3、Automatic registration of Converter, GenericConverter, and Formatter beans.

+ **Converter（数据类型转换）**
+ **Formater（数据格式化，比如日期）**

4、Support for HttpMessageConverters (covered later in this document).

+ **HttpMessageConverter：SpringMVC用来转换Http请求和响应的：User类 --> Json格式**

5、Automatic registration of MessageCodesResolver (covered later in this document).
6、Static index.html support.
7、Custom Favicon support (covered later in this document).
8、Automatic use of a ConfigurableWebBindingInitializer bean (covered later in this document).

If you want to keep Spring Boot MVC features and you want to add additional MVC configuration (interceptors, formatters, view controllers, and other features), you can add your own @Configuration class of type WebMvcConfigurer but without @EnableWebMvc. If you wish to provide custom instances of RequestMappingHandlerMapping, RequestMappingHandlerAdapter, or ExceptionHandlerExceptionResolver, you can declare a WebMvcRegistrationsAdapter instance to provide such components.

If you want to take complete control of Spring MVC, you can add your own @Configuration annotated with @EnableWebMvc.
