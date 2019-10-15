# web开发

---

静态资源的映射规则

WebMvcAutoConfiguration -> addRecourceHandler

```java
public void addResourceHandlers(ResourceHandlerRegistry registry) {
            if (!this.resourceProperties.isAddMappings()) {
                logger.debug("Default resource handling disabled");
            } else {
                Duration cachePeriod = this.resourceProperties.getCache().getPeriod();
                CacheControl cacheControl = this.resourceProperties.getCache().getCachecontrol().toHttpCacheControl();
                if (!registry.hasMappingForPattern("/webjars/**")) {
                    this.customizeResourceHandlerRegistration(registry.addResourceHandler(new String[]{"/webjars/**"}).addResourceLocations(new String[]{"classpath:/META-INF/resources/webjars/"}).setCachePeriod(this.getSeconds(cachePeriod)).setCacheControl(cacheControl));
                }

                String staticPathPattern = this.mvcProperties.getStaticPathPattern();
                if (!registry.hasMappingForPattern(staticPathPattern)) {
                    this.customizeResourceHandlerRegistration(registry.addResourceHandler(new String[]{staticPathPattern}).addResourceLocations(WebMvcAutoConfiguration.getResourceLocations(this.resourceProperties.getStaticLocations())).setCachePeriod(this.getSeconds(cachePeriod)).setCacheControl(cacheControl));
                }

            }
        }
```

==1、所有/webjars/**，都去classpath:/META-INF/resources/webjars/找资源==

+ 以jar包的方式导入静态资源，依赖于[www.webjars.org](https://www.webjars.org/"www.webjars.org")中查找

+ 引入xml

  ```xml
  <dependency>
    <groupId>org.webjars</groupId>
    <artifactId>jquery</artifactId>
    <version>3.3.1</version>
  </dependency>
  ```

+ jar包结构如下图
![webjars](/pic/2019-09-05_201235.png "webjars")

+ [localhost:8080/webjars/jquery/3.3.1/jquery.js](http://localhost:8080/webjars/jquery/3.3.1/jquery.js "webjars")能访问该资源

==2、/**，访问当前项目下的任何资源==

```java
{
    "classpath:/META-INF/resources/", // resouces/META-INF/resources
    "classpath:/resources/", // resouces/resources
    "classpath:/static/", // resouces/static
    "classpath:/public/" // resouces/public
}
```

localhost:8080/abc  ->  去静态资源文件夹里面找abc（上面的四个路径）

==3、欢迎页，静态资源文件夹下（上面的四个路径）的index.html页面，被/**映射==

```java
@Bean
public WelcomePageHandlerMapping welcomePageHandlerMapping(ApplicationContext applicationContext) {
    WelcomePageHandlerMapping welcomePageHandlerMapping = new WelcomePageHandlerMapping(new TemplateAvailabilityProviders(applicationContext), applicationContext, this.getWelcomePage(), this.mvcProperties.getStaticPathPattern());
    welcomePageHandlerMapping.setInterceptors(this.getInterceptors());
    return welcomePageHandlerMapping;
}

private Optional<Resource> getWelcomePage() {
    String[] locations = WebMvcAutoConfiguration.getResourceLocations(this.resourceProperties.getStaticLocations());
    return Arrays.stream(locations).map(this::getIndexHtml).filter(this::isReadable).findFirst();
}

private Resource getIndexHtml(String location) {
    return this.resourceLoader.getResource(location + "index.html");
}
```

localhost:8080/

==4、图标，所有的**/favicon.ico，都在静态文件夹下（上面的四个路径）==

```java
@Bean
public SimpleUrlHandlerMapping faviconHandlerMapping() {
    SimpleUrlHandlerMapping mapping = new SimpleUrlHandlerMapping();
    mapping.setOrder(-2147483647);
    mapping.setUrlMap(Collections.singletonMap("**/favicon.ico", this.faviconRequestHandler()));
    return mapping;
}


@Bean
public ResourceHttpRequestHandler faviconRequestHandler() {
    ResourceHttpRequestHandler requestHandler = new ResourceHttpRequestHandler();
    requestHandler.setLocations(this.resolveFaviconLocations());
    return requestHandler;
}


private List<Resource> resolveFaviconLocations() {
    String[] staticLocations = WebMvcAutoConfiguration.getResourceLocations(this.resourceProperties.getStaticLocations());
    List<Resource> locations = new ArrayList(staticLocations.length + 1);
    Stream var10000 = Arrays.stream(staticLocations);
    ResourceLoader var10001 = this.resourceLoader;
    this.resourceLoader.getClass();
    var10000.map(var10001::getResource).forEach(locations::add);
    locations.add(new ClassPathResource("/"));
    return Collections.unmodifiableList(locations);
}
```

==5、静态文件夹路径也支持配置，且支持多个==

```properties
spring.resource.static-locations=classpath:/hello,classpath:/zn
```
s
6、this.resourceProperties.getStaticLocations()贯穿全场
