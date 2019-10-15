# 自定义banner

---

+ properties配置实现

```java
private Banner getBanner(Environment environment) {
    SpringApplicationBannerPrinter.Banners banners = new SpringApplicationBannerPrinter.Banners();
    banners.addIfNotNull(this.getImageBanner(environment));
    banners.addIfNotNull(this.getTextBanner(environment));
    if (banners.hasAtLeastOneBanner()) {
        return banners;
    } else {
        return this.fallbackBanner != null ? this.fallbackBanner : DEFAULT_BANNER;
    }
}

static final String[] IMAGE_EXTENSION = new String[]{"gif", "jpg", "png"};
```

this.getImageBanner(environment) 获取图片格式banner
this.getTextBanner(environment)  获取txt格式banner

若图片和txt两者都有，则两者都会输出，且优先输出图片格式banner，图片格式先后顺序gif,jpg,png

实现配置如下:

```properties
spring.banner.location=banner.txt
spring.banner.image.location=banner.png
```

以上配置的默认值如上所示，即，只需要在类路径(resources)下存在对应的文件，不需要配置即可生效。

+ 自定义类实现

```java
package com.zn.springboot5web.customize;

import org.springframework.boot.Banner;
import org.springframework.boot.SpringBootVersion;
import org.springframework.boot.ansi.AnsiColor;
import org.springframework.boot.ansi.AnsiOutput;
import org.springframework.boot.ansi.AnsiStyle;
import org.springframework.core.env.Environment;

import java.io.PrintStream;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2019/9/10 17:32
 * @description
 */
public class BannerCustomize implements Banner {
    private static final String[] BANNER = new String[]{"", "  .   ____          _            __ _ _", " /\\\\ / ___\'_ __ _ _(_)_ __  __ _ \\ \\ \\ \\", "( ( )\\___ | \'_ | \'_| | \'_ \\/ _` | \\ \\ \\ \\", " \\\\/  ___)| |_)| | | | | || (_| |  ) ) ) )", "  \'  |____| .__|_| |_|_| |_\\__, | / / / /", " =========|_|==============|___/=/_/_/_/"};
    private static final String SPRING_BOOT = " :: Spring Boot :: ";
    private static final int STRAP_LINE_SIZE = 42;

    public BannerCustomize() {
    }

    public void printBanner(Environment environment, Class<?> sourceClass, PrintStream printStream) {
        String[] version = BANNER;
        int padding = version.length;

        for (int var6 = 0; var6 < padding; ++var6) {
            String line = version[var6];
            printStream.println(line);
        }

        String var8 = SpringBootVersion.getVersion();
        var8 = var8 == null ? "" : " (v" + var8 + ")";

        String var9;
        for (var9 = ""; var9.length() < 42 - (var8.length() + " :: Spring Boot :: ".length()); var9 = var9 + " ") {
        }

        printStream.println(AnsiOutput.toString(
                new Object[]{
                        AnsiColor.GREEN, " :: Spring Boot :: ",
                        AnsiColor.DEFAULT, var9,
                        AnsiStyle.FAINT, var8
                })
        );
        printStream.println((AnsiOutput.toString(AnsiColor.BRIGHT_BLUE, "图南自定义banner")));
    }

}

```

```java
@SpringBootApplication
public class SpringBoot5WebApplication {

    public static void main(String[] args) {
        SpringApplication app = new SpringApplication(SpringBoot5WebApplication.class);
        Banner banner = new BannerCustomize();
        app.setBanner(banner);                // 注入自定义Banner
//        app.setBannerMode(Banner.Mode.OFF); // 禁用Banner
        app.run(args);
    }
}
```
