package 算法4.排序_第一版;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/2/6 17:26
 * @description 希尔排序
 *
 * 选择排序 -> 插入排序 -> 希尔排序
 */
public class ShellSort {

    public static <T extends Number & Comparable<T>> void sort(T[] array) {
        int L = array.length;
        int h = 1;
        while (h < L / 3) h = 3 * h + 1;
        while (h > 0) {
            for (int i = h; i + h < L; i++) {
                for (int j = i - h; j > -1 && (array[j + h].compareTo(array[j]) < 0); j -= h) {
                    T temp = array[j];
                    array[j] = array[j + h];
                    array[j + h] = temp;
                }
            }
            h /= 3;
        }
    }

    public static void main(String[] args) {
        Integer[] array = new Integer[]{
                9, 3, 0, 2, 10, 7, 11
        };
        System.out.println("排序前");
        for (Integer i : array) {
            System.out.print(i + " ");
        }
        ShellSort.sort(array);
        System.out.println("");
        System.out.println("排序后");
        for (Integer i : array) {
            System.out.print(i + " ");
        }
    }

}
