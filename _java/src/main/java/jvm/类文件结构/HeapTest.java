package jvm.类文件结构;

import java.util.ArrayList;
import java.util.List;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/1/29 11:28
 * @description
 */
public class HeapTest {

    byte[] a = new byte[1024*10]; // 100KB

    public static void main(String[] args) throws InterruptedException {
        List<HeapTest> heapTests = new ArrayList<HeapTest>();
        while (true) {
            heapTests.add(new HeapTest());
            Thread.sleep(10);
        }
    }

}
