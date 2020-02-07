package jvm.类文件结构;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/1/23 23:24
 * @description
 */
public class Math {

    public static final int initData = 666;
    public static HelloWorld hello = new HelloWorld();

    public int compute() {
        int a = 1;
        int b = 2;
        int c = (a+b)*10;
        return c;
    }

    public static void main(String[] args) {
        Math math = new Math();
        math.compute();
        System.out.println("运行结束");
    }

}
