package 异常;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/1/23 10:20
 * @description
 */
public class Demo2 {

    static int methodA() throws Exception{
        try {
            int i = 1/0;
            return i;
        } catch (Exception e) {
            throw e;
        } finally {
            return -1;
        }
    }

    static int methodB() throws Exception {
        try {
            int i = 1/0;
            return i;
        } catch (Exception e) {
            throw e;
        } finally {

        }
    }

    public static void main(String[] args) {
        try {
            int a = methodA();
        } catch (Exception e) {
            e.printStackTrace();
        }

        try {
            int b = methodB();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        System.out.println("运行结束");
    }
}
