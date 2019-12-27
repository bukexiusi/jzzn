/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2019/11/24 13:34
 * @description
 */
public class HelloWorld {

    public static void methodA() {
        System.out.println("调用methodA成功");
    }

    public void methodB() {
        System.out.println("调用methodB成功");
    }

    public String methodC() {
        return "zn";
    }

    public static int methodD() {
        int a = 2;
        int b = 3;
        int c = a * b;
        return c;
    }

    public static void main(String[] args) {
        int c = methodD();
        System.out.println("Hello, world!");
    }

}
