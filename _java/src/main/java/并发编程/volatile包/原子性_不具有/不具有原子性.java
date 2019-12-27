package 并发编程.volatile包.原子性_不具有;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2019/11/24 13:37
 * @description
 * 理想中
 */
public class 不具有原子性 {

    public static volatile int num = 0;

    public static void increase() {
        num ++;
    }

    public static void main(String[] args) throws InterruptedException{

        Thread[] array = new Thread[10];
        for (int i = 0; i < 10; i++) {
            Thread t = new Thread(new Runnable() {
                public void run() {
                    for (int i=0; i < 1000; i++) { //
                        increase();
                    }
                }
            });
            t.start();
            array[i] = t;
        }

        for (Thread td: array) {
            td.join();
        }

        System.out.println(num);

    }

}
