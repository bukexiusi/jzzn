# web

---

+ 前后端不分离防止表单重复提交(重定向)

```java
public String login(@RequestParam("username") String username,
                    @RequestParam("password") String password) {
    return "redirect:/main.html";
}
```

+ 自定义错误返回json数据

方法一：

```java
package com.zn.springboot5web.handler;

import com.zn.springboot5web.exception.MyJsonException;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.HashMap;
import java.util.Map;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2019/9/10 1:09
 * @description
 */

@ControllerAdvice
public class MyExceptionHandler {

    @ResponseBody
    @ExceptionHandler(MyJsonException.class)
    public Map<String, Object> handlerException(Exception e) {
        Map<String, Object> map = new HashMap<>();
        map.put("code", "user.noteexists");
        map.put("msg", e.getMessage());
        return map;
    }

}

```

缺点是没有自适应效果（浏览器访问返回页面，客户端访问返回json数据），浏览器和客户端返回的都是json数据

+ 内置servlet容器参数修改

方法一：
server.port=8081
server.xxx
server.tomcat.xxx

方法二：
容器定制器
（xxxCustomerizer）
